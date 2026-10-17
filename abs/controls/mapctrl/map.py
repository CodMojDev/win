from win.abs.axhost import *
from win.com.mshtml import *
from win.com.comtl.baseface import *
from win.com.dispatch import *
from win.abs.core.uri import *

class MapControl(AxHost):
    class Mark:
        ctrl: 'MapControl'
        name: str
        
        def __init__(self, ctrl: 'MapControl', name: str):
            self.ctrl = ctrl
            self.name = name
        
        def delete(self):
            """
            Delete the mark from map.
            """
            self.ctrl._execute_script(f'map.deleteLayer({self.name}); {self.name} = null;')
            
        def popup(self, string: str):
            """
            Add popup to the mark.
            """
            self.ctrl._execute_script(f'{self.name}.bindPopup("{string}").openPopup();')
    
    _tile_url: str
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU, 
                 tile_url: str = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'):
        super().__init__('htmlfile', width, height, parent, identifier)
        self._tile_url = tile_url
    
    def _execute_script(self, code: str):
        holder = TL_GUARD_OBJECT()
        document = self.get_control(IHTMLDocument2)
        TlAddRefGuardMultiEx(holder, document)
        window = IHTMLWindow2.NULL()
        hr = document.get_parentWindow(byref(window))
        if FAILED(hr): raise COMError(hr)
        window = window.contents
        TlAddRefGuardMultiEx(holder, window)
        bstrCode = BSTR.new(code)
        out = Variant()
        hr = window.execScript(bstrCode, NULL, out.ref())
        out.clear()
        bstrCode.free()
        if FAILED(hr): raise COMError(hr)
    
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(x, y, relative)
        holder = TL_GUARD_OBJECT()
        document = self.get_control(IHTMLDocument2)
        TlAddRefGuardEx(holder, document)
        with open(script_relative('data/map.html'), 'r') as file:
            data = file.read()
        with open(script_relative('data/leaflet.css'), 'r') as file:
            data = data.replace('/* [MAP CONTROL] PLACEHOLDER - STYLESHEET */', file.read())
        with open(script_relative('data/leaflet.js'), 'r') as file:
            data = data.replace('/* [MAP CONTROL] PLACEHOLDER - SCRIPT */', file.read())
        with open(script_relative('data/json2.js'), 'r') as file:
            data = data.replace('//* [MAP CONTROL] PLACEHOLDER - JSON POLYFILL (IE6) */', file.read())
        data = data.replace(
            '[MAP CONTROL] PLACEHOLDER - ICON PATH',
            URL.path(script_relative('data')).value)
        data = data.replace('[MAP CONTROL] PLACEHOLDER - TILE URL', self._tile_url)
        variant = Variant()
        variant.value = data
        array = SafeArray.typed(Variant).create([variant])
        document.write(array.ref())
        variant.clear()
        
    def locate(self, latitude: SupportsFloat, longitude: SupportsFloat, zoom: int):
        """
        Locate to the given Lat./Lon. and set the zoom.
        """
        self._execute_script(f'map.setView([{latitude}, {longitude}], {zoom});')
        
    def mark(self, latitude: SupportsFloat, longitude: SupportsFloat) -> Mark:
        """
        Add the mark to map.
        """
        variable = f'MARK_{str(latitude).replace(".", "_")}_{str(longitude).replace(".", "_")}'
        self._execute_script(f'var {variable} = L.marker([{latitude}, {longitude}]).addTo(map);')
        return self.Mark(self, variable)
    
    def geolocate(self):
        """
        Locate the map position by the GeoIP position.
        """
        self._execute_script('locateByGeoIP();')