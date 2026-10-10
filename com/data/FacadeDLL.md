FacadeDLL is compiled with Visual Studio 2022 (MSVC) Compiler and distributed as-is in its binary compiled file image as compilation process by end-user is not needed to preserve the portability and compatibility of the library.

The shared source of this DLL is published in this Markdown file.

`Facade.def`:
```
EXPORTS
    DllCanUnloadNow         PRIVATE
    DllGetClassObject       PRIVATE
    DllRegisterServer       PRIVATE
    DllUnregisterServer     PRIVATE
    DllInstall              PRIVATE
    DllGetActivationFactory PRIVATE
    InternalScriptNameAddr  PRIVATE
```
`Facade.cpp`:
```cpp
// C includes
#include <Windows.h>
#include <VersionHelpers.h>
#include <Python.h>

// C++ includes
#include <iostream>

typedef LPCWSTR(WINAPI *TWindowsGetStringRawBuffer)(PVOID string, UINT32* length);

CHAR ScriptName[128] = "TestFacade";
HINSTANCE g_hInstance = NULL;
HMODULE g_hModuleCombase = NULL;
PyObject* Script = NULL;

BOOL EnsurePythonInitialized()
{
    PyGILState_STATE gstate;
    std::wstring CPPCurrentDirectoryEXE;
    std::wstring CPPCurrentDirectory;
    WCHAR PrevDirectory[MAX_PATH];
    WCHAR CurrentDirectory[MAX_PATH];

    if (Py_IsInitialized() && Script) return TRUE;

    GetCurrentDirectory(MAX_PATH, PrevDirectory);
    GetModuleFileName(g_hInstance, CurrentDirectory, MAX_PATH);

    CPPCurrentDirectoryEXE = std::wstring(CurrentDirectory);
    CPPCurrentDirectory = CPPCurrentDirectoryEXE.substr(0,
        CPPCurrentDirectoryEXE.find_last_of(L'\\') + 1);

    SetCurrentDirectory(CPPCurrentDirectory.c_str());

    if (!Py_IsInitialized())
    {
        Py_Initialize();
    }

    if (!Py_IsInitialized())
    {
        SetCurrentDirectory(PrevDirectory);
        return FALSE;
    }

    gstate = PyGILState_Ensure();

    PyObject* sys = PyImport_ImportModule("sys");
    if (!sys) {
        PyErr_Print();
        return FALSE;
    }

    PyObject* sys_path = PyObject_GetAttrString(sys, "path");
    if (!sys_path) {
        PyErr_Print();
        Py_DECREF(sys);
        return FALSE;
    }

    PyObject* folder_path = PyUnicode_FromWideChar(L".", -1);
    if (!folder_path) {
        PyErr_Print();
        Py_DECREF(sys);
        Py_DECREF(sys_path);
        return FALSE;
    }

    if (PyList_Append(sys_path, folder_path) == -1) {
        PyErr_Print();
        return FALSE;
    }
    Py_DECREF(sys); Py_DECREF(sys_path); Py_DECREF(folder_path);

    Script = PyImport_ImportModule(ScriptName);

    if (!Script)
    {
        PyGILState_Release(gstate);
        SetCurrentDirectory(PrevDirectory);
        return FALSE;
    }

    PyGILState_Release(gstate);
    SetCurrentDirectory(PrevDirectory);

    return TRUE;
}

EXTERN_C_START
BOOL WINAPI DllMain(
    HINSTANCE hinstDLL,  // handle to DLL module
    DWORD fdwReason,     // reason for calling function
    LPVOID lpvReserved)  // reserved
{
    switch (fdwReason)
    {
    case DLL_PROCESS_ATTACH:
        g_hInstance = hinstDLL;
        if (IsWindows8OrGreater())
        {
            g_hModuleCombase = LoadLibraryW(L"combase.dll");
        }
        break;
    case DLL_PROCESS_DETACH:
        if (lpvReserved == NULL)
        {
            if (IsWindows8OrGreater())
            {
                FreeLibrary(g_hModuleCombase);
                g_hModuleCombase = NULL;
            }
            if (Py_IsInitialized())
            {
                if (Script)
                {
                    PyGILState_STATE gstate = PyGILState_Ensure();

                    Py_XDECREF(Script);
                    Script = NULL;

                    PyGILState_Release(gstate);
                }

                Py_Finalize();
            }
        }
        break;
    }
    return TRUE;
}

HRESULT WINAPI DllCanUnloadNow()
{
    if (!EnsurePythonInitialized())
    {
        return E_UNEXPECTED; // catastrophic failure
    }

    if (!Script) return E_UNEXPECTED;

    PyGILState_STATE gstate = PyGILState_Ensure();
    HRESULT hr = S_FALSE;

    PyObject* PyDllCanUnloadNow = PyObject_GetAttrString(Script, "I_DllCanUnloadNow");
    PyObject* HResult = NULL;

    if (!PyDllCanUnloadNow)
    {
        PyErr_Clear();
        goto cleanup;
    }

    HResult = PyObject_CallNoArgs(PyDllCanUnloadNow);
    Py_DECREF(PyDllCanUnloadNow);

    if (!HResult)
    {
        PyErr_Clear();
        goto cleanup;
    }

    hr = PyLong_AsLong(HResult);
    Py_DECREF(HResult);

cleanup:
    PyGILState_Release(gstate);
    return hr;
}

HRESULT WINAPI DllRegisterServer()
{
    if (!EnsurePythonInitialized())
    {
        return E_UNEXPECTED; // catastrophic failure
    }

    if (!Script) return E_UNEXPECTED;

    PyGILState_STATE gstate = PyGILState_Ensure();
    HRESULT hr = E_NOTIMPL;

    PyObject* PyDllRegisterServer  = PyObject_GetAttrString(Script, "I_DllRegisterServer");
    PyObject* HResult = NULL;

    if (!PyDllRegisterServer)
    {
        PyErr_Clear();
        goto cleanup;
    }

    HResult = PyObject_CallNoArgs(PyDllRegisterServer);
    Py_DECREF(PyDllRegisterServer);

    if (!HResult)
    {
        PyErr_Clear();
        hr = E_FAIL;
        goto cleanup;
    }

    hr = PyLong_AsLong(HResult);
    Py_DECREF(HResult);

cleanup:
    PyGILState_Release(gstate);
    return hr;
}

HRESULT WINAPI DllUnregisterServer()
{
    if (!EnsurePythonInitialized())
    {
        return E_UNEXPECTED; // catastrophic failure
    }

    if (!Script) return E_UNEXPECTED;

    PyGILState_STATE gstate = PyGILState_Ensure();
    HRESULT hr = E_NOTIMPL;

    PyObject* PyDllUnregisterServer = PyObject_GetAttrString(Script, "I_DllUnregisterServer");
    PyObject* HResult = NULL;

    if (!PyDllUnregisterServer)
    {
        PyErr_Clear();
        goto cleanup;
    }


    HResult = PyObject_CallNoArgs(PyDllUnregisterServer);
    Py_DECREF(PyDllUnregisterServer);

    if (!HResult)
    {
        PyErr_Clear();
        hr = E_FAIL;
        goto cleanup;
    }

    hr = PyLong_AsLong(HResult);
    Py_DECREF(HResult);

cleanup:
    PyGILState_Release(gstate);
    return hr;
}

HRESULT WINAPI DllInstall(BOOL bInstall, PCWSTR pszCmdLine)
{
    if (!EnsurePythonInitialized())
    {
        return E_UNEXPECTED; // catastrophic failure
    }

    if (!Script) return E_UNEXPECTED;

    PyGILState_STATE gstate = PyGILState_Ensure();
    HRESULT hr = E_NOTIMPL;

    PyObject* Py_DllInstall = PyObject_GetAttrString(Script, "I_DllInstall");
    PyObject* PyBool_bInstall = NULL;
    PyObject* PyLong_pszCmdLine = NULL;
    PyObject* HResult = NULL;
    PyObject* Args = NULL;

    if (!Py_DllInstall)
    {
        PyErr_Clear();
        goto cleanup;
    }

    hr = E_FAIL;

    PyBool_bInstall = PyBool_FromLong(bInstall);
    PyLong_pszCmdLine = PyLong_FromVoidPtr((void*)pszCmdLine);

    if (!(PyBool_bInstall && PyLong_pszCmdLine))
    {
        Py_XDECREF(PyBool_bInstall);
        Py_XDECREF(PyLong_pszCmdLine);
        Py_DECREF(Py_DllInstall);

        PyErr_Clear();
        goto cleanup;
    }

    Args = PyTuple_Pack(2, PyBool_bInstall, PyLong_pszCmdLine);
    Py_DECREF(PyBool_bInstall);
    Py_DECREF(PyLong_pszCmdLine);
    
    if (!Args)
    {
        Py_DECREF(Py_DllInstall);

        PyErr_Clear();
        goto cleanup;
    }

    HResult = PyObject_Call(Py_DllInstall, Args, NULL);
    Py_DECREF(Py_DllInstall);

    if (!HResult)
    {
        PyErr_Clear();
        goto cleanup;
    }

    hr = PyLong_AsLong(HResult);
    Py_DECREF(HResult);

cleanup:
    PyGILState_Release(gstate);
    return hr;
}

HRESULT WINAPI DllGetClassObject(
    REFCLSID rclsid,
    REFIID   riid,
    LPVOID* ppv
)
{
    if (!EnsurePythonInitialized())
    {
        return E_UNEXPECTED; // catastrophic failure
    }

    if (!Script) return E_UNEXPECTED;

    if (!&rclsid) return E_POINTER;
    if (!&riid) return E_POINTER;
    if (!ppv) return E_POINTER;

    PyGILState_STATE gstate = PyGILState_Ensure();
    HRESULT hr = E_NOTIMPL;

    PyObject* PyDllGetClassObject = PyObject_GetAttrString(Script, "I_DllGetClassObject");

    PyObject* PyLong_rclsid = NULL;
    PyObject* PyLong_riid = NULL;
    PyObject* PyLong_ppv = NULL;
    PyObject* Args = NULL;
    PyObject* HResult = NULL;

    if (!PyDllGetClassObject)
    {
        PyErr_Clear();
        goto cleanup;
    }

    hr = E_FAIL;

    PyLong_rclsid = PyLong_FromVoidPtr((void*)&rclsid);
    PyLong_riid = PyLong_FromVoidPtr((void*)&riid);
    PyLong_ppv = PyLong_FromVoidPtr(ppv);

    if (!(PyLong_rclsid && PyLong_riid && PyLong_ppv))
    {
        Py_XDECREF(PyLong_rclsid);
        Py_XDECREF(PyLong_riid);
        Py_XDECREF(PyLong_ppv);
        Py_DECREF(PyDllGetClassObject);
        PyErr_Clear();
        goto cleanup;
    }

    Args = PyTuple_Pack(3, PyLong_rclsid, PyLong_riid, PyLong_ppv);

    Py_DECREF(PyLong_rclsid);
    Py_DECREF(PyLong_riid);
    Py_DECREF(PyLong_ppv);

    if (!Args)
    {
        Py_DECREF(PyDllGetClassObject);
        PyErr_Clear();
        goto cleanup;
    }

    HResult = PyObject_Call(PyDllGetClassObject, Args, NULL);
    Py_DECREF(PyDllGetClassObject);
    Py_DECREF(Args);
    
    if (!HResult)
    {
        PyErr_Clear();
        goto cleanup;
    }

    hr = PyLong_AsLong(HResult);
    Py_DECREF(HResult);

cleanup:
    PyGILState_Release(gstate);
    return hr;
}

HRESULT WINAPI DllGetActivationFactory(PVOID activatableClassId, PVOID ppFactory)
{
    if (!IsWindows8OrGreater())
    {
        return E_NOTIMPL;
    }
    if (!EnsurePythonInitialized())
    {
        return E_UNEXPECTED;
    }
    TWindowsGetStringRawBuffer WindowsGetStringRawBuffer = (TWindowsGetStringRawBuffer)GetProcAddress(g_hModuleCombase, "WindowsGetStringRawBuffer");
    if (!WindowsGetStringRawBuffer)
    {
        return E_UNEXPECTED;
    }

    if (!Script) return E_UNEXPECTED;
    if (!ppFactory) return E_POINTER;
    if (!activatableClassId) return E_INVALIDARG;

    PyGILState_STATE gstate = PyGILState_Ensure();
    HRESULT hr = E_NOTIMPL;

    PyObject* PyDllGetActivationFactory = PyObject_GetAttrString(Script, "I_DllGetActivationFactory");
    PyObject* HResult = NULL;
    LPCWSTR lpszActivatableClsID = NULL;
    PyObject* PyActivatableClsID = NULL;
    PyObject* PyFactoryPpv = NULL;
    PyObject* Args = NULL;

    if (!PyDllGetActivationFactory)
    {
        PyErr_Clear();
        goto cleanup;
    }

    UINT32 uActivatableClsIDLength;
    lpszActivatableClsID = WindowsGetStringRawBuffer(activatableClassId, &uActivatableClsIDLength);
    if (!lpszActivatableClsID)
    {
        Py_DECREF(PyDllGetActivationFactory);
        hr = E_INVALIDARG;
        goto cleanup;
    }

    hr = E_FAIL;

    PyActivatableClsID = PyUnicode_FromWideChar(lpszActivatableClsID, uActivatableClsIDLength);
    PyFactoryPpv = PyLong_FromVoidPtr(ppFactory);
    if (!(PyActivatableClsID && PyFactoryPpv))
    {
        Py_XDECREF(PyActivatableClsID);
        Py_XDECREF(PyFactoryPpv);
        Py_DECREF(PyDllGetActivationFactory);
        PyErr_Clear();
        goto cleanup;
    }

    Args = PyTuple_Pack(2, PyActivatableClsID, PyFactoryPpv);

    Py_DECREF(PyActivatableClsID);
    Py_DECREF(PyFactoryPpv);

    if (!Args)
    {
        Py_DECREF(PyDllGetActivationFactory);
        PyErr_Clear();
        goto cleanup;
    }

    HResult = PyObject_Call(PyDllGetActivationFactory, Args, NULL);
    Py_DECREF(PyDllGetActivationFactory);
    Py_DECREF(Args);

    if (!HResult)
    {
        PyErr_Clear();
        goto cleanup;
    }

    hr = PyLong_AsLong(HResult);
    Py_DECREF(HResult);

cleanup:
    PyGILState_Release(gstate);
    return hr;
}

PVOID InternalScriptNameAddr()
{
    return &ScriptName;
}

EXTERN_C_END
```