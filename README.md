### Complex Type Library and C++/COM/WinAPI Bridge

Contains many file definitions, WinAPI, COM, base NET/CoreCLR interaction, WinRT, inter-process and many-many more cool features. See the library source code for reference. Library is written in pure Python.

### Main library terms

1. IML - Instructions Markup Language, custom DSL standard for this library. 
Uses space-delimiter-based tokenization and instruction-centric model.
See `iml/imldef.py` for IML parser implementation.
2. ICL - Interface Contract Language, custom DSL for the definition of the COM interfaces and speedup the COM/Python declaring.
See `com/icl/wicl/parser.py` for parser implementation.
3. WICL - (Windows) Interface Contract Language, Generator/Parser implementation for the ICL standard.
See `com/icl/wicl/parser.py` for its implementation.
4. Intermediate Methods Process - the architecture of intermediate layer of Python delegator function and C++ declaration, Python must be call delegate method.
See `defbase.py` for reference (`foreign_optimized`, `foreign`, `delegate`, `CStructure.delegate`, `CStructure.virt_delegate`).
5. CIMPL - C Implementation Language, custom DSL for the definition of the JIT-compilable code, which lays between assembly and high-level definitions. Now is in development and not stable-to-work.
See `cimpl/cimpldef.py` and `cimpl/cimpljit.py` (under construction) for reference.
6. WET - Windows Event Tracing, custom tracing and logging system.
See `wet/trace.py` for reference.
7. WD - Win Debugger, custom debugger for debugging Python code with native calls, supports calling INT3 for entering native debugger (e.g. WinDbg).
8. COM TL - COM Template Library, the answer to Microsoft ATL, core module for COM utilities, COM object definitions and COM Servers API
9. NTL - .NET Template Library, library for hosting CLR, .NET Framework interop startup, utilities for interop.
10. JTL - Java Template Library, library for interacting JNI and interop startup.
11. WRPC - Win Remote Procedure Call, custom protocol for distributed objects system and remote procedure calling.
12. WinAbs - Win Abstractions Layer, abstractions over Win32 primitives for securely interacting with WinAPI and fastely developing on WinAPI on Python, destroying the Win32 API boilerplate code.

### Main files

1. `defbase.py`: core infrastructure and types definitions. first-to-see file.
2. `cpreproc.py`: core definition of the runtime preprocessor simulation.
3. `com/comdefbase.py`: core definition of the COM APIs.
4. `com/interfacedef.py`: core definition of the COM interface bases.
5. `defbase_process.py`: definitions for the CProcess class and inter-process communication.
6. `defbase_thread.py`: definitions for the CThread class and thread manipulations.
7. `defbase_module.py`: definitions for the CModule class and module manipulations.
8. `defbase_allocator.py`: core definitions of library Allocator APIs and IAllocator interface.
9. `defbase_assembly.py`: definition for the CAssembly class and machine code parsing.
10. `cimpl/cimpldef.py`: definitions for the core CIMPL infrastructure.
11. `iml/imldef.py`: definitions for the IML parser and its context.
12. `com/icl/wicl/parser.py`: definitions for the WICL - ICL Parser and its context.
13. `defbase_errordef.py`: definitions for the Windows error exceptions and exception text formatting.
14. `com/guid.py`: definitions for the GUID, IID and CLSID. 
15. `com/comtl`: COM Templates Library, the ATL analogue in library.
16. `com/bstr.py`: definition of the BSTR class.
17. `com/unknwn.py`: definition of the IUnknown, IClassFactory and COMClass classes and other core COM infrastructure logic.
18. `abs/core/handle.py`: core definitions for RAII-like handles for WinAbs
19. `abs/core/event.py`: core definition of WinAbs C#-like Event
20. `abs/window.py`: core window logic of WinAbs framework
21. `wrpc/message.py`: specification of WRPC protocol
22. `wrpc/marshal.py`: core marshal logic of WRPC
23. `wrpc/protocol.py`: main implementation of WRPC protocol
24. `net/interop.py`: .NET Framework Interop full implementation
25. `net/ntl.py` and `net/ntlext.py`: NTL and its extension
26. `net/ntlgen.py`: Python code generator from .NET assembly (part of NTL)
27. `java/interop.py`: Java Interop full implementation
28. `java/jtl.py`: Java Template Library
29. `winrt/winrtns.py`: definitions of WinRT namespaces, core import
30. `wet/trace.py`: implementation of WET - Windows Event Tracing
31. `dbg/wd.py`: implementation of WD - Win Debugger
32. `com/dispatch.py`: definition for OLE Automation wrapper
33. `com/icl/iclstorage`: main storage place for ICL files