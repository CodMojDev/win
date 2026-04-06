from .jni import *

null = NULL

class JInteropMethod:
    _methodIDinfo: dict[str, tuple[str, jmethodID]]
    _jnidescInfo: str | set[str]
    _boundJobject: jobject
    _static: bool
    _name: str
    
    _keepRef: Any
    
    def __init__(self, name: str, jnidescInfo: str | set[str], 
                 methodIDinfo: dict[str, jmethodID],
                 boundJobject: TUnion[jobject, 'JInteropObject', type['JInteropObject']],
                 static: bool = False):
        self._methodIDinfo = methodIDinfo
        self._jnidescInfo = jnidescInfo
        self._static = static
        self._name = name
        
        if boundJobject is not None:
            if isinstance(boundJobject, JInteropObject):
                self._boundJobject = boundJobject._object
            elif isinstance(boundJobject, type) and issubclass(boundJobject, JInteropObject):
                self._boundJobject = boundJobject._clazz
        else:
            self._boundJobject = boundJobject
            
        self._keepRef = boundJobject
            
    def __call__(self, *args):
        jnidescInfo = self._jnidescInfo
        
        if not isinstance(jnidescInfo, set):
            jnidescInfo = {jnidescInfo}
        
        foundMethod = False
        arguments = []
        variadic = []
        
        for jnidesc in jnidescInfo:
            jnidescReprs = JInteropObject.parse_jnidesc_parameters(jnidesc)
            
            if len(jnidescReprs) == len(args):
                iterationFailure = False
                for i, jnidescRepr in enumerate(jnidescReprs):
                    if not jnidescRepr.is_compatible(args[i]):
                        iterationFailure = True
                        break
                
                if not iterationFailure:
                    jnidesc2 = jnidesc
                    foundMethod = True
                    for i, arg in enumerate(args):
                        arguments.append(jnidescReprs[i].marshal_value(arg))
                        variadic.append(jnidescReprs[i].get_c_type())
                        
                    break
        
        if not foundMethod:
            raise ValueError('Not found method signature for providen arguments.')
        
        returnTypeJnidesc, methodID = self._methodIDinfo[self._name+jnidesc2]
        env = JInteropObject._ensureEnv()
        boundJobject = self._boundJobject
        
        if self._name == '<init>':
            result = env.NewObject(boundJobject, methodID, *arguments, variadic=variadic)
        elif returnTypeJnidesc == 'Z':
            if self._static:
                result = env.CallStaticBooleanMethod(boundJobject, methodID, *arguments, variadic=variadic) == JNI_TRUE
            else:
                result = env.CallBooleanMethod(boundJobject, methodID, *arguments, variadic=variadic) == JNI_TRUE
        elif returnTypeJnidesc == 'B':
            if self._static:
                result = env.CallStaticByteMethod(boundJobject, methodID, *arguments, variadic=variadic)
            else:
                result = env.CallByteMethod(boundJobject, methodID, *arguments, variadic=variadic)
        elif returnTypeJnidesc == 'C':
            if self._static:
                result = chr(env.CallStaticCharMethod(boundJobject, methodID, *arguments, variadic=variadic))
            else:
                result = chr(env.CallCharMethod(boundJobject, methodID, *arguments, variadic=variadic))
        elif returnTypeJnidesc == 'S':
            if self._static:
                result = env.CallStaticShortMethod(boundJobject, methodID, *arguments, variadic=variadic)
            else:
                result = env.CallShortMethod(boundJobject, methodID, *arguments, variadic=variadic)
        elif returnTypeJnidesc == 'I':
            if self._static:
                result = env.CallStaticIntMethod(boundJobject, methodID, *arguments, variadic=variadic)
            else:
                result = env.CallIntMethod(boundJobject, methodID, *arguments, variadic=variadic)
        elif returnTypeJnidesc == 'J':
            if self._static:
                result = env.CallStaticLongMethod(boundJobject, methodID, *arguments, variadic=variadic)
            else:
                result = env.CallLongMethod(boundJobject, methodID, *arguments, variadic=variadic)
        elif returnTypeJnidesc == 'F':
            if self._static:
                result = env.CallStaticFloatMethod(boundJobject, methodID, *arguments, variadic=variadic)
            else:
                result = env.CallFloatMethod(boundJobject, methodID, *arguments, variadic=variadic)
        elif returnTypeJnidesc == 'D':
            if self._static:
                result = env.CallStaticDoubleMethod(boundJobject, methodID, *arguments, variadic=variadic)
            else:
                result = env.CallDoubleMethod(boundJobject, methodID, *arguments, variadic=variadic)
        elif returnTypeJnidesc == 'V':
            result = None
            if self._static:
                env.CallStaticVoidMethod(boundJobject, methodID, *arguments, variadic=variadic)
            else:
                env.CallVoidMethod(boundJobject, methodID, *arguments, variadic=variadic)
        else:
            if self._static:
                result = env.CallStaticObjectMethod(boundJobject, methodID, *arguments, variadic=variadic)
            else:
                result = env.CallObjectMethod(boundJobject, methodID, *arguments, variadic=variadic)
            result = JInteropObject.construct(returnTypeJnidesc).from_object(result)
        
        JInteropObject.jni_check_errors()
        
        for i, jnidescRepr in enumerate(jnidescReprs):
            jnidescRepr.deallocate(arguments[i])
        
        return result

class JClassDescriptor:
    def __get__(self, instance, owner: type['JInteropObject']) -> 'JInteropObject':
        env = JInteropObject._ensureEnv()
        clazz = env.GetObjectClass(owner._clazz)
        return JInteropObject.construct('java/lang/Class').from_object(clazz)

class IJniDescRepr(IMarshaller):
    jnidesc: str
    
    @interface_abstract_method
    def is_compatible(self, argument) -> bool: ...
    
    @interface_abstract_method
    def __repr__(self) -> str: ...
    
    @interface_abstract_method
    def deallocate(self, value): ...
    
    @interface_abstract_method
    def get_c_type(self): ...
    
class JNIDescLRepr(IJniDescRepr):
    def __init__(self, jnidescLclass: str):
        self.jnidesc = jnidescLclass
    
    def __repr__(self) -> str:
        return f"{self.jnidesc.replace('/', '.')}"
    
    def is_compatible(self, argument) -> bool:
        if argument is None:
            return True
        
        env = JInteropObject._ensureEnv()
        jnidesc = self.jnidesc
        
        if PtrUtil.is_pointer(argument):
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.IsInstanceOf(argument, jClass)
            env.DeleteLocalRef(jClass)
            return result == JNI_TRUE
        if isinstance(argument, JInteropObject):
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.IsInstanceOf(argument._object, jClass)
            env.DeleteLocalRef(jClass)
            return result == JNI_TRUE
        if jnidesc == 'java/lang/String':
            return isinstance(argument, str)
        if jnidesc == 'java/lang/Boolean':
            return isinstance(argument, bool) or argument in (JNI_TRUE, JNI_FALSE)
        if jnidesc == 'java/lang/Byte':
            if isinstance(argument, (c_byte, BYTE)):
                return True
            if isinstance(argument, int):
                return integerInRange(argument, BYTE_RANGE)
            return False
        if jnidesc == 'java/lang/Character':
            if isinstance(argument, (WCHAR, SHORT, USHORT)):
                return True
            if isinstance(argument, (str, bytes)) and len(argument) == 1:
                return True
            if isinstance(argument, int):
                return integerInRange(argument, CHAR_RANGE)
            return False
        if jnidesc == 'java/lang/Short':
            if isinstance(argument, (SHORT, USHORT)):
                return True
            if isinstance(argument, int):
                return integerInRange(argument, SHORT_RANGE)
            return False
        if jnidesc == 'java/lang/Integer':
            if isinstance(argument, (INT, UINT)):
                return True
            if isinstance(argument, int):
                return integerInRange(argument, INT_RANGE)
            return False
        if jnidesc == 'java/lang/Long':
            if isinstance(argument, (LONGLONG, ULONGLONG)):
                return True
            if isinstance(argument, int):
                return integerInRange(argument, LONG_RANGE)
            return False
        if jnidesc == 'java/lang/Float':
            return isinstance(argument, (float, c_float))
        if jnidesc == 'java/lang/Double':
            return isinstance(argument, (float, c_double))
        
        return False
    
    def marshal_value(self, value):
        env = JInteropObject._ensureEnv()
        
        if isinstance(value, JInteropObject):
            return env.NewLocalRef(value._object)
        
        jnidesc = self.jnidesc
        
        if jnidesc == 'java/lang/String':
            return env.NewString(value, len(value))
        if jnidesc == 'java/lang/Boolean':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JInteropObject._interopMethodIDCache['Boolean.valueOf'], 
                JNI_TRUE if value else JNI_FALSE, variadic=(jboolean,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Byte':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JInteropObject._interopMethodIDCache['Byte.valueOf'], 
                value, variadic=(jbyte,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Character':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            if isinstance(value, str):
                value = ord(value)
            elif isinstance(value, bytes):
                value = value[0]
            result = env.CallObjectMethod(
                jClass, JInteropObject._interopMethodIDCache['Character.valueOf'], 
                value, variadic=(jchar,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Short':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JInteropObject._interopMethodIDCache['Short.valueOf'], 
                value, variadic=(jshort,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Integer':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JInteropObject._interopMethodIDCache['Integer.valueOf'], 
                value, variadic=(jint,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Long':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JInteropObject._interopMethodIDCache['Long.valueOf'], 
                value, variadic=(jlong,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Float':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JInteropObject._interopMethodIDCache['Float.valueOf'], 
                value, variadic=(jfloat,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Double':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JInteropObject._interopMethodIDCache['Double.valueOf'], 
                value, variadic=(jdouble,))
            env.DeleteLocalRef(jClass)
            return result
        
        return value
    
    def deallocate(self, value):
        env = JInteropObject._ensureEnv()
        env.DeleteLocalRef(value)
        
    def get_c_type(self):
        return jobject
    
def integerInRange(integer: int, range: tuple[int, int]) -> bool:
    return integer >= range[0] and integer <= range[1]
    
BYTE_RANGE = (-128, 127)
CHAR_RANGE = (0, 65535)
SHORT_RANGE = (-32768, 32767)
INT_RANGE = (-2147483648, 2147483647)
LONG_RANGE = (-9223372036854775808, 9223372036854775807)

class JNIDescPrimitiveRepr(IJniDescRepr):
    def __init__(self, jnidesc: str):
        self.jnidesc = jnidesc
    
    def __repr__(self) -> str:
        jnidesc = self.jnidesc
        if jnidesc == 'Z':
            return 'boolean'
        if jnidesc == 'B':
            return 'byte'
        if jnidesc == 'C':
            return 'char'
        if jnidesc == 'S':
            return 'short'
        if jnidesc == 'I':
            return 'int'
        if jnidesc == 'J':
            return 'long'
        if jnidesc == 'F':
            return 'float'
        if jnidesc == 'D':
            return 'double'
        
    def is_compatible(self, argument) -> bool:
        jnidesc = self.jnidesc
        if jnidesc == 'Z':
            return isinstance(argument, bool) or argument in (JNI_TRUE, JNI_FALSE)
        if jnidesc == 'B':
            if isinstance(argument, (c_byte, BYTE)):
                return True
            if isinstance(argument, int):
                return integerInRange(argument, BYTE_RANGE)
            return False
        if jnidesc == 'C':
            if isinstance(argument, (WCHAR, SHORT, USHORT)):
                return True
            if isinstance(argument, (str, bytes)) and len(argument) == 1:
                return True
            if isinstance(argument, int):
                return integerInRange(argument, CHAR_RANGE)
            return False
        if jnidesc == 'S':
            if isinstance(argument, (SHORT, USHORT)):
                return True
            if isinstance(argument, int):
                return integerInRange(argument, SHORT_RANGE)
            return False
        if jnidesc == 'I':
            if isinstance(argument, (INT, UINT)):
                return True
            if isinstance(argument, int):
                return integerInRange(argument, INT_RANGE)
            return False
        if jnidesc == 'J':
            if isinstance(argument, (LONGLONG, ULONGLONG)):
                return True
            if isinstance(argument, int):
                return integerInRange(argument, LONG_RANGE)
            return False
        if jnidesc == 'F':
            return isinstance(argument, (float, c_float))
        if jnidesc == 'D':
            return isinstance(argument, (float, c_double))
        return False
    
    def marshal_value(self, value):
        jnidesc = self.jnidesc
        if jnidesc == 'Z':
            return JNI_TRUE if value else JNI_FALSE
        if jnidesc == 'C':
            if isinstance(value, str):
                value = ord(value)
            elif isinstance(value, bytes):
                value = value[0]
            return value
        return value
    
    def deallocate(self, value):
        return
    
    def get_c_type(self):
        jnidesc = self.jnidesc
        if jnidesc == 'Z':
            return jboolean
        if jnidesc == 'B':
            return jbyte
        if jnidesc == 'C':
            return jchar
        if jnidesc == 'S':
            return jshort
        if jnidesc == 'I':
            return jint
        if jnidesc == 'J':
            return jlong
        if jnidesc == 'F':
            return jfloat
        if jnidesc == 'D':
            return jdouble
    
class JNIDescArrayRepr(IJniDescRepr):
    descItemType: IJniDescRepr
    
    def __init__(self, descItemType: IJniDescRepr):
        self.descItemType = descItemType
        
        desc = self.descItemType
        self.jnidesc = ''
        while isinstance(desc, JNIDescArrayRepr):
            self.jnidesc += '['
            desc = desc.descItemType
        self.jnidesc += 'L' + desc.jnidesc + ';'
    
    def __repr__(self) -> str:
        return f'{self.descItemType}[]'
    
    def is_compatible(self, argument) -> bool:
        if not isinstance(argument, (list, tuple)):
            return False
        for value in argument:
            if not self.descItemType.is_compatible(value):
                return False
        return True
    
    def marshal_value(self, value):
        env = JInteropObject._ensureEnv()
        descItemType = self.descItemType
        length = len(value)
        
        if isinstance(descItemType, JNIDescPrimitiveRepr):
            jnidesc = descItemType.jnidesc
            
            if jnidesc == 'Z':
                array = env.NewBooleanArray(length)
                elements = env.GetBooleanArrayElements(array, NULL)
                delRoutine = env.ReleaseBooleanArrayElements
            elif jnidesc == 'B':
                array = env.NewByteArray(length)
                elements = env.GetByteArrayElements(array, NULL)
                delRoutine = env.ReleaseByteArrayElements
            elif jnidesc == 'C':
                array = env.NewCharArray(length)
                elements = env.GetCharArrayElements(array, NULL)
                delRoutine = env.ReleaseCharArrayElements
            elif jnidesc == 'S':
                array = env.NewShortArray(length)
                elements = env.GetShortArrayElements(array, NULL)
                delRoutine = env.ReleaseShortArrayElements
            elif jnidesc == 'I':
                array = env.NewIntArray(length)
                elements = env.GetIntArrayElements(array, NULL)
                delRoutine = env.ReleaseIntArrayElements
            elif jnidesc == 'J':
                array = env.NewLongArray(length)
                elements = env.GetLongArrayElements(array, NULL)
                delRoutine = env.ReleaseLongArrayElements
            elif jnidesc == 'F':
                array = env.NewFloatArray(length)
                elements = env.GetFloatArrayElements(array, NULL)
                delRoutine = env.ReleaseFloatArrayElements
            elif jnidesc == 'D':
                array = env.NewDoubleArray(length)
                elements = env.GetDoubleArrayElements(array, NULL)
                delRoutine = env.ReleaseDoubleArrayElements
            
            for i in range(length):
                elements[i] = descItemType.marshal_value(value[i])
            
            delRoutine(array, elements, 0)
            
            return array
        
        elif isinstance(descItemType, JNIDescLRepr):
            jClass = JInteropObject.find_jni_class(descItemType.jnidesc)
            array = env.NewObjectArray(length, jClass, NULL)
            
            for i in range(length):
                marshalled = descItemType.marshal_value(value[i])
                env.SetObjectArrayElement(array, i, marshalled)
                descItemType.deallocate(marshalled)
                
            env.DeleteLocalRef(jClass)
            return array
        elif isinstance(descItemType, JNIDescArrayRepr):
            jClass = JInteropObject.find_jni_class(self.jnidesc[1:])
            array = env.NewObjectArray(length, jClass, NULL)
            
            for i in range(length):
                marshalled = descItemType.marshal_value(value[i])
                env.SetObjectArrayElement(array, i, marshalled)
                descItemType.deallocate(marshalled)
                
            env.DeleteLocalRef(jClass)
            return array
        
    def deallocate(self, value):
        env = JInteropObject._ensureEnv()
        env.DeleteLocalRef(value)
        
    def get_c_type(self):
        return jarray

class JInteropMeta(type):
    _staticMethodsIDCache: dict[str, tuple[str, jmethodID]] = {}
    _staticFieldsIDCache: dict[str, tuple[str, jfieldID]] = {}
    _staticMethods: dict[str, str | set[str]] = {}
    _classLoaders: list[jobject] = []
    
    _clazz: jclass = None
    
    def __getattr__(cls, name: str):
        env = JInteropObject._ensureEnv()
        
        if name in cls._staticFieldsIDCache:
            jnidesc, fieldID = cls._staticFieldsIDCache[name]
            
            if jnidesc == 'Z':
                return env.GetStaticBooleanField(cls._clazz, fieldID) == JNI_TRUE
            if jnidesc == 'B':
                return env.GetStaticByteField(cls._clazz, fieldID)
            if jnidesc == 'C':
                return env.GetStaticCharField(cls._clazz, fieldID)
            if jnidesc == 'S':
                return env.GetStaticShortField(cls._clazz, fieldID)
            if jnidesc == 'I':
                return env.GetStaticIntField(cls._clazz, fieldID)
            if jnidesc == 'J':
                return env.GetStaticLongField(cls._clazz, fieldID)
            if jnidesc == 'F':
                return env.GetStaticFloatField(cls._clazz, fieldID)
            if jnidesc == 'D':
                return env.GetStaticFloatField(cls._clazz, fieldID)
            if jnidesc[0] == 'L':
                jObject = env.GetStaticObjectField(cls._clazz, fieldID)
                jInteropObject = JInteropObject.construct(jnidesc).from_object(jObject)
                env.DeleteLocalRef(jObject)
                return jInteropObject
            
        if name in cls._staticMethods:
            return JInteropMethod(name, cls._staticMethods[name], cls._staticMethodsIDCache, cls, True)
            
    def __setattr__(cls, name: str, value):
        if name in JInteropObject.__annotations__: return type.__setattr__(cls, name, value)
        env = JInteropObject._ensureEnv()
        
        if name in cls._staticFieldsIDCache:
            jnidesc, fieldID = cls._staticFieldsIDCache[name]
            
            if jnidesc == 'Z':
                return env.SetStaticBooleanField(
                    cls._clazz, fieldID, 
                    JNI_TRUE if value else JNI_FALSE)
            if jnidesc == 'B':
                return env.SetStaticByteField(cls._clazz, fieldID, value)
            if jnidesc == 'C':
                if isinstance(value, str):
                    value = ord(value)
                elif isinstance(value, bytes):
                    value = value[0]
                return env.SetStaticCharField(cls._clazz, fieldID, value)
            if jnidesc == 'S':
                return env.SetStaticShortField(cls._clazz, fieldID, value)
            if jnidesc == 'I':
                return env.SetStaticIntField(cls._clazz, fieldID, value)
            if jnidesc == 'J':
                return env.SetStaticLongField(cls._clazz, fieldID, value)
            if jnidesc == 'F':
                return env.SetStaticFloatField(cls._clazz, fieldID, value)
            if jnidesc == 'D':
                return env.SetStaticDoubleField(cls._clazz, fieldID, value)
            if jnidesc[0] == 'L':
                if isinstance(value, JInteropObject):
                    return env.SetStaticObjectField(cls._clazz, fieldID, value._object)
                return env.SetStaticObjectField(cls._clazz, fieldID, value)
            
    def __del__(cls):
        env = JInteropObject._env
        if env:
            if cls._clazz:
                env.DeleteGlobalRef(cls._clazz)
            if cls.__name__ == 'JInteropObject':
                jInteropCls: type[JInteropObject] = cls
                for classLoader in jInteropCls._classLoaders:
                    env.DeleteGlobalRef(classLoader)
                jInteropCls._classLoaders = []

class JInteropObject(metaclass=JInteropMeta):
    """
    Object representing Java class.
    """
    
    _interopMethodIDCache: dict[str, jmethodID] = {}
    _classLoaders: list[jobject] = []
    
    _staticMethodsIDCache: dict[str, jmethodID] = {}
    _staticFieldsIDCache: dict[str, jfieldID] = {}
    _methodsIDCache: dict[str, jmethodID] = {}
    _fieldsIDCache: dict[str, jmethodID] = {}
    
    _classesCache: dict[str, type['JInteropObject']] = {}
    
    _staticMethods: dict[str, str | set[str]] = {}
    _methods: dict[str, str | set[str]] = {}
    
    _nativeName: str = None
    _clazz: jclass = None
    
    _javaVM: JavaVM = None
    _env: JNIEnv = None
    
    _object: jobject
    
    @classmethod
    def _ensureEnv(cls) -> JNIEnv:
        env = cls._env
        
        if env is None:
            raise RuntimeError('JNIEnv (and likely Java VM) is not initialized.')
        
        return env
    
    @classmethod
    def construct(cls, nativeName: str) -> type['JInteropObject']:
        nativeName = cls.normalize_L_jnidesc(nativeName)
        JClass = JInteropObject._classesCache.get(nativeName, None)
        
        if JClass is not None:
            return JClass
        
        env = JInteropObject._ensureEnv()
        clazz = JInteropObject.find_jni_class(nativeName)
        
        if not clazz:
            raise ValueError(f'Not existing class "{nativeName}".')
        
        jclass_clazz = env.NewGlobalRef(clazz)
        env.DeleteLocalRef(clazz)
        
        class JClass(JInteropObject):
            _nativeName = nativeName
            _methods = {}
            _methodsIDCache = {}
            _staticFieldsIDCache = {}
            _staticMethods = {}
            _staticMethodsIDCache = {}
            _fieldsIDCache = {}
            _clazz = jclass_clazz
            
            # various versions of Java T.class
            class_ = JClassDescriptor()
            cls = JClassDescriptor()
            clazz = JClassDescriptor()
        
        JInteropObject._classesCache[nativeName] = JClass
        JClass.__name__ = nativeName
        JClass.initialize_type()
        
        return JClass
    
    @classmethod
    def from_object(cls, jObject: jobject) -> 'JInteropObject':
        env = JInteropObject._ensureEnv()
        
        instance = cls.__new__(cls)
        instance._object = env.NewGlobalRef(jObject)
        
        return instance
    
    @classmethod
    def load_jar(cls, jar_path: str):
        interopCache = JInteropObject._interopMethodIDCache
        env = JInteropObject._ensureEnv()
        env.ExceptionClear()
        java_io_File = env.FindClass(b'java/io/File')
        jJarPath = env.NewString(jar_path, len(jar_path))
        jJarFile = env.NewObject(
            java_io_File, interopCache['File.<init>'],
            jJarPath, variadic=(jstring,))
        JInteropObject.jni_check_errors()
        env.DeleteLocalRef(jJarPath)
        env.DeleteLocalRef(java_io_File)
        jURI = env.CallObjectMethod(jJarFile, interopCache['File.toURI'])
        JInteropObject.jni_check_errors()
        env.DeleteLocalRef(jJarFile)
        jURL = env.CallObjectMethod(jURI, interopCache['URI.toURL'])
        JInteropObject.jni_check_errors()
        env.DeleteLocalRef(jURI)
        java_net_URL = env.FindClass(b'java/net/URL')
        jUrls = env.NewObjectArray(1, java_net_URL, NULL)
        env.SetObjectArrayElement(jUrls, 0, jURL)
        env.DeleteLocalRef(jURL)
        jClassLoader = env.CallObjectMethod(java_net_URL, interopCache['Class.getClassLoader'])
        JInteropObject.jni_check_errors()
        env.DeleteLocalRef(java_net_URL)
        java_net_URLClassLoader = env.FindClass(b'java/net/URLClassLoader')
        jUrlLoader = env.NewObject(
            java_net_URLClassLoader, interopCache['URLClassLoader.<init>'],
            jUrls, jClassLoader, variadic=(jobjectArray, jobject))
        JInteropObject.jni_check_errors()
        env.DeleteLocalRef(java_net_URLClassLoader)
        env.DeleteLocalRef(jUrls)
        env.DeleteLocalRef(jClassLoader)
        JInteropObject._classLoaders.append(env.NewGlobalRef(jUrlLoader))
        env.DeleteLocalRef(jUrlLoader)
    
    def __init__(self, *args):
        env = JInteropObject._ensureEnv()
        jObject = JInteropMethod('<init>', self._methods['<init>'], self._methodsIDCache, self.__class__)(*args)
        self._object = env.NewGlobalRef(jObject)
        env.DeleteLocalRef(jObject)
    
    def __str__(self) -> str:
        env = JInteropObject._ensureEnv()
        strObject = self.toString()
        jStrObject = strObject._object
        stringChars = env.GetStringChars(jStrObject, NULL)
        string = stringChars.value
        env.ReleaseStringChars(jStrObject, stringChars)
        return string
    
    def __repr__(self) -> str:
        env = JInteropObject._ensureEnv()
        jString = env.CallObjectMethod(self._clazz, JInteropObject._interopMethodIDCache['Class.getName'])
        stringChars = env.GetStringChars(jString, NULL)
        string = stringChars.value
        env.ReleaseStringChars(jString, stringChars)
        return f'<{string} "{str(self)}">'
    
    def __eq__(self, other: 'JInteropObject') -> bool:
        env = JInteropObject._ensureEnv()
        if other is None:
            return env.IsSameObject(self._object, NULL)
        return env.IsSameObject(self._object, other._object)

    def __getattr__(self, name: str):
        env = JInteropObject._ensureEnv()
        
        if name in self._fieldsIDCache:
            jnidesc, fieldID = self._fieldsIDCache[name]
            
            if jnidesc == 'Z':
                return env.GetBooleanField(self._object, fieldID) == JNI_TRUE
            if jnidesc == 'B':
                return env.GetByteField(self._object, fieldID)
            if jnidesc == 'C':
                return env.GetCharField(self._object, fieldID)
            if jnidesc == 'S':
                return env.GetShortField(self._object, fieldID)
            if jnidesc == 'I':
                return env.GetIntField(self._object, fieldID)
            if jnidesc == 'J':
                return env.GetLongField(self._object, fieldID)
            if jnidesc == 'F':
                return env.GetFloatField(self._object, fieldID)
            if jnidesc == 'D':
                return env.GetDoubleField(self._object, fieldID)
            if jnidesc[0] == 'L':
                jObject = env.GetObjectField(self._object, fieldID)
                jInteropObject = JInteropObject.construct(jnidesc).from_object(jObject)
                env.DeleteLocalRef(jObject)
                return jInteropObject
            
        if name in self._methods:
            return JInteropMethod(name, self._methods[name], self._methodsIDCache, self)
            
    def __del__(self):
        env = JInteropObject._env
        if env:
            if self._object:
                env.DeleteGlobalRef(self._object)
            
    def __setattr__(self, name: str, value):
        if name in JInteropObject.__annotations__: return object.__setattr__(self, name, value)
        env = JInteropObject._ensureEnv()
        
        if name in self._fieldsIDCache:
            jnidesc, fieldID = self._fieldsIDCache[name]
            
            if jnidesc == 'Z':
                return env.SetBooleanField(
                    self._object, fieldID, 
                    JNI_TRUE if value else JNI_FALSE)
            if jnidesc == 'B':
                return env.SetByteField(self._object, fieldID, value)
            if jnidesc == 'C':
                if isinstance(value, str):
                    value = ord(value)
                elif isinstance(value, bytes):
                    value = value[0]
                return env.SetSCharField(self._object, fieldID, value)
            if jnidesc == 'S':
                return env.SetShortField(self._object, fieldID, value)
            if jnidesc == 'I':
                return env.SetIntField(self._object, fieldID, value)
            if jnidesc == 'J':
                return env.SetLongField(self._object, fieldID, value)
            if jnidesc == 'F':
                return env.SetFloatField(self._object, fieldID, value)
            if jnidesc == 'D':
                return env.SetDoubleField(self._object, fieldID, value)
            if jnidesc[0] == 'L':
                if isinstance(value, JInteropObject):
                    return env.SetObjectField(self._object, fieldID, value._object)
                return env.SetObjectField(self._object, fieldID, value)
        
    @classmethod
    def jni_check_errors(cls):
        env = JInteropObject._ensureEnv()
        
        if env.ExceptionCheck():
            env.ExceptionDescribe()
            env.ExceptionClear()
            raise RuntimeError('JNI/Java Exception.')
        
    @classmethod
    def initialize_type(cls):
        env = JInteropObject._ensureEnv()
        
        interopCache = JInteropObject._interopMethodIDCache
        jMethods = env.CallObjectMethod(cls._clazz, interopCache['Class.getMethods'])
        JInteropObject.jni_check_errors()
        nMethods = env.GetArrayLength(jMethods)
        
        JInteropObject.jni_check_errors()
        
        for iMeth in range(nMethods):
            jMethod = env.GetObjectArrayElement(jMethods, iMeth)
            jParameterTypes = env.CallObjectMethod(jMethod, interopCache['Method.getParameterTypes'])
            JInteropObject.jni_check_errors()
            nParameterTypes = env.GetArrayLength(jParameterTypes)
            
            jnidesc = '('
            for iParamType in range(nParameterTypes):
                jParameterType = env.GetObjectArrayElement(jParameterTypes, iParamType)
                jnidesc += cls.jclass_to_jnidesc(jParameterType)
                env.DeleteLocalRef(jParameterType)
            jnidesc += ')'
            env.DeleteLocalRef(jParameterTypes)
            
            jReturnType = env.CallObjectMethod(jMethod, interopCache['Method.getReturnType'])
            JInteropObject.jni_check_errors()
            jReturnTypeJnidesc = cls.jclass_to_jnidesc(jReturnType)
            jnidesc += jReturnTypeJnidesc
            env.DeleteLocalRef(jReturnType)
            
            jMethodName = env.CallObjectMethod(jMethod, interopCache['Method.getName'])
            JInteropObject.jni_check_errors()
            methNameChars = env.GetStringChars(jMethodName, NULL)
            methodName = methNameChars.value
            env.ReleaseStringChars(jMethodName, methNameChars)
            env.DeleteLocalRef(jMethodName)
            
            jModifiers = env.CallIntMethod(jMethod, interopCache['Method.getModifiers'])
            JInteropObject.jni_check_errors()
            
            if jModifiers & JVM_ACC_STATIC:
                methods = cls._staticMethods
            else:
                methods = cls._methods
            
            value = methods.get(methodName, None)
            
            if value is None:
                methods[methodName] = jnidesc
            elif isinstance(value, set):
                methods[methodName].add(jnidesc)
            else:
                methods[methodName] = {value, jnidesc}
            
            if jModifiers & JVM_ACC_STATIC:
                cls._staticMethodsIDCache[methodName+jnidesc] = (jReturnTypeJnidesc, env.GetStaticMethodID(cls._clazz, methodName.encode('ascii'), jnidesc.encode('ascii')))
            else:
                cls._methodsIDCache[methodName+jnidesc] = (jReturnTypeJnidesc, env.GetMethodID(cls._clazz, methodName.encode('ascii'), jnidesc.encode('ascii')))
            
            env.DeleteLocalRef(jMethod)
            
        env.DeleteLocalRef(jMethods)
        
        jFields = env.CallObjectMethod(cls._clazz, interopCache['Class.getFields'])
        JInteropObject.jni_check_errors()
        nFields = env.GetArrayLength(jFields)
        
        for iField in range(nFields):
            jField = env.GetObjectArrayElement(jFields, iField)
            jFieldType = env.CallObjectMethod(jField, interopCache['Field.getType'])
            JInteropObject.jni_check_errors()
            jnidesc = cls.jclass_to_jnidesc(jFieldType)
            jFieldName = env.CallObjectMethod(jField, interopCache['Field.getName'])
            JInteropObject.jni_check_errors()
            fieldNameChars = env.GetStringChars(jFieldName, NULL)
            fieldName = fieldNameChars.value
            env.ReleaseStringChars(jFieldName, fieldNameChars)
            env.DeleteLocalRef(jFieldName)
            env.DeleteLocalRef(jFieldType)
            
            jModifiers = env.CallIntMethod(jField, interopCache['Field.getModifiers'])
            JInteropObject.jni_check_errors()
            
            if jModifiers & JVM_ACC_STATIC:
                cls._staticFieldsIDCache[fieldName] = (jnidesc, env.GetStaticFieldID(cls._clazz, fieldName.encode('ascii'), jnidesc.encode('ascii')))
            else:
                cls._fieldsIDCache[fieldName] = (jnidesc, env.GetFieldID(cls._clazz, fieldName.encode('ascii'), jnidesc.encode('ascii')))
            
            env.DeleteLocalRef(jField)
        
        env.DeleteLocalRef(jFields)
        
        jConstructors = env.CallObjectMethod(cls._clazz, interopCache['Class.getConstructors'])
        JInteropObject.jni_check_errors()
        nConstructors = env.GetArrayLength(jConstructors)
        
        for iCtor in range(nConstructors):
            jConstructor = env.GetObjectArrayElement(jConstructors, iCtor)
            jParameterTypes = env.CallObjectMethod(jMethod, interopCache['Constructor.getParameterTypes'])
            JInteropObject.jni_check_errors()
            nParameterTypes = env.GetArrayLength(jParameterTypes)
            
            jnidesc = '('
            for iParamType in range(nParameterTypes):
                jParameterType = env.GetObjectArrayElement(jParameterTypes, iParamType)
                jnidesc += cls.jclass_to_jnidesc(jParameterType)
                env.DeleteLocalRef(jParameterType)
            jnidesc += ')V'
            env.DeleteLocalRef(jParameterTypes)
            env.DeleteLocalRef(jConstructor)
            
            value = cls._methods.get('<init>', None)
            
            if value is None:
                cls._methods['<init>'] = jnidesc
            elif isinstance(value, set):
                cls._methods['<init>'].add(jnidesc)
            else:
                cls._methods['<init>'] = {value, jnidesc}
                
            cls._methodsIDCache['<init>'+jnidesc] = (jReturnTypeJnidesc, env.GetMethodID(cls._clazz, b'<init>', jnidesc.encode('ascii')))
        
        env.DeleteLocalRef(jConstructors)
            
    @classmethod
    def jclass_to_jnidesc(cls, clazz: jclass) -> str:
        env = JInteropObject._ensureEnv()
        
        jName = env.CallObjectMethod(clazz, cls._interopMethodIDCache['Class.getName'])
        chars = env.GetStringChars(jName, NULL)
        name = chars.value
        env.ReleaseStringChars(jName, chars)
        env.DeleteLocalRef(jName)
        
        JInteropObject.jni_check_errors()
        
        jIsPrimitive = env.CallBooleanMethod(clazz, cls._interopMethodIDCache['Class.isPrimitive'])
        
        JInteropObject.jni_check_errors()
        
        if jIsPrimitive == JNI_TRUE:
            if name == 'boolean': return 'Z'
            if name == 'byte': return 'B'
            if name == 'char': return 'C'
            if name == 'short': return 'S'
            if name == 'int': return 'I'
            if name == 'long': return 'J'
            if name == 'float': return 'F'
            if name == 'double': return 'D'
            if name == 'void': return 'V'
        
        jIsArray = env.CallBooleanMethod(clazz, cls._interopMethodIDCache['Class.isArray'])
        
        JInteropObject.jni_check_errors()
        
        if jIsArray == JNI_TRUE:
            JInteropObject.jni_check_errors()
            return name.replace('.', '/')
        
        JInteropObject.jni_check_errors()
        
        return 'L' + name.replace('.', '/') + ';'
    
    @classmethod
    def normalize_L_jnidesc(cls, jnidesc: str) -> str:
        jnidesc = jnidesc.replace('.', '/')
        
        if jnidesc[0] == 'L':
            jnidesc = jnidesc[1:]
        
        if jnidesc[-1] == ';':
            jnidesc = jnidesc[:-1]
            
        return jnidesc
    
    @classmethod
    def parse_jnidesc_parameters(cls, jnidesc: str) -> list[IJniDescRepr]:
        jnidesc = jnidesc[1:]
        jnidesc = jnidesc.split(')')[0]
        
        resultReprs: list[IJniDescRepr] = []
        
        fTranslatingLclass = False
        fTranslatingArray = False
        nJnidesc = len(jnidesc)
        LclassBuffer = ''
        nArrayDepth = 0
        i = 0
        while i < nJnidesc:
            ch = jnidesc[i]
            if ch == ';':
                fTranslatingLclass = False
                if fTranslatingArray:
                    fTranslatingArray = False
                    descArrRepr = JNIDescLRepr(LclassBuffer)
                    for _ in range(nArrayDepth):
                        descArrRepr = JNIDescArrayRepr(descArrRepr)
                    resultReprs.append(descArrRepr)
                    nArrayDepth = 0
                else:
                    resultReprs.append(JNIDescLRepr(LclassBuffer))
                LclassBuffer = ''
            else:
                if fTranslatingLclass:
                    LclassBuffer += ch
                else:
                    if ch == 'L':
                        fTranslatingLclass = True
                    elif ch == '[':
                        fTranslatingArray = True
                        nArrayDepth += 1
                    else:
                        if fTranslatingArray:
                            fTranslatingArray = False
                            descArrRepr = JNIDescPrimitiveRepr(ch)
                            for _ in range(nArrayDepth):
                                descArrRepr = JNIDescArrayRepr(descArrRepr)
                            resultReprs.append(descArrRepr)
                            nArrayDepth = 0
                        else:
                            resultReprs.append(JNIDescPrimitiveRepr(ch))
            i += 1
            
        return resultReprs
    
    @classmethod
    def find_jni_class(cls, nativeName: str | bytes) -> jclass:
        env = JInteropObject._ensureEnv()
        env.ExceptionClear()
        if isinstance(nativeName, str):
            jniNativeName = nativeName.encode('ascii')
        else:
            jniNativeName = nativeName
        jStdClass = env.FindClass(jniNativeName)
        if jStdClass:
            return jStdClass
        if isinstance(nativeName, bytes):
            raise RuntimeError(f'Class "{nativeName}" not found in JNI, providen name in bytes (only JNI).')
        jClassName = env.NewString(nativeName, len(nativeName))
        jClass = env.FindClass('java/lang/Class')
        for classLoader in cls._classLoaders:
            clazz = env.CallStaticObjectMethod(
                jClass, JInteropObject._interopMethodIDCache['Class.forName'],
                jClassName, JNI_TRUE, classLoader, variadic=(jstring, jboolean, jobject))
            if env.ExceptionCheck():
                env.ExceptionClear()
                continue
            env.DeleteLocalRef(jClassName)
            env.DeleteLocalRef(jClass)
            return clazz
        env.DeleteLocalRef(jClassName)
        env.DeleteLocalRef(jClass)
        raise RuntimeError(f'Not found class {nativeName}.')