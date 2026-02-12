"""
//
// corecrt_search.h
//
//      Copyright (c) Microsoft Corporation. All rights reserved.
//
// Declarations of functions for sorting and searching.  These declarations are
// split out so that they may be included by both <stdlib.h> and <search.h>.
// <stdlib.h> does not include <search.h> to avoid introducing conflicts with
// other user headers named <search.h>.
//
"""

from .corecrt import *

CoreCrtSecureSearchSortCompareFunction = CDECL(INT, LPVOID, LPCVOID, LPCVOID)
CoreCrtNonSecureSearchSortCompareFunction = CDECL(INT, LPCVOID, LPCVOID)

#bsearch_s = declare(ucrtbase.bsearch_s, LPVOID, LPCVOID, LPCVOID, rsize_t, rsize_t, CoreCrtSecureSearchSortCompareFunction, LPVOID)
#qsort_s = declare(ucrtbase.qsort_s, VOID, LPVOID, rsize_t, rsize_t, CoreCrtSecureSearchSortCompareFunction, LPVOID)

#bsearch = declare(ucrtbase.bsearch, LPVOID, LPCVOID, LPCVOID, rsize_t, rsize_t, CoreCrtNonSecureSearchSortCompareFunction)
#qsort = declare(ucrtbase.qsort, VOID, LPVOID, rsize_t, rsize_t, CoreCrtNonSecureSearchSortCompareFunction)
#lfind_s = declare(ucrtbase._lfind_s, LPVOID, LPCVOID, LPCVOID, PUINT, rsize_t, CoreCrtSecureSearchSortCompareFunction, LPVOID)
#lfind = declare(ucrtbase.lfind, LPVOID, LPCVOID, LPCVOID, PUINT, UINT, CoreCrtNonSecureSearchSortCompareFunction)
#lsearch = declare(ucrtbase.lsearch, LPVOID, LPCVOID, LPVOID, PUINT, UINT, CoreCrtNonSecureSearchSortCompareFunction)