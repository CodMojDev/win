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
15. `com/comtl.py`: COM Templates Library, the ATL analogue in library.
16. `com/bstr.py`: definition of the BSTR class.
17. `com/unknwn.py`: definition of the IUnknown, IClassFactory and COMClass classes and other core COM infrastructure logic.

### Philosophy & Architecture

You should be aware of all possible uses of this library, both successful and unsuccessful, and should not blame the library developer for your own carelessness.

All responsibility for the code lies with the developer. If my code is faulty, then it's my problem, but if it's caused by your incorrect interaction with the library, then it's your problem.

My library aims to bring the philosophy and architecture of C++ to Python and prove that Python can be a systems programming language.