"""
/********************************************************
*                                                       *
*   Copyright (C) Microsoft. All rights reserved.       *
*                                                       *
********************************************************/

//-----------------------------------------------------------------------------
//
// File:		adc.h
//
// Contents:	Adc external constants and GUIDS
//
// Comments:
//
//-----------------------------------------------------------------------------
"""

from . import cpreproc

from .guiddef import CLSID, GUID, IID

from .minwindef import INT

if cpreproc.pragma_once("ADC_INCLUDED"):
    # REGION *** Desktop Family ***
	
    CLSID_FoxRowset          = CLSID("{3ff292b6-b204-11cf-8d23-00aa005ffe58}")
    DBPROPSET_ADC            = GUID( "{b68e3cc1-6deb-11d0-8df6-00aa005ffe58}")
    IID_IAsyncAllowed        = GUID( "{f5f2893a-ba9e-11d0-abb9-00c04fc29f8f}")
    IID_IRowsetADCExtensions = IID(  "{f17324c4-68E0-11d0-ad45-00c04fc29863}")
    IID_IUpdateInfo          = IID(  "{a0385420-62b8-11d1-9a06-00a0c903aa45}")
    IID_IRowsetSynchronize   = IID(  "{1be41e60-807a-11d1-9a14-00a0c903aa45}")
    IID_IRowsetProperties    = IID(  "{1e837070-bcfc-11d1-9a2c-00a0c903aa45}")

    ADCPROPENUM = INT
    if True:
        DBPROP_ADC_ASYNCHFETCHSIZE = 3
        DBPROP_ADC_BATCHSIZE = 4
        DBPROP_ADC_UPDATECRITERIA = 5
        # dropping support for the UPDATEOPERTION property, but should not reuse the number
        #	  DBPROP_ADC_UPDATEOPERATION = 6
        DBPROP_ADC_ASYNCHPREFETCHSIZE = 7
        DBPROP_ADC_ASYNCHTHREADPRIORITY = 8
        DBPROP_ADC_CACHECHILDROWS = 9
        DBPROP_ADC_MAINTAINCHANGESTATUS = 10
        DBPROP_ADC_AUTORECALC = 11
        DBPROP_ADC_UNIQUETABLE = 13
        DBPROP_ADC_UNIQUESCHEMA = 14
        DBPROP_ADC_UNIQUECATALOG = 15
        DBPROP_ADC_CUSTOMRESYNCH = 16
        DBPROP_ADC_CEVER = 17
        DBPROP_ADC_RESHAPENAME = 18
        DBPROP_ADC_UPDATERESYNC = 19
        # removing SaveMode, but we should not reuse the number
        #	  DBPROP_ADC_SAVEMODE = 20
        DBPROP_ADC_BACKINGSTORE = 21
        DBPROP_ADC_RELEASESHAPEONDISCONNECT = 22

    # these enums are defined in both adc.h and adoint.h 
    # do not re define them here if adoint.h has already been included
    if cpreproc.pragma_once("_COMMON_ADC_AND_ADO_PROPS_"):
        ADCPROP_UPDATECRITERIA_ENUM = INT
        if True:
            adCriteriaKey = 0
            adCriteriaAllCols = 1
            adCriteriaUpdCols = 2
            adCriteriaTimeStamp = 3

        ADCPROP_ASYNCTHREADPRIORITY_ENUM = INT
        if True:
            adPriorityLowest = 1
            adPriorityBelowNormal = 2
            adPriorityNormal = 3
            adPriorityAboveNormal = 4
            adPriorityHighest = 5

        ADCPROP_UPDATERESYNC_ENUM = INT
        if True:
            adResyncNone = 0
            adResyncAutoIncrement = 0x1
            adResyncConflicts = 0x2
            adResyncUpdates = 0x4
            adResyncInserts = 0x8
            adResyncAll = 0x0F

        ADCPROP_AUTORECALC_ENUM = INT
        if True:
            adRecalcUpFront = 0
            adRecalcAlways = 1

    # _COMMON_ADC_AND_ADO_PROPS_
    FOXROWSETPROPENUM = INT
    if True:
        DBPROP_FOXTABLENAME = 0xeeff
    # REGION ***

# ADC_INCLUDED