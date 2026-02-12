from . import cpreproc

from .minwindef import *

from .winnt import (GUID, NULL, PWSTR, 
                    PZZWSTR, PCZZWSTR, PCNZCH,
                    PULONGLONG, ULONGLONG,
                    PSYSTEMTIME)

from .defbase import *

import sys

from typing import (Callable)

if cpreproc.ifndef("NOAPISET"):
    from .libloaderapi import *
if cpreproc.ifndef("NONLS"):
    
    kernel32 = W_WinDLL("kernel32.dll")
    kernelbase = W_WinDLL("kernelbase.dll")

    # REGION *** Application Family or OneCore or Games Family ***

	######################################
	#
	#  Constants
	#
	#  Define all constants for the NLS component here.
	#
	######################################
	#
	#  String Length Maximums.
	#
    MAX_LEADBYTES = 12 # 5 ranges, 2 bytes ea., 0 term.
    MAX_DEFAULTCHAR = 2 # single or double byte
	#
	#  Surrogate pairs
	#
	#  Conversion examples:
	#
	#  A) The first character in the Surrogate range (D800, DC00) as UTF-32:
	#
	#  1.  D800: binary 1101100000000000  (lower ten bits: 0000000000)
	#  2.  DC00: binary 1101110000000000  (lower ten bits: 0000000000)
	#  3.  Concatenate 0000000000+0000000000 = 0x0000
	#  4.  Add 0x10000
	#
	#  Result: U+10000. This is correct, since the first character in the Supplementary character
	#  range immediately follows the last code point in the 16-bit UTF-16 range (U+FFFF)
	#
	#  B) A UTF-32 code point such as U+2040A (this a CJK character in CJK Extension B), and wish
	#  to convert it in UTF-16:
	#
	#  1.  Subtract 0x10000 - Result: 0x1040A
	#  2.  Split into two ten-bit pieces: 0001000001 0000001010
	#  3.  Add 1101100000000000 (0xD800) to the high 10 bits piece (0001000001) - Result: 1101100001000001 (0xD841)
	#  4.  Add 1101110000000000 (0xDC00) to the low 10 bits piece (0000001010) - Result: 1101110000001010 (0xDC0A)
	#
	#  RESULT: The surrogate pair: U+D841, U+DC0A
	#
	#  Special Unicode code point values, for use with UTF-16 surrogate pairs.
	#
    HIGH_SURROGATE_START = 0xd800
    HIGH_SURROGATE_END = 0xdbff
    LOW_SURROGATE_START = 0xdc00
    LOW_SURROGATE_END = 0xdfff
	#
	#  MBCS and Unicode Translation Flags.
	#  Please use Unicode, either UTF-16 (WCHAR) or UTF-8 (CP_UTF8)
	#
	# MB_PRECOMPOSED and MB_COMPOSITE are deprecated, not recommended, and
	# provide out-of-date behavior.
	# Windows typically uses Unicode Normalization Form C type sequences,
	# If explicit normalization forms are required, please use NormalizeString.
    MB_PRECOMPOSED = 0x00000001 # DEPRECATED: use single precomposed characters when possible.
    MB_COMPOSITE = 0x00000002 # DEPRECATED: use multiple discrete characters when possible.
    MB_USEGLYPHCHARS = 0x00000004 # DEPRECATED: use glyph chars, not ctrl chars
    MB_ERR_INVALID_CHARS = 0x00000008 # error for invalid chars
	# WC_COMPOSITECHECK, WC_DISCARDNS and WC_SEPCHARS are deprecated, not recommended,
	# and provide out-of-date behavior.
	# Windows typically uses Unicode Normalization Form C type sequences,
	# If explicit normalization forms are required, please use NormalizeString.
    WC_COMPOSITECHECK = 0x00000200 # convert composite to precomposed
    WC_DISCARDNS = 0x00000010 # discard non-spacing chars          # Used with WC_COMPOSITECHECK
    WC_SEPCHARS = 0x00000020 # generate separate chars            # Used with WC_COMPOSITECHECK
    WC_DEFAULTCHAR = 0x00000040 # replace w/ default char            # Used with WC_COMPOSITECHECK
    WC_ERR_INVALID_CHARS = 0x00000080 # error for invalid chars
    WC_NO_BEST_FIT_CHARS = 0x00000400 # do not use best fit chars
	#
	#  Character Type Flags.
	#
    CT_CTYPE1 = 0x00000001 # ctype 1 information
    CT_CTYPE2 = 0x00000002 # ctype 2 information
    CT_CTYPE3 = 0x00000004 # ctype 3 information
	#
	#  CType 1 Flag Bits.
	#
    C1_UPPER = 0x0001 # upper case
    C1_LOWER = 0x0002 # lower case
    C1_DIGIT = 0x0004 # decimal digits
    C1_SPACE = 0x0008 # spacing characters
    C1_PUNCT = 0x0010 # punctuation characters
    C1_CNTRL = 0x0020 # control characters
    C1_BLANK = 0x0040 # blank characters
    C1_XDIGIT = 0x0080 # other digits
    C1_ALPHA = 0x0100 # any linguistic character
    C1_DEFINED = 0x0200 # defined character
	#
	#  CType 2 Flag Bits.
	#
    C2_LEFTTORIGHT = 0x0001 # left to right
    C2_RIGHTTOLEFT = 0x0002 # right to left
    C2_EUROPENUMBER = 0x0003 # European number, digit
    C2_EUROPESEPARATOR = 0x0004 # European numeric separator
    C2_EUROPETERMINATOR = 0x0005 # European numeric terminator
    C2_ARABICNUMBER = 0x0006 # Arabic number
    C2_COMMONSEPARATOR = 0x0007 # common numeric separator
    C2_BLOCKSEPARATOR = 0x0008 # block separator
    C2_SEGMENTSEPARATOR = 0x0009 # segment separator
    C2_WHITESPACE = 0x000A # white space
    C2_OTHERNEUTRAL = 0x000B # other neutrals
    C2_NOTAPPLICABLE = 0x0000 # no implicit directionality
	#
	#  CType 3 Flag Bits.
	#
    C3_NONSPACING = 0x0001 # nonspacing character
    C3_DIACRITIC = 0x0002 # diacritic mark
    C3_VOWELMARK = 0x0004 # vowel mark
    C3_SYMBOL = 0x0008 # symbols
    C3_KATAKANA = 0x0010 # katakana character
    C3_HIRAGANA = 0x0020 # hiragana character
    C3_HALFWIDTH = 0x0040 # half width character
    C3_FULLWIDTH = 0x0080 # full width character
    C3_IDEOGRAPH = 0x0100 # ideographic character
    C3_KASHIDA = 0x0200 # Arabic kashida character
    C3_LEXICAL = 0x0400 # lexical character
    C3_HIGHSURROGATE = 0x0800 # high surrogate code unit
    C3_LOWSURROGATE = 0x1000 # low surrogate code unit
    C3_ALPHA = 0x8000 # any linguistic char (C1_ALPHA)
    C3_NOTAPPLICABLE = 0x0000 # ctype 3 is not applicable
	#
	#  String Flags.
	#
    NORM_IGNORECASE = 0x00000001 # ignore case
    NORM_IGNORENONSPACE = 0x00000002 # ignore nonspacing chars
    NORM_IGNORESYMBOLS = 0x00000004 # ignore symbols
    LINGUISTIC_IGNORECASE = 0x00000010 # linguistically appropriate 'ignore case'
    LINGUISTIC_IGNOREDIACRITIC = 0x00000020 # linguistically appropriate 'ignore nonspace'
    NORM_IGNOREKANATYPE = 0x00010000 # ignore kanatype
    NORM_IGNOREWIDTH = 0x00020000 # ignore width
    NORM_LINGUISTIC_CASING = 0x08000000 # use linguistic rules for casing
	#
	#  Locale Independent Mapping Flags.
	#
    MAP_FOLDCZONE = 0x00000010 # fold compatibility zone chars
    MAP_PRECOMPOSED = 0x00000020 # convert to precomposed chars
    MAP_COMPOSITE = 0x00000040 # convert to composite chars
    MAP_FOLDDIGITS = 0x00000080 # all digits to ASCII 0-9
    MAP_EXPAND_LIGATURES = 0x00002000 # expand all ligatures
	#
	#  Locale Dependent Mapping Flags.
	#
    LCMAP_LOWERCASE = 0x00000100 # lower case letters
    LCMAP_UPPERCASE = 0x00000200 # UPPER CASE LETTERS
    LCMAP_TITLECASE = 0x00000300 # Title Case Letters
    LCMAP_SORTKEY = 0x00000400 # WC sort key (normalize)
    LCMAP_BYTEREV = 0x00000800 # byte reversal
    LCMAP_HIRAGANA = 0x00100000 # map katakana to hiragana
    LCMAP_KATAKANA = 0x00200000 # map hiragana to katakana
    LCMAP_HALFWIDTH = 0x00400000 # map double byte to single byte
    LCMAP_FULLWIDTH = 0x00800000 # map single byte to double byte
    LCMAP_LINGUISTIC_CASING = 0x01000000 # use linguistic rules for casing
    LCMAP_SIMPLIFIED_CHINESE = 0x02000000 # map traditional chinese to simplified chinese
    LCMAP_TRADITIONAL_CHINESE = 0x04000000 # map simplified chinese to traditional chinese
    LCMAP_SORTHANDLE = 0x20000000
    LCMAP_HASH = 0x00040000
	#
	#  Search Flags
	#
    FIND_STARTSWITH = 0x00100000 # see if value is at the beginning of source
    FIND_ENDSWITH = 0x00200000 # see if value is at the end of source
    FIND_FROMSTART = 0x00400000 # look for value in source, starting at the beginning
    FIND_FROMEND = 0x00800000 # look for value in source, starting at the end
	#
	# ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
	#
	# Language Group Enumeration Flags.
	#
	# The "Language Group" concept is an obsolete concept.
	# The groups returned are not well defined, arbitrary, inconsistent, inaccurate,
	# no longer maintained, and no longer supported.
	#
	# ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
	#
    LGRPID_INSTALLED = 0x00000001 # installed language group ids
    LGRPID_SUPPORTED = 0x00000002 # supported language group ids
	#
	#  Locale Enumeration Flags.
	#
    LCID_INSTALLED = 0x00000001 # installed locale ids
    LCID_SUPPORTED = 0x00000002 # supported locale ids
    LCID_ALTERNATE_SORTS = 0x00000004 # alternate sort locale ids
	#
	#  Named based enumeration flags.
	#
    LOCALE_ALL = 0 # enumerate all named based locales
    LOCALE_WINDOWS = 0x00000001 # shipped locales and/or replacements for them
    LOCALE_SUPPLEMENTAL = 0x00000002 # supplemental locales only
    LOCALE_ALTERNATE_SORTS = 0x00000004 # alternate sort locales
    LOCALE_REPLACEMENT = 0x00000008 # locales that replace shipped locales (callback flag only)
    LOCALE_NEUTRALDATA = 0x00000010 # Locales that are "neutral" (language only, region data is default)
    LOCALE_SPECIFICDATA = 0x00000020 # Locales that contain language and region data
	#
	#  Code Page Enumeration Flags.
	#
    CP_INSTALLED = 0x00000001 # installed code page ids
    CP_SUPPORTED = 0x00000002 # supported code page ids
	#
	#  Sorting Flags.
	#
	#    WORD Sort:    culturally correct sort
	#                  hyphen and apostrophe are special cased
	#                  example: "coop" and "co-op" will sort together in a list
	#
	#                        co_op     <-------  underscore (symbol)
	#                        coat
	#                        comb
	#                        coop
	#                        co-op     <-------  hyphen (punctuation)
	#                        cork
	#                        went
	#                        were
	#                        we're     <-------  apostrophe (punctuation)
	#
	#
	#    STRING Sort:  hyphen and apostrophe will sort with all other symbols
	#
	#                        co-op     <-------  hyphen (punctuation)
	#                        co_op     <-------  underscore (symbol)
	#                        coat
	#                        comb
	#                        coop
	#                        cork
	#                        we're     <-------  apostrophe (punctuation)
	#                        went
	#                        were
	#
    SORT_STRINGSORT = 0x00001000 # use string sort method
	#  Sort digits as numbers (ie: 2 comes before 10)
    SORT_DIGITSASNUMBERS = 0x00000008 # use digits as numbers sort method
	#
	#  Compare String Return Values.
	#
    CSTR_LESS_THAN = 1 # string 1 less than string 2
    CSTR_EQUAL = 2 # string 1 equal to string 2
    CSTR_GREATER_THAN = 3 # string 1 greater than string 2
	#
	#  Code Page Default Values.
	#  Please Use Unicode, either UTF-16 (as in WCHAR) or UTF-8 (code page CP_ACP)
	#
    CP_ACP = 0 # default to ANSI code page
    CP_OEMCP = 1 # default to OEM  code page
    CP_MACCP = 2 # default to MAC  code page
    CP_THREAD_ACP = 3 # current thread's ANSI code page
    CP_SYMBOL = 42 # SYMBOL translations
    CP_UTF7 = 65000 # UTF-7 translation
    CP_UTF8 = 65001 # UTF-8 translation
	#
	# ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
	#
	#  Country/Region Codes.
	#
	#  DEPRECATED: The GEOID  concept is deprecated, please use
	#  Country/Region Names instead, eg: "US" instead of a GEOID like 244.
	#  See the documentation for GetGeoInfoEx.
	#
	#  WARNING: These values are arbitrarily assigned values, please use
	#           standard country/region names instead, such as "US".
	#
	# ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
	#
    CTRY_DEFAULT = 0
    CTRY_ALBANIA = 355 # Albania
    CTRY_ALGERIA = 213 # Algeria
    CTRY_ARGENTINA = 54 # Argentina
    CTRY_ARMENIA = 374 # Armenia
    CTRY_AUSTRALIA = 61 # Australia
    CTRY_AUSTRIA = 43 # Austria
    CTRY_AZERBAIJAN = 994 # Azerbaijan
    CTRY_BAHRAIN = 973 # Bahrain
    CTRY_BELARUS = 375 # Belarus
    CTRY_BELGIUM = 32 # Belgium
    CTRY_BELIZE = 501 # Belize
    CTRY_BOLIVIA = 591 # Bolivia
    CTRY_BRAZIL = 55 # Brazil
    CTRY_BRUNEI_DARUSSALAM = 673 # Brunei Darussalam
    CTRY_BULGARIA = 359 # Bulgaria
    CTRY_CANADA = 2 # Canada
    CTRY_CARIBBEAN = 1 # Caribbean
    CTRY_CHILE = 56 # Chile
    CTRY_COLOMBIA = 57 # Colombia
    CTRY_COSTA_RICA = 506 # Costa Rica
    CTRY_CROATIA = 385 # Croatia
    CTRY_CZECH = 420 # Czech Republic
    CTRY_DENMARK = 45 # Denmark
    CTRY_DOMINICAN_REPUBLIC = 1 # Dominican Republic
    CTRY_ECUADOR = 593 # Ecuador
    CTRY_EGYPT = 20 # Egypt
    CTRY_EL_SALVADOR = 503 # El Salvador
    CTRY_ESTONIA = 372 # Estonia
    CTRY_FAEROE_ISLANDS = 298 # Faeroe Islands
    CTRY_FINLAND = 358 # Finland
    CTRY_FRANCE = 33 # France
    CTRY_GEORGIA = 995 # Georgia
    CTRY_GERMANY = 49 # Germany
    CTRY_GREECE = 30 # Greece
    CTRY_GUATEMALA = 502 # Guatemala
    CTRY_HONDURAS = 504 # Honduras
    CTRY_HONG_KONG = 852 # Hong Kong S.A.R., P.R.C.
    CTRY_HUNGARY = 36 # Hungary
    CTRY_ICELAND = 354 # Iceland
    CTRY_INDIA = 91 # India
    CTRY_INDONESIA = 62 # Indonesia
    CTRY_IRAN = 981 # Iran
    CTRY_IRAQ = 964 # Iraq
    CTRY_IRELAND = 353 # Ireland
    CTRY_ISRAEL = 972 # Israel
    CTRY_ITALY = 39 # Italy
    CTRY_JAMAICA = 1 # Jamaica
    CTRY_JAPAN = 81 # Japan
    CTRY_JORDAN = 962 # Jordan
    CTRY_KAZAKSTAN = 7 # Kazakstan
    CTRY_KENYA = 254 # Kenya
    CTRY_KUWAIT = 965 # Kuwait
    CTRY_KYRGYZSTAN = 996 # Kyrgyzstan
    CTRY_LATVIA = 371 # Latvia
    CTRY_LEBANON = 961 # Lebanon
    CTRY_LIBYA = 218 # Libya
    CTRY_LIECHTENSTEIN = 41 # Liechtenstein
    CTRY_LITHUANIA = 370 # Lithuania
    CTRY_LUXEMBOURG = 352 # Luxembourg
    CTRY_MACAU = 853 # Macao SAR, PRC
    CTRY_MACEDONIA = 389 # Former Yugoslav Republic of Macedonia
    CTRY_MALAYSIA = 60 # Malaysia
    CTRY_MALDIVES = 960 # Maldives
    CTRY_MEXICO = 52 # Mexico
    CTRY_MONACO = 33 # Principality of Monaco
    CTRY_MONGOLIA = 976 # Mongolia
    CTRY_MOROCCO = 212 # Morocco
    CTRY_NETHERLANDS = 31 # Netherlands
    CTRY_NEW_ZEALAND = 64 # New Zealand
    CTRY_NICARAGUA = 505 # Nicaragua
    CTRY_NORWAY = 47 # Norway
    CTRY_OMAN = 968 # Oman
    CTRY_PAKISTAN = 92 # Islamic Republic of Pakistan
    CTRY_PANAMA = 507 # Panama
    CTRY_PARAGUAY = 595 # Paraguay
    CTRY_PERU = 51 # Peru
    CTRY_PHILIPPINES = 63 # Republic of the Philippines
    CTRY_POLAND = 48 # Poland
    CTRY_PORTUGAL = 351 # Portugal
    CTRY_PRCHINA = 86 # People's Republic of China
    CTRY_PUERTO_RICO = 1 # Puerto Rico
    CTRY_QATAR = 974 # Qatar
    CTRY_ROMANIA = 40 # Romania
    CTRY_RUSSIA = 7 # Russia
    CTRY_SAUDI_ARABIA = 966 # Saudi Arabia
    CTRY_SERBIA = 381 # Serbia
    CTRY_SINGAPORE = 65 # Singapore
    CTRY_SLOVAK = 421 # Slovak Republic
    CTRY_SLOVENIA = 386 # Slovenia
    CTRY_SOUTH_AFRICA = 27 # South Africa
    CTRY_SOUTH_KOREA = 82 # Korea
    CTRY_SPAIN = 34 # Spain
    CTRY_SWEDEN = 46 # Sweden
    CTRY_SWITZERLAND = 41 # Switzerland
    CTRY_SYRIA = 963 # Syria
    CTRY_TAIWAN = 886 # Taiwan
    CTRY_TATARSTAN = 7 # Tatarstan
    CTRY_THAILAND = 66 # Thailand
    CTRY_TRINIDAD_Y_TOBAGO = 1 # Trinidad y Tobago
    CTRY_TUNISIA = 216 # Tunisia
    CTRY_TURKEY = 90 # Turkey
    CTRY_UAE = 971 # U.A.E.
    CTRY_UKRAINE = 380 # Ukraine
    CTRY_UNITED_KINGDOM = 44 # United Kingdom
    CTRY_UNITED_STATES = 1 # United States
    CTRY_URUGUAY = 598 # Uruguay
    CTRY_UZBEKISTAN = 7 # Uzbekistan
    CTRY_VENEZUELA = 58 # Venezuela
    CTRY_VIET_NAM = 84 # Viet Nam
    CTRY_YEMEN = 967 # Yemen
    CTRY_ZIMBABWE = 263 # Zimbabwe
	#
	#  Locale Types.
	#
	#  These types are used for the GetLocaleInfo NLS API routine.
	#  Some of these types are also used for the SetLocaleInfo NLS API routine.
	#
	#
	#  The following LCTypes may be used in combination with any other LCTypes.
	#
	#    LOCALE_NOUSEROVERRIDE is also used in GetTimeFormat and
	#    GetDateFormat.
	#
	#    LOCALE_RETURN_NUMBER will return the result from GetLocaleInfo as a
	#    number instead of a string.  This flag is only valid for the LCTypes
	#    beginning with LOCALE_I.
	#
	#    DEPRECATED: LOCALE_USE_CP_ACP is used in many of the A (Ansi) apis that need
	#                to do string translation.  Callers are encouraged to use the W
	#                (WCHAR/Unicode) apis instead.
	#
    LOCALE_NOUSEROVERRIDE = 0x80000000 # Not Recommended - do not use user overrides
    LOCALE_USE_CP_ACP = 0x40000000 # DEPRECATED, call Unicode APIs instead: use the system ACP
    LOCALE_RETURN_NUMBER = 0x20000000 # return number instead of string
    LOCALE_RETURN_GENITIVE_NAMES = 0x10000000 #Flag to return the Genitive forms of month names
    LOCALE_ALLOW_NEUTRAL_NAMES = 0x08000000 #Flag to allow returning neutral names/lcids for name conversion
	#
	#  The following LCTypes are mutually exclusive in that they may NOT
	#  be used in combination with each other.
	#
	#
	# These are the various forms of the name of the locale:
	#
    LOCALE_SLOCALIZEDDISPLAYNAME = 0x00000002 # localized name of locale, eg "German (Germany)" in UI language
    LOCALE_SENGLISHDISPLAYNAME = 0x00000072 # Display name (language + country/region usually) in English, eg "German (Germany)"
    LOCALE_SNATIVEDISPLAYNAME = 0x00000073 # Display name in native locale language, eg "Deutsch (Deutschland)
    LOCALE_SLOCALIZEDLANGUAGENAME = 0x0000006f # Language Display Name for a language, eg "German" in UI language
    LOCALE_SENGLISHLANGUAGENAME = 0x00001001 # English name of language, eg "German"
    LOCALE_SNATIVELANGUAGENAME = 0x00000004 # native name of language, eg "Deutsch"
    LOCALE_SLOCALIZEDCOUNTRYNAME = 0x00000006 # localized name of country/region, eg "Germany" in UI language
    LOCALE_SENGLISHCOUNTRYNAME = 0x00001002 # English name of country/region, eg "Germany"
    LOCALE_SNATIVECOUNTRYNAME = 0x00000008 # native name of country/region, eg "Deutschland"
	# Additional LCTypes
    LOCALE_IDIALINGCODE = 0x00000005 # country/region dialing code, example: en-US and en-CA return 1.
    LOCALE_SLIST = 0x0000000C # list item separator, eg "," for "1,2,3,4"
    LOCALE_IMEASURE = 0x0000000D # 0 = metric, 1 = US measurement system
    LOCALE_SDECIMAL = 0x0000000E # decimal separator, eg "." for 1,234.00
    LOCALE_STHOUSAND = 0x0000000F # thousand separator, eg "," for 1,234.00
    LOCALE_SGROUPING = 0x00000010 # digit grouping, eg "3;0" for 1,000,000
    LOCALE_IDIGITS = 0x00000011 # number of fractional digits eg 2 for 1.00
    LOCALE_ILZERO = 0x00000012 # leading zeros for decimal, 0 for .97, 1 for 0.97
    LOCALE_INEGNUMBER = 0x00001010 # negative number mode, 0-4, see documentation
    LOCALE_SNATIVEDIGITS = 0x00000013 # native digits for 0-9, eg "0123456789"
    LOCALE_SCURRENCY = 0x00000014 # local monetary symbol, eg "$"
    LOCALE_SINTLSYMBOL = 0x00000015 # intl monetary symbol, eg "USD"
    LOCALE_SMONDECIMALSEP = 0x00000016 # monetary decimal separator, eg "." for $1,234.00
    LOCALE_SMONTHOUSANDSEP = 0x00000017 # monetary thousand separator, eg "," for $1,234.00
    LOCALE_SMONGROUPING = 0x00000018 # monetary grouping, eg "3;0" for $1,000,000.00
    LOCALE_ICURRDIGITS = 0x00000019 # # local monetary digits, eg 2 for $1.00
    LOCALE_ICURRENCY = 0x0000001B # positive currency mode, 0-3, see documentation
    LOCALE_INEGCURR = 0x0000001C # negative currency mode, 0-15, see documentation
    LOCALE_SSHORTDATE = 0x0000001F # short date format string, eg "MM/dd/yyyy"
    LOCALE_SLONGDATE = 0x00000020 # long date format string, eg "dddd, MMMM dd, yyyy"
    LOCALE_STIMEFORMAT = 0x00001003 # time format string, eg "HH:mm:ss"
    LOCALE_SAM = 0x00000028 # AM designator, eg "AM"
    LOCALE_SPM = 0x00000029 # PM designator, eg "PM"
    LOCALE_ICALENDARTYPE = 0x00001009 # type of calendar specifier, eg CAL_GREGORIAN
    LOCALE_IOPTIONALCALENDAR = 0x0000100B # additional calendar types specifier, eg CAL_GREGORIAN_US
    LOCALE_IFIRSTDAYOFWEEK = 0x0000100C # first day of week specifier, 0-6, 0=Monday, 6=Sunday
    LOCALE_IFIRSTWEEKOFYEAR = 0x0000100D # first week of year specifier, 0-2, see documentation
    LOCALE_SDAYNAME1 = 0x0000002A # long name for Monday
    LOCALE_SDAYNAME2 = 0x0000002B # long name for Tuesday
    LOCALE_SDAYNAME3 = 0x0000002C # long name for Wednesday
    LOCALE_SDAYNAME4 = 0x0000002D # long name for Thursday
    LOCALE_SDAYNAME5 = 0x0000002E # long name for Friday
    LOCALE_SDAYNAME6 = 0x0000002F # long name for Saturday
    LOCALE_SDAYNAME7 = 0x00000030 # long name for Sunday
    LOCALE_SABBREVDAYNAME1 = 0x00000031 # abbreviated name for Monday
    LOCALE_SABBREVDAYNAME2 = 0x00000032 # abbreviated name for Tuesday
    LOCALE_SABBREVDAYNAME3 = 0x00000033 # abbreviated name for Wednesday
    LOCALE_SABBREVDAYNAME4 = 0x00000034 # abbreviated name for Thursday
    LOCALE_SABBREVDAYNAME5 = 0x00000035 # abbreviated name for Friday
    LOCALE_SABBREVDAYNAME6 = 0x00000036 # abbreviated name for Saturday
    LOCALE_SABBREVDAYNAME7 = 0x00000037 # abbreviated name for Sunday
    LOCALE_SMONTHNAME1 = 0x00000038 # long name for January
    LOCALE_SMONTHNAME2 = 0x00000039 # long name for February
    LOCALE_SMONTHNAME3 = 0x0000003A # long name for March
    LOCALE_SMONTHNAME4 = 0x0000003B # long name for April
    LOCALE_SMONTHNAME5 = 0x0000003C # long name for May
    LOCALE_SMONTHNAME6 = 0x0000003D # long name for June
    LOCALE_SMONTHNAME7 = 0x0000003E # long name for July
    LOCALE_SMONTHNAME8 = 0x0000003F # long name for August
    LOCALE_SMONTHNAME9 = 0x00000040 # long name for September
    LOCALE_SMONTHNAME10 = 0x00000041 # long name for October
    LOCALE_SMONTHNAME11 = 0x00000042 # long name for November
    LOCALE_SMONTHNAME12 = 0x00000043 # long name for December
    LOCALE_SMONTHNAME13 = 0x0000100E # long name for 13th month (if exists)
    LOCALE_SABBREVMONTHNAME1 = 0x00000044 # abbreviated name for January
    LOCALE_SABBREVMONTHNAME2 = 0x00000045 # abbreviated name for February
    LOCALE_SABBREVMONTHNAME3 = 0x00000046 # abbreviated name for March
    LOCALE_SABBREVMONTHNAME4 = 0x00000047 # abbreviated name for April
    LOCALE_SABBREVMONTHNAME5 = 0x00000048 # abbreviated name for May
    LOCALE_SABBREVMONTHNAME6 = 0x00000049 # abbreviated name for June
    LOCALE_SABBREVMONTHNAME7 = 0x0000004A # abbreviated name for July
    LOCALE_SABBREVMONTHNAME8 = 0x0000004B # abbreviated name for August
    LOCALE_SABBREVMONTHNAME9 = 0x0000004C # abbreviated name for September
    LOCALE_SABBREVMONTHNAME10 = 0x0000004D # abbreviated name for October
    LOCALE_SABBREVMONTHNAME11 = 0x0000004E # abbreviated name for November
    LOCALE_SABBREVMONTHNAME12 = 0x0000004F # abbreviated name for December
    LOCALE_SABBREVMONTHNAME13 = 0x0000100F # abbreviated name for 13th month (if exists)
    LOCALE_SPOSITIVESIGN = 0x00000050 # positive sign, eg ""
    LOCALE_SNEGATIVESIGN = 0x00000051 # negative sign, eg "-"
    LOCALE_IPOSSIGNPOSN = 0x00000052 # positive sign position (derived from INEGCURR)
    LOCALE_INEGSIGNPOSN = 0x00000053 # negative sign position (derived from INEGCURR)
    LOCALE_IPOSSYMPRECEDES = 0x00000054 # mon sym precedes pos amt (derived from ICURRENCY)
    LOCALE_IPOSSEPBYSPACE = 0x00000055 # mon sym sep by space from pos amt (derived from ICURRENCY)
    LOCALE_INEGSYMPRECEDES = 0x00000056 # mon sym precedes neg amt (derived from INEGCURR)
    LOCALE_INEGSEPBYSPACE = 0x00000057 # mon sym sep by space from neg amt (derived from INEGCURR)
    LOCALE_FONTSIGNATURE = 0x00000058 # font signature
    LOCALE_SISO639LANGNAME = 0x00000059 # ISO abbreviated language name, eg "en"
    LOCALE_SISO3166CTRYNAME = 0x0000005A # ISO abbreviated country/region name, eg "US"
    LOCALE_IPAPERSIZE = 0x0000100A # 1 = letter, 5 = legal, 8 = a3, 9 = a4
    LOCALE_SENGCURRNAME = 0x00001007 # english name of currency, eg "Euro"
    LOCALE_SNATIVECURRNAME = 0x00001008 # native name of currency, eg "euro"
    LOCALE_SYEARMONTH = 0x00001006 # year month format string, eg "MM/yyyy"
    LOCALE_SSORTNAME = 0x00001013 # sort name, usually "", eg "Dictionary" in UI Language
    LOCALE_IDIGITSUBSTITUTION = 0x00001014 # 0 = context, 1 = none, 2 = national
    LOCALE_SNAME = 0x0000005c # locale name (ie: en-us)
    LOCALE_SDURATION = 0x0000005d # time duration format, eg "hh:mm:ss"
    LOCALE_SSHORTESTDAYNAME1 = 0x00000060 # Shortest day name for Monday
    LOCALE_SSHORTESTDAYNAME2 = 0x00000061 # Shortest day name for Tuesday
    LOCALE_SSHORTESTDAYNAME3 = 0x00000062 # Shortest day name for Wednesday
    LOCALE_SSHORTESTDAYNAME4 = 0x00000063 # Shortest day name for Thursday
    LOCALE_SSHORTESTDAYNAME5 = 0x00000064 # Shortest day name for Friday
    LOCALE_SSHORTESTDAYNAME6 = 0x00000065 # Shortest day name for Saturday
    LOCALE_SSHORTESTDAYNAME7 = 0x00000066 # Shortest day name for Sunday
    LOCALE_SISO639LANGNAME2 = 0x00000067 # 3 character ISO abbreviated language name, eg "eng"
    LOCALE_SISO3166CTRYNAME2 = 0x00000068 # 3 character ISO country/region name, eg "USA"
    LOCALE_SNAN = 0x00000069 # Not a Number, eg "NaN"
    LOCALE_SPOSINFINITY = 0x0000006a # + Infinity, eg "infinity"
    LOCALE_SNEGINFINITY = 0x0000006b # - Infinity, eg "-infinity"
    LOCALE_SSCRIPTS = 0x0000006c # Typical scripts in the locale: ; delimited script codes, eg "Latn;"
    LOCALE_SPARENT = 0x0000006d # Fallback name for resources, eg "en" for "en-US"
    LOCALE_SCONSOLEFALLBACKNAME = 0x0000006e # Fallback name for within the console for Unicode Only locales, eg "en" for bn-IN
    LOCALE_IREADINGLAYOUT = 0x00000070 # Returns one of the following 4 reading layout values:
	# 0 - Left to right (eg en-US)
	# 1 - Right to left (eg arabic locales)
	# 2 - Vertical top to bottom with columns to the left and also left to right (ja-JP locales)
	# 3 - Vertical top to bottom with columns proceeding to the right
    LOCALE_INEUTRAL = 0x00000071 # Returns 0 for specific cultures, 1 for neutral cultures.
    LOCALE_INEGATIVEPERCENT = 0x00000074 # Returns 0-11 for the negative percent format
    LOCALE_IPOSITIVEPERCENT = 0x00000075 # Returns 0-3 for the positive percent formatIPOSITIVEPERCENT
    LOCALE_SPERCENT = 0x00000076 # Returns the percent symbol
    LOCALE_SPERMILLE = 0x00000077 # Returns the permille (U+2030) symbol
    LOCALE_SMONTHDAY = 0x00000078 # Returns the preferred month/day format
    LOCALE_SSHORTTIME = 0x00000079 # Returns the preferred short time format (ie: no seconds, just h:mm)
    LOCALE_SOPENTYPELANGUAGETAG = 0x0000007a # Open type language tag, eg: "latn" or "dflt"
    LOCALE_SSORTLOCALE = 0x0000007b # Name of locale to use for sorting/collation/casing behavior.
    LOCALE_SRELATIVELONGDATE = 0x0000007c # Long date without year, day of week, month, date, eg: for lock screen
    LOCALE_SSHORTESTAM = 0x0000007e # Shortest AM designator, eg "A"
    LOCALE_SSHORTESTPM = 0x0000007f # Shortest PM designator, eg "P"
	#
	# DEPRECATED LCTYPEs
	#
	# DEPRECATED LCTYPEs for Code Pages
	# Applications are strongly encouraged to Use Unicode, such as UTF-16 (WCHAR type)
	# or the CP_UTF8 Code Page.  Legacy encodings are unable to represent the full
	# set of scripts/language and characters (& emoji!) available on modern computers.
	# Use of legacy code pages (encodings) is a leading cause of data loss and corruption.
    LOCALE_IDEFAULTCODEPAGE = 0x0000000B # default oem code page for locale (user may configure as UTF-8, use of Unicode is recommended instead)
    LOCALE_IDEFAULTANSICODEPAGE = 0x00001004 # default ansi code page for locale (user may configure as UTF-8, use of Unicode is recommended instead)
    LOCALE_IDEFAULTMACCODEPAGE = 0x00001011 # default mac code page for locale (user may configure as UTF-8, use of Unicode is recommended instead)
    LOCALE_IDEFAULTEBCDICCODEPAGE = 0x00001012 # default ebcdic code page for a locale (use of Unicode is recommended instead)
	# LCTYPEs using out-of-date concepts
    LOCALE_ILANGUAGE = 0x00000001 # DEPRECATED language id (LCID), LOCALE_SNAME preferred
    LOCALE_SABBREVLANGNAME = 0x00000003 # DEPRECATED arbitrary abbreviated language name, LOCALE_SISO639LANGNAME instead.
    LOCALE_SABBREVCTRYNAME = 0x00000007 # DEPRECATED arbitrary abbreviated country/region name, LOCALE_SISO3166CTRYNAME instead.
    LOCALE_IGEOID = 0x0000005B # DEPRECATED geographical location id, use LOCALE_SISO3166CTRYNAME instead.
    LOCALE_IDEFAULTLANGUAGE = 0x00000009 # DEPRECATED default language id, deprecated
    LOCALE_IDEFAULTCOUNTRY = 0x0000000A # DEPRECATED default country/region code, deprecated
    LOCALE_IINTLCURRDIGITS = 0x0000001A # DEPRECATED, use LOCALE_ICURRDIGITS # intl monetary digits, eg 2 for $1.00
	# Derived legacy date & time values for compatibility only.
	# Please use the appropriate date or time pattern instead.
	# These can be misleading, for example a locale configured as 12h24m52s could have a time separator of "h".
    LOCALE_SDATE = 0x0000001D # DEPRECATED date separator (derived from LOCALE_SSHORTDATE, use that instead)
    LOCALE_STIME = 0x0000001E # DEPRECATED time separator (derived from LOCALE_STIMEFORMAT, use that instead)
    LOCALE_IDATE = 0x00000021 # DEPRECATED short date format ordering (derived from LOCALE_SSHORTDATE, use that instead)
    LOCALE_ILDATE = 0x00000022 # DEPRECATED long date format ordering (derived from LOCALE_SLONGDATE, use that instead)
    LOCALE_ITIME = 0x00000023 # DEPRECATED time format specifier (derived from LOCALE_STIMEFORMAT, use that instead)
    LOCALE_ITIMEMARKPOSN = 0x00001005 # DEPRECATED time marker position (derived from LOCALE_STIMEFORMAT, use that instead)
    LOCALE_ICENTURY = 0x00000024 # DEPRECATED century format specifier (short date, LOCALE_SSHORTDATE is preferred)
    LOCALE_ITLZERO = 0x00000025 # DEPRECATED leading zeros in time field (derived from LOCALE_STIMEFORMAT, use that instead)
    LOCALE_IDAYLZERO = 0x00000026 # DEPRECATED leading zeros in day field (short date, LOCALE_SSHORTDATE is preferred)
    LOCALE_IMONLZERO = 0x00000027 # DEPRECATED leading zeros in month field (short date, LOCALE_SSHORTDATE is preferred)
    LOCALE_SKEYBOARDSTOINSTALL = 0x0000005e # Used internally, see GetKeyboardLayoutName() function
	# LCTYPEs which have been renamed to enable more understandable source code.
    LOCALE_SLANGUAGE = LOCALE_SLOCALIZEDDISPLAYNAME # DEPRECATED as new name is more readable.
    LOCALE_SLANGDISPLAYNAME = LOCALE_SLOCALIZEDLANGUAGENAME # DEPRECATED as new name is more readable.
    LOCALE_SENGLANGUAGE = LOCALE_SENGLISHLANGUAGENAME # DEPRECATED as new name is more readable.
    LOCALE_SNATIVELANGNAME = LOCALE_SNATIVELANGUAGENAME # DEPRECATED as new name is more readable.
    LOCALE_SCOUNTRY = LOCALE_SLOCALIZEDCOUNTRYNAME # DEPRECATED as new name is more readable.
    LOCALE_SENGCOUNTRY = LOCALE_SENGLISHCOUNTRYNAME # DEPRECATED as new name is more readable.
    LOCALE_SNATIVECTRYNAME = LOCALE_SNATIVECOUNTRYNAME # DEPRECATED as new name is more readable.
	# DEPRECATED: Use LOCALE_SISO3166CTRYNAME to query for a region identifier, LOCALE_ICOUNTRY is not a region identifier.
    LOCALE_ICOUNTRY = LOCALE_IDIALINGCODE # Deprecated synonym for LOCALE_IDIALINGCODE
    LOCALE_S1159 = LOCALE_SAM # DEPRECATED: Please use LOCALE_SAM, which is more readable.
    LOCALE_S2359 = LOCALE_SPM # DEPRECATED: Please use LOCALE_SPM, which is more readable.
	#
	#  Time Flags for GetTimeFormat.
	#
    TIME_NOMINUTESORSECONDS = 0x00000001 # do not use minutes or seconds
    TIME_NOSECONDS = 0x00000002 # do not use seconds
    TIME_NOTIMEMARKER = 0x00000004 # do not use time marker
    TIME_FORCE24HOURFORMAT = 0x00000008 # always use 24 hour format
	#
	#  Date Flags for GetDateFormat.
	#
    DATE_SHORTDATE = 0x00000001 # use short date picture
    DATE_LONGDATE = 0x00000002 # use long date picture
    DATE_USE_ALT_CALENDAR = 0x00000004 # use alternate calendar (if any)
    DATE_YEARMONTH = 0x00000008 # use year month picture
    DATE_LTRREADING = 0x00000010 # add marks for left to right reading order layout
    DATE_RTLREADING = 0x00000020 # add marks for right to left reading order layout
    DATE_AUTOLAYOUT = 0x00000040 # add appropriate marks for left-to-right or right-to-left reading order layout
    DATE_MONTHDAY = 0x00000080 # include month day pictures
	#
	#  Calendar Types.
	#
	#  These types are used for the EnumCalendarInfo and GetCalendarInfo
	#  NLS API routines.
	#  Some of these types are also used for the SetCalendarInfo NLS API
	#  routine.
	#
	#
	#  The following CalTypes may be used in combination with any other CalTypes.
	#
	#    CAL_NOUSEROVERRIDE
	#
	#    CAL_RETURN_NUMBER will return the result from GetCalendarInfo as a
	#    number instead of a string.  This flag is only valid for the CalTypes
	#    beginning with CAL_I.
	#
	#    DEPRECATED: CAL_USE_CP_ACP is used in many of the A (Ansi) apis that need
	#                to do string translation.  Callers are encouraged to use the W
	#                (WCHAR/Unicode) apis instead.
	#
    CAL_NOUSEROVERRIDE = LOCALE_NOUSEROVERRIDE # Not Recommended - do not use user overrides
    CAL_USE_CP_ACP = LOCALE_USE_CP_ACP # DEPRECATED, call Unicode APIs instead: use the system ACP
    CAL_RETURN_NUMBER = LOCALE_RETURN_NUMBER # return number instead of string
    CAL_RETURN_GENITIVE_NAMES = LOCALE_RETURN_GENITIVE_NAMES # return genitive forms of month names
	#
	#  The following CalTypes are mutually exclusive in that they may NOT
	#  be used in combination with each other.
	#
    CAL_ICALINTVALUE = 0x00000001 # calendar type
    CAL_SCALNAME = 0x00000002 # native name of calendar
    CAL_IYEAROFFSETRANGE = 0x00000003 # starting years of eras
    CAL_SERASTRING = 0x00000004 # era name for IYearOffsetRanges, eg A.D.
    CAL_SSHORTDATE = 0x00000005 # short date format string
    CAL_SLONGDATE = 0x00000006 # long date format string
    CAL_SDAYNAME1 = 0x00000007 # native name for Monday
    CAL_SDAYNAME2 = 0x00000008 # native name for Tuesday
    CAL_SDAYNAME3 = 0x00000009 # native name for Wednesday
    CAL_SDAYNAME4 = 0x0000000a # native name for Thursday
    CAL_SDAYNAME5 = 0x0000000b # native name for Friday
    CAL_SDAYNAME6 = 0x0000000c # native name for Saturday
    CAL_SDAYNAME7 = 0x0000000d # native name for Sunday
    CAL_SABBREVDAYNAME1 = 0x0000000e # abbreviated name for Mon
    CAL_SABBREVDAYNAME2 = 0x0000000f # abbreviated name for Tue
    CAL_SABBREVDAYNAME3 = 0x00000010 # abbreviated name for Wed
    CAL_SABBREVDAYNAME4 = 0x00000011 # abbreviated name for Thu
    CAL_SABBREVDAYNAME5 = 0x00000012 # abbreviated name for Fri
    CAL_SABBREVDAYNAME6 = 0x00000013 # abbreviated name for Sat
    CAL_SABBREVDAYNAME7 = 0x00000014 # abbreviated name for Sun
	# Note that in the hebrew calendar the leap month name is always returned as the 7th month
    CAL_SMONTHNAME1 = 0x00000015 # native name for January
    CAL_SMONTHNAME2 = 0x00000016 # native name for February
    CAL_SMONTHNAME3 = 0x00000017 # native name for March
    CAL_SMONTHNAME4 = 0x00000018 # native name for April
    CAL_SMONTHNAME5 = 0x00000019 # native name for May
    CAL_SMONTHNAME6 = 0x0000001a # native name for June
    CAL_SMONTHNAME7 = 0x0000001b # native name for July
    CAL_SMONTHNAME8 = 0x0000001c # native name for August
    CAL_SMONTHNAME9 = 0x0000001d # native name for September
    CAL_SMONTHNAME10 = 0x0000001e # native name for October
    CAL_SMONTHNAME11 = 0x0000001f # native name for November
    CAL_SMONTHNAME12 = 0x00000020 # native name for December
    CAL_SMONTHNAME13 = 0x00000021 # native name for 13th month (if any)
    CAL_SABBREVMONTHNAME1 = 0x00000022 # abbreviated name for Jan
    CAL_SABBREVMONTHNAME2 = 0x00000023 # abbreviated name for Feb
    CAL_SABBREVMONTHNAME3 = 0x00000024 # abbreviated name for Mar
    CAL_SABBREVMONTHNAME4 = 0x00000025 # abbreviated name for Apr
    CAL_SABBREVMONTHNAME5 = 0x00000026 # abbreviated name for May
    CAL_SABBREVMONTHNAME6 = 0x00000027 # abbreviated name for Jun
    CAL_SABBREVMONTHNAME7 = 0x00000028 # abbreviated name for July
    CAL_SABBREVMONTHNAME8 = 0x00000029 # abbreviated name for Aug
    CAL_SABBREVMONTHNAME9 = 0x0000002a # abbreviated name for Sep
    CAL_SABBREVMONTHNAME10 = 0x0000002b # abbreviated name for Oct
    CAL_SABBREVMONTHNAME11 = 0x0000002c # abbreviated name for Nov
    CAL_SABBREVMONTHNAME12 = 0x0000002d # abbreviated name for Dec
    CAL_SABBREVMONTHNAME13 = 0x0000002e # abbreviated name for 13th month (if any)
    CAL_SYEARMONTH = 0x0000002f # year month format string
    CAL_ITWODIGITYEARMAX = 0x00000030 # two digit year max
    CAL_SSHORTESTDAYNAME1 = 0x00000031 # Shortest day name for Mo
    CAL_SSHORTESTDAYNAME2 = 0x00000032 # Shortest day name for Tu
    CAL_SSHORTESTDAYNAME3 = 0x00000033 # Shortest day name for We
    CAL_SSHORTESTDAYNAME4 = 0x00000034 # Shortest day name for Th
    CAL_SSHORTESTDAYNAME5 = 0x00000035 # Shortest day name for Fr
    CAL_SSHORTESTDAYNAME6 = 0x00000036 # Shortest day name for Sa
    CAL_SSHORTESTDAYNAME7 = 0x00000037 # Shortest day name for Su
    CAL_SMONTHDAY = 0x00000038 # Month/day format
    CAL_SABBREVERASTRING = 0x00000039 # Abbreviated era string (eg: AD)
    CAL_SRELATIVELONGDATE = 0x0000003a # Long date without year, day of week, month, date, eg: for lock screen
    CAL_SENGLISHERANAME = 0x0000003b # Japanese calendar only: return the English era names for .Net compatibility
    CAL_SENGLISHABBREVERANAME = 0x0000003c # Japanese calendar only: return the English Abbreviated era names for .Net compatibility
	# CAL_SJAPANESEERAFIRSTYEAR is only supported on machines with updates to support the "gannen" era first year behavior
	# Machines without that update will return 0 and ERROR_INVALID_FLAGS, in which case ichinen is presumed.
    CAL_SJAPANESEERAFIRSTYEAR = 0x0000003d # Japanese calendar only: return ichinen or gannen first year
	#
	#  Calendar Enumeration Value.
	#
    ENUM_ALL_CALENDARS = 0xffffffff # enumerate all calendars
	#
	#  Calendar ID Values.
	#
    CAL_GREGORIAN = 1 # Gregorian (localized) calendar
    CAL_GREGORIAN_US = 2 # Gregorian (U.S.) calendar
    CAL_JAPAN = 3 # Japanese Emperor Era calendar
    CAL_TAIWAN = 4 # Taiwan calendar
    CAL_KOREA = 5 # Korean Tangun Era calendar
    CAL_HIJRI = 6 # Hijri (Arabic Lunar) calendar
    CAL_THAI = 7 # Thai calendar
    CAL_HEBREW = 8 # Hebrew (Lunar) calendar
    CAL_GREGORIAN_ME_FRENCH = 9 # Gregorian Middle East French calendar
    CAL_GREGORIAN_ARABIC = 10 # Gregorian Arabic calendar
    CAL_GREGORIAN_XLIT_ENGLISH = 11 # Gregorian Transliterated English calendar
    CAL_GREGORIAN_XLIT_FRENCH = 12 # Gregorian Transliterated French calendar
    CAL_PERSIAN = 22 # Persian (Solar Hijri) calendar
    CAL_UMALQURA = 23 # UmAlQura Hijri (Arabic Lunar) calendar
	#
	# ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
	#
	#  Language Group ID Values
	#
	# The "Language Group" concept is an obsolete concept.
	# The groups returned are not well defined, arbitrary, inconsistent, inaccurate,
	# no longer maintained, and no longer supported.
	#
	# ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
	#
    LGRPID_WESTERN_EUROPE = 0x0001 # Western Europe & U.S.
    LGRPID_CENTRAL_EUROPE = 0x0002 # Central Europe
    LGRPID_BALTIC = 0x0003 # Baltic
    LGRPID_GREEK = 0x0004 # Greek
    LGRPID_CYRILLIC = 0x0005 # Cyrillic
    LGRPID_TURKIC = 0x0006 # Turkic
    LGRPID_TURKISH = 0x0006 # Turkish
    LGRPID_JAPANESE = 0x0007 # Japanese
    LGRPID_KOREAN = 0x0008 # Korean
    LGRPID_TRADITIONAL_CHINESE = 0x0009 # Traditional Chinese
    LGRPID_SIMPLIFIED_CHINESE = 0x000a # Simplified Chinese
    LGRPID_THAI = 0x000b # Thai
    LGRPID_HEBREW = 0x000c # Hebrew
    LGRPID_ARABIC = 0x000d # Arabic
    LGRPID_VIETNAMESE = 0x000e # Vietnamese
    LGRPID_INDIC = 0x000f # Indic
    LGRPID_GEORGIAN = 0x0010 # Georgian
    LGRPID_ARMENIAN = 0x0011 # Armenian
	#
	#  MUI function flag values
	#
    MUI_LANGUAGE_ID = 0x4 # Use traditional language ID convention
    MUI_LANGUAGE_NAME = 0x8 # Use ISO language (culture) name convention
    MUI_MERGE_SYSTEM_FALLBACK = 0x10 # GetThreadPreferredUILanguages merges in parent and base languages
    MUI_MERGE_USER_FALLBACK = 0x20 # GetThreadPreferredUILanguages merges in user preferred languages
    MUI_UI_FALLBACK = MUI_MERGE_SYSTEM_FALLBACK | MUI_MERGE_USER_FALLBACK
    MUI_THREAD_LANGUAGES = 0x40 # GetThreadPreferredUILanguages merges in user preferred languages
    MUI_CONSOLE_FILTER = 0x100 # SetThreadPreferredUILanguages takes on console specific behavior
    MUI_COMPLEX_SCRIPT_FILTER = 0x200 # SetThreadPreferredUILanguages takes on complex script specific behavior
    MUI_RESET_FILTERS = 0x001 # Reset MUI_CONSOLE_FILTER and MUI_COMPLEX_SCRIPT_FILTER
    MUI_USER_PREFERRED_UI_LANGUAGES = 0x10 # GetFileMUIPath returns the MUI files for the languages in the fallback list
    MUI_USE_INSTALLED_LANGUAGES = 0x20 # GetFileMUIPath returns all the MUI files installed in the machine
    MUI_USE_SEARCH_ALL_LANGUAGES = 0x40 # GetFileMUIPath returns all the MUI files irrespective of whether language is installed
    MUI_LANG_NEUTRAL_PE_FILE = 0x100 # GetFileMUIPath returns target file with .mui extension
    MUI_NON_LANG_NEUTRAL_FILE = 0x200 # GetFileMUIPath returns target file with same name as source
    MUI_MACHINE_LANGUAGE_SETTINGS = 0x400
    MUI_FILETYPE_NOT_LANGUAGE_NEUTRAL = 0x001 # GetFileMUIInfo found a non-split resource file
    MUI_FILETYPE_LANGUAGE_NEUTRAL_MAIN = 0x002 # GetFileMUIInfo found a LN main module resource file
    MUI_FILETYPE_LANGUAGE_NEUTRAL_MUI = 0x004 # GetFileMUIInfo found a LN MUI module resource file
    MUI_QUERY_TYPE = 0x001 # GetFileMUIInfo will look for the type of the resource file
    MUI_QUERY_CHECKSUM = 0x002 # GetFileMUIInfo will look for the checksum of the resource file
    MUI_QUERY_LANGUAGE_NAME = 0x004 # GetFileMUIInfo will look for the culture of the resource file
    MUI_QUERY_RESOURCE_TYPES = 0x008 # GetFileMUIInfo will look for the resource types of the resource file
    MUI_FILEINFO_VERSION = 0x001 # Version of FILEMUIINFO structure used with GetFileMUIInfo
    MUI_FULL_LANGUAGE = 0x01
    MUI_PARTIAL_LANGUAGE = 0x02
    MUI_LIP_LANGUAGE = 0x04
    MUI_LANGUAGE_INSTALLED = 0x20
    MUI_LANGUAGE_LICENSED = 0x40
	#
	# MUI_CALLBACK_FLAG defines are duplicated in rtlmui.h
	#
    # MUI_CALLBACK_ALL_FLAGS = MUI_CALLBACK_CAAG_UPGRADED_INSTALLATION # OR all other flags when defined.
	#
	# MUI_CALLBACK_ flags are duplicated in rtlmui.h
	#
	######################################
	#
	#  Typedefs
	#
	#  Define all types for the NLS component here.
	#
	######################################
	#
	# ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
	#
	#  Language Group ID
	#
	# The "Language Group" concept is an obsolete concept.
	# The groups returned are not well defined, arbitrary, inconsistent, inaccurate,
	# no longer maintained, and no longer supported.
	#
	# ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
    LGRPID = DWORD

    #
    # Local type constant.
    #
    LCTYPE = DWORD

    #
    # Calendar type constant.
    #
    CALTYPE = DWORD

    #
    # Calendar ID.
    #
    CALID = DWORD

    #
    #  CP Info.
    #
    # Deprecated.  Applications should use Unicode (WCHAR / UTF-16 or UTF-8)
    #
    # WARNING: These structures fail for some encodings, including UTF-8, which
    #          do not fit into the assumptions of these APIs.
    #

    class _cpinfo(CStructure):
        _fields_ = [
            ("MaxCharSize", UINT), # max length (in bytes) of a char
            ("DefaultChar", BYTE * MAX_DEFAULTCHAR), # default character
            ("LeadByte", BYTE * MAX_LEADBYTES) # lead byte ranges
        ]
    CPINFO = _cpinfo
    LPCPINFO = POINTER(CPINFO)

    #
    #  GEO defines
    #
    GEOTYPE = DWORD
    GEOCLASS = DWORD

    #
    # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
    #
    #  DEPRECATED: The GEOID  concept is deprecated, please use
    #  Country/Region Names instead, eg: "US" instead of a GEOID like 244.
    #  See the documentation for GetGeoInfoEx.
    #
    #  WARNING: These values are arbitrarily assigned values, please use
    #           standard country/region names instead, such as "US".
    #
    # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
    #
    GEOID = LONG

    GEOID_NOT_AVAILABLE = -1

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    class _cpinfoexA(CStructure):
        _fields_ = [
            ("MaxCharSize", UINT), # max length (in bytes) of a char
            ("DefaultChar", BYTE * MAX_DEFAULTCHAR), # default character (MB)
            ("LeadByte", BYTE * MAX_LEADBYTES), # lead byte ranges
            ("UnicodeDefaultChar", WCHAR), # default character (Unicode)
            ("CodePage", UINT), # code page id
            ("CodePageName", CHAR * MAX_PATH) # code page name (Unicode)
        ]
    CPINFOEXA = _cpinfoexA
    LPCPINFOEXA = POINTER(CPINFOEXA)

    class _cpinfoexW(CStructure):
        _fields_ = [
            ("MaxCharSize", UINT), # max length (in bytes) of a char
            ("DefaultChar", BYTE * MAX_DEFAULTCHAR), # default character (MB)
            ("LeadByte", BYTE * MAX_LEADBYTES), # lead byte ranges
            ("UnicodeDefaultChar", WCHAR), # default character (Unicode)
            ("CodePage", UINT), # code page id
            ("CodePageName", WCHAR * MAX_PATH) # code page name (Unicode)
        ]
    CPINFOEXW = _cpinfoexW
    LPCPINFOEXW = POINTER(CPINFOEXW)

    CPINFOEX = unicode(CPINFOEXW, CPINFOEXA)
    LPCPINFOEX = unicode(LPCPINFOEXW, LPCPINFOEXA)
    
    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    #
    #  Number format.
    #

    class _numberfmtA(CStructure):
        _fields_ = [
            ("NumDigits", UINT), # number of decimal digits
            ("LeadingZero", UINT), # if leading zero in decimal fields
            ("Grouping", UINT), # group size left of decimal
            ("lpDecimalSep", LPSTR), # ptr to decimal separator string
            ("lpThousandSep", LPSTR), # ptr to thousand separator string
            ("NegativeOrder", UINT) # negative number ordering
        ]
    NUMBERFMTA = _numberfmtA
    PNUMBERFMTA = POINTER(NUMBERFMTA)
    LPNUMBERFMTA = PNUMBERFMTA

    class _numberfmtW(CStructure):
        _fields_ = [
            ("NumDigits", UINT), # number of decimal digits
            ("LeadingZero", UINT), # if leading zero in decimal fields
            ("Grouping", UINT), # group size left of decimal
            ("lpDecimalSep", LPWSTR), # ptr to decimal separator string
            ("lpThousandSep", LPWSTR), # ptr to thousand separator string
            ("NegativeOrder", UINT) # negative number ordering
        ]
    NUMBERFMTW = _numberfmtW
    PNUMBERFMTW = POINTER(NUMBERFMTW)
    LPNUMBERFMTW = PNUMBERFMTW

    NUMBERFMT = unicode(NUMBERFMTW, NUMBERFMTA)
    PNUMBERFMT = unicode(PNUMBERFMTW, PNUMBERFMTA)
    LPNUMBERFMT = unicode(LPNUMBERFMTW, LPNUMBERFMTA)

    #
    #  Currency format.
    #

    class _currencyfmtA(CStructure):
        _fields_ = [
            ("NumDigits", UINT), # number of decimal digits
            ("LeadingZero", UINT), # if leading zero in decimal fields
            ("Grouping", UINT), # group size left of decimal
            ("lpDecimalSep", LPSTR), # ptr to decimal separator string
            ("lpThousandSep", LPSTR), # ptr to thousand separator string
            ("NegativeOrder", UINT), # negative currency ordering
            ("PositiveOrder", UINT), # positive currency ordering
            ("lpCurrencySymbol", LPSTR) # ptr to currency symbol string
        ]
    CURRENCYFMTA = _currencyfmtA
    PCURRENCYFMTA = POINTER(CURRENCYFMTA)
    LPCURRENCYFMTA = PCURRENCYFMTA

    class _currencyfmtW(CStructure):
        _fields_ = [
            ("NumDigits", UINT), # number of decimal digits
            ("LeadingZero", UINT), # if leading zero in decimal fields
            ("Grouping", UINT), # group size left of decimal
            ("lpDecimalSep", LPWSTR), # ptr to decimal separator string
            ("lpThousandSep", LPWSTR), # ptr to thousand separator string
            ("NegativeOrder", UINT), # negative currency ordering
            ("PositiveOrder", UINT), # positive currency ordering
            ("lpCurrencySymbol", LPWSTR) # ptr to currency symbol string
        ]
    CURRENCYFMTW = _currencyfmtW
    PCURRENCYFMTW = POINTER(CURRENCYFMTW)
    LPCURRENCYFMTW = PCURRENCYFMTW

    CURRENCYFMT = unicode(CURRENCYFMTW, CURRENCYFMTA)
    PCURRENCYFMT = unicode(PCURRENCYFMTW, PCURRENCYFMTA)
    LPCURRENCYFMT = unicode(LPCURRENCYFMTW, LPCURRENCYFMTA)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***
    #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    #
    #  NLS function capabilities
    #

    SYSNLS_FUNCTION = INT
    if True:
        COMPARE_STRING    =  0x0001,
    NLS_FUNCTION = DWORD


    #
    #  NLS version structure.
    #

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    if sys.getwindowsversion().major >= 6:
        #
        # New structures are the same
        #

        # The combination of dwNLSVersion, and guidCustomVersion
        # identify specific sort behavior, persist those to ensure identical
        # behavior in the future.
        class _nlsversioninfo(CStructure):
            _fields_ = [
                ("dwNLSVersionInfoSize", DWORD), # sizeof(NLSVERSIONINFO) == 32 bytes
                ("dwNLSVersion", DWORD), 
                ("dwDefinedVersion", DWORD), # Deprecated, use dwNLSVersion instead
                ("dwEffectiveId", DWORD), # Deprecated, use guidCustomVerison instead
                ("guidCustomVersion", GUID) # Explicit sort version
            ]
        NLSVERSIONINFO = _nlsversioninfo
        LPNLSVERSIONINFO = POINTER(NLSVERSIONINFO)

    else:
        # 
        # Windows 7 and below had different sizes
        #

        # This is to be deprecated, please use the NLSVERSIONINFOEX
        # structure below in the future.  The difference is that
        # guidCustomversion is required to uniquely identify a sort
        class _nlsversioninfo(CStructure): # Use NLSVERSIONINFOEX instead
            _fields_ = [
                ("dwNLSVersionInfoSize", DWORD), # 12 bytes
                ("dwNLSVersion", DWORD),
                ("dwDefinedVersion", DWORD) # Deprecated, use dwNLSVersion instead
            ]
        NLSVERSIONINFO = _nlsversioninfo
        LPNLSVERSIONINFO = POINTER(NLSVERSIONINFO)

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    # The combination of dwNLSVersion, and guidCustomVersion
    # identify specific sort behavior, persist those to ensure identical
    # behavior in the future.
    class _nlsversioninfoex(CStructure):
        _fields_ = [
            ("dwNLSVersionInfoSize", DWORD), # sizeof(NLSVERSIONINFOEX) == 32 bytes
            ("dwNLSVersion", DWORD), 
            ("dwDefinedVersion", DWORD), # Deprecated, use dwNLSVersion instead
            ("dwEffectiveId", DWORD), # Deprecated, use guidCustomVerison instead
            ("guidCustomVersion", GUID) # Explicit sort version
        ]
    NLSVERSIONINFOEX = _nlsversioninfoex
    LPNLSVERSIONINFOEX = POINTER(NLSVERSIONINFOEX)

    GEO_NAME_USER_DEFAULT = NULL

    #
    #  GEO information types for clients to query
    #
    # Please use GetGeoInfoEx and query by country/region name instead of GEOID (eg: "US" instead of 244)
    SYSGEOTYPE = INT
    if True:
        GEO_NATION      =       0x0001 # DEPRECATED Not used by name API
        GEO_LATITUDE    =       0x0002
        GEO_LONGITUDE   =       0x0003
        GEO_ISO2        =       0x0004
        GEO_ISO3        =       0x0005
        GEO_RFC1766     =       0x0006 # DEPRECATED and misleading, not used by name API
        GEO_LCID        =       0x0007 # DEPRECATED Not used by name API
        GEO_FRIENDLYNAME=       0x0008
        GEO_OFFICIALNAME=       0x0009
        GEO_TIMEZONES   =       0x000A # Not implemented
        GEO_OFFICIALLANGUAGES = 0x000B # Not implemented
        GEO_ISO_UN_NUMBER =     0x000C
        GEO_PARENT      =       0x000D
        GEO_DIALINGCODE =       0x000E
        GEO_CURRENCYCODE=       0x000F # eg: USD
        GEO_CURRENCYSYMBOL=     0x0010 # eg: $
        GEO_NAME        =       0x0011 # Name, eg: US or 001
        GEO_ID          =       0x0012  # DEPRECATED - For compatibility, please avoid

    #
    #  More GEOCLASS defines will be listed here
    #
    SYSGEOCLASS = INT
    if True:
        GEOCLASS_NATION  = 16
        GEOCLASS_REGION  = 14          # DEPRECATED - Never used
        GEOCLASS_ALL = 0

    LOCALE_ENUMPROCA = CALLBACK(BOOL, LPSTR) # Deprecated, please use Unicode
    LOCALE_ENUMPROCW = CALLBACK(BOOL, LPWSTR) # DEPRECATED: please use LOCALE_ENUMPROCEX                                        

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    #
    #  Normalization forms
    #

    _NORM_FORM = INT
    if True:
        NormalizationOther  = 0       # Not supported
        NormalizationC      = 0x1     # Each base plus combining characters to the canonical precomposed equivalent.
        NormalizationD      = 0x2     # Each precomposed character to its canonical decomposed equivalent.
        NormalizationKC     = 0x5     # Each base plus combining characters to the canonical precomposed
                                    #   equivalents and all compatibility characters to their equivalents.
        NormalizationKD     = 0x6      # Each precomposed character to its canonical decomposed equivalent
                                    #   and all compatibility characters to their equivalents.
    NORM_FORM = _NORM_FORM

    HSAVEDUILANGUAGES = HANDLE

    #
    # IDN (International Domain Name) Flags
    #
    IDN_ALLOW_UNASSIGNED = 0x01  # Allow unassigned "query" behavior per RFC 3454
    IDN_USE_STD3_ASCII_RULES = 0x02  # Enforce STD3 ASCII restrictions for legal characters
    IDN_EMAIL_ADDRESS = 0x04  # Enable EAI algorithmic fallback for email local parts behavior
    IDN_RAW_PUNYCODE = 0x08  # Disable validation and mapping of punycode.   

    VS_ALLOW_LATIN = 0x0001  # Allow Latin in test script even if not present in locale script

    GSS_ALLOW_INHERITED_COMMON = 0x0001  # Output script ids for inherited and common character types if present

    #
    #  Enumeration function constants.
    #
    LANGUAGEGROUP_ENUMPROCA = CALLBACK(BOOL, LGRPID, LPSTR, LPSTR, DWORD, LONG_PTR) # Deprecated, please use Unicode
    LANGGROUPLOCALE_ENUMPROCA = CALLBACK(BOOL, LGRPID, LCID, LPSTR, LONG_PTR) # Deprecated, please use Unicode
    UILANGUAGE_ENUMPROCA = CALLBACK(BOOL, LPSTR, LONG_PTR) # Deprecated, please use Unicode
    CODEPAGE_ENUMPROCA = CALLBACK(BOOL, LPSTR) # Deprecated, please use Unicode
    DATEFMT_ENUMPROCA = CALLBACK(BOOL, LPSTR) # Deprecated, please use Unicode
    DATEFMT_ENUMPROCEXA = CALLBACK(BOOL, LPSTR, CALID) # Deprecated, please use Unicode
    TIMEFMT_ENUMPROCA = CALLBACK(BOOL, LPSTR) # Deprecated, please use Unicode
    CALINFO_ENUMPROCA = CALLBACK(BOOL, LPSTR) # Deprecated, please use Unicode
    CALINFO_ENUMPROCEXA = CALLBACK(BOOL, LPSTR, CALID) # Deprecated, please use Unicode

    LANGUAGEGROUP_ENUMPROCW = CALLBACK(BOOL, LGRPID, LPWSTR, LPWSTR, DWORD, LONG_PTR) # DEPRECATED: Language groups are no longer supported
    LANGGROUPLOCALE_ENUMPROCW = CALLBACK(BOOL, LGRPID, LCID, LPWSTR, LONG_PTR) # DEPRECATED: Language groups are no longer supported
    UILANGUAGE_ENUMPROCW = CALLBACK(BOOL, LPWSTR, LONG_PTR) 
    CODEPAGE_ENUMPROCW = CALLBACK(BOOL, LPWSTR) # Please use Unicode / UTF-8
    DATEFMT_ENUMPROCW = CALLBACK(BOOL, LPWSTR)
    DATEFMT_ENUMPROCEXW = CALLBACK(BOOL, LPWSTR, CALID)
    TIMEFMT_ENUMPROCW = CALLBACK(BOOL, LPWSTR)
    CALINFO_ENUMPROCW = CALLBACK(BOOL, LPWSTR)
    CALINFO_ENUMPROCEXW = CALLBACK(BOOL, LPWSTR, CALID)

    GEO_ENUMPROC = CALLBACK(BOOL, GEOID) # DEPRECATED, use GEO_ENUMNAMEPROC instead
    GEO_ENUMNAMEPROC = CALLBACK(BOOL, PWSTR, LPARAM)

    LANGUAGEGROUP_ENUMPROC = unicode(LANGUAGEGROUP_ENUMPROCW,LANGUAGEGROUP_ENUMPROCA)
    LANGGROUPLOCALE_ENUMPROC = unicode(LANGGROUPLOCALE_ENUMPROCW, LANGGROUPLOCALE_ENUMPROCA)
    UILANGUAGE_ENUMPROC = unicode(UILANGUAGE_ENUMPROCW, UILANGUAGE_ENUMPROCA)
    CODEPAGE_ENUMPROC = unicode(CODEPAGE_ENUMPROCW, CODEPAGE_ENUMPROCA)
    DATEFMT_ENUMPROC = unicode(DATEFMT_ENUMPROCW, DATEFMT_ENUMPROCA)
    DATEFMT_ENUMPROCEX = unicode(DATEFMT_ENUMPROCEXW, DATEFMT_ENUMPROCEXA)
    TIMEFMT_ENUMPROC = unicode(TIMEFMT_ENUMPROCW, TIMEFMT_ENUMPROCA)
    CALINFO_ENUMPROC = unicode(CALINFO_ENUMPROCW, CALINFO_ENUMPROCA)
    CALINFO_ENUMPROCEX = unicode(CALINFO_ENUMPROCEXW, CALINFO_ENUMPROCEXA) 

    #
    # Information about a MUI file, used as input/output in GetFileMUIInfo
    # All offsets are relative to start of the structure. Offsets with value 0 mean empty field.
    #

    class _FILEMUIINFO(CStructure):
        _fields_ = [
            ("dwSize", DWORD), 
            ("dwVersion", DWORD), 
            ("dwFileType", DWORD),
            ("pChecksum", BYTE * 16), 
            ("pServiceChecksum", BYTE * 16),
            ("dwLanguageNameOffset", DWORD), 
            ("dwTypeIDMainSize", DWORD), 
            ("dwTypeIDMainOffset", DWORD), 
            ("dwTypeNameMainOffset", DWORD), 
            ("dwTypeIDMUISize", DWORD), 
            ("dwTypeIDMUIOffset", DWORD), 
            ("dwTypeNameMUIOffset", DWORD), 
            ("abBuffer", BYTE * 8)
        ]
    FILEMUIINFO = _FILEMUIINFO
    PFILEMUIINFO = POINTER(FILEMUIINFO)

    ######################################
    #
    #  Function Prototypes
    #
    #  Only prototypes for the NLS APIs should go here.
    #
    ######################################

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    #
    #  Code Page Dependent APIs.
    #
    #  Applications should use Unicode (WCHAR / UTF-16 &/or UTF-8)
    #
    IsValidCodePage = declare(kernel32.IsValidCodePage, BOOL, UINT)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***


    # REGION ***

    # REGION *** Desktop or Pc Family or OneCore or Games Family ***

    GetCPInfo = declare(kernel32.GetCPInfo, BOOL, UINT, LPCPINFO)

    # REGION ***

    # REGION *** Desktop or Pc Family or OneCore Family or Games Family ***

    GetCPInfoExA = declare(kernel32.GetCPInfoExA, BOOL, UINT, DWORD, LPCPINFOEXA)
    GetCPInfoExW = declare(kernel32.GetCPInfoExW, BOOL, UINT, DWORD, LPCPINFOEXW)
    GetCPInfoEx = unicode(GetCPInfoExW, GetCPInfoExA)

    # REGION ***
    #
    #  Locale Dependent APIs.
    #

    # REGION *** Desktop or OneCore or Application or Games Family ***

    CompareStringA = declare(kernel32.CompareStringA, INT, LCID, DWORD, PCNZCH, INT, PCNZCH, INT)
    if cpreproc.ifndef("UNICODE"):
            CompareString = CompareStringA
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_APP | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application or OneCore or Games Family ***

    # DEPRECATED: FindNLSStringEx is preferred
    FindNLSString = declare(kernel32.FindNLSString, INT, LCID, DWORD, LPCWSTR, INT, LPCWSTR, INT, LPINT)

    # REGION ***

    # REGION *** Desktop or OneCore or Games Family ***

    # DEPRECATED: LCMapStringEx is preferred
    LCMapStringW = declare(kernel32.LCMapStringW, INT, LCID, DWORD, LPCWSTR, INT, LPWSTR, INT)
    if cpreproc.ifdef("UNICODE"):
        LCMapString = LCMapStringW
    # DEPRECATED: Use Unicode, LCMapStringEx is preferred
    LCMapStringA = declare(kernel32.LCMapStringA, INT, LCID, DWORD, LPCSTR, INT, LPSTR, INT)
    if cpreproc.ifndef("UNICODE"):
            LCMapString = LCMapStringA
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    # DEPRECATED: GetLocaleInfoEx is preferred
    GetLocaleInfoW = declare(kernel32.GetLocaleInfoW, INT, LCID, LCTYPE, LPWSTR, INT)
    if cpreproc.ifdef("UNICODE"):
        GetLocaleInfo = GetLocaleInfoW
    # DEPRECATED: Use Unicode. GetLocaleInfoEx is preferred
    GetLocaleInfoA = declare(kernel32.GetLocaleInfoA, INT, LCID, LCTYPE, LPSTR, INT)
    if cpreproc.ifndef("UNICODE"):
        GetLocaleInfo = GetLocaleInfoA
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application or OneCore Family ***

    SetLocaleInfoA = declare(kernel32.SetLocaleInfoA, BOOL, LCID, LCTYPE, LPCSTR)
    SetLocaleInfoW = declare(kernel32.SetLocaleInfoW, BOOL, LCID, LCTYPE, LPCWSTR)
    SetLocaleInfo = unicode(SetLocaleInfoW, SetLocaleInfoA)
    # DEPRECATED: GetCalendarInfoEx is preferred
    GetCalendarInfoA = declare(kernel32.GetCalendarInfoA, INT, LCID, CALID, CALTYPE, LPSTR, INT, LPDWORD)
    # DEPRECATED: GetCalendarInfoEx is preferred
    GetCalendarInfoW = declare(kernel32.GetCalendarInfoW, INT, LCID, CALID, CALTYPE, LPWSTR, INT, LPDWORD)
    GetCalendarInfo = unicode(GetCalendarInfoW, GetCalendarInfoA)
    SetCalendarInfoA = declare(kernel32.SetCalendarInfoA, BOOL, LCID, CALID, CALTYPE, LPCSTR)
    SetCalendarInfoW = declare(kernel32.SetCalendarInfoW, BOOL, LCID, CALID, CALTYPE, LPCWSTR)
    SetCalendarInfo = unicode(SetCalendarInfoW, SetCalendarInfoA)
    # !UNICODE
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family ***

    #
    # Flags used by LoadStringByReference
    #
    MUI_FORMAT_REG_COMPAT = 0x0001
    MUI_FORMAT_INF_COMPAT = 0x0002
    MUI_VERIFY_FILE_EXISTS = 0x0004
    MUI_SKIP_STRING_CACHE = 0x0008
    MUI_IMMUTABLE_LOOKUP = 0x0010
    LoadStringByReference = declare(kernelbase.LoadStringByReference, BOOL, DWORD, PCWSTR, PCWSTR, PWSTR, ULONG, PCWSTR, PULONG)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    IsDBCSLeadByte = declare(kernel32.IsDBCSLeadByte, BOOL, BYTE)
    IsDBCSLeadByteEx = declare(kernel32.IsDBCSLeadByteEx, BOOL, UINT, BYTE)

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    # Use of Locale Names is preferred, LCIDs are deprecated.
    # This function is provided to enable compatibility with legacy data sets only.
    LocaleNameToLCID = declare(kernel32.LocaleNameToLCID, LCID, LPCWSTR, DWORD)
    # Use of Locale Names is preferred, LCIDs are deprecated.
    # This function is provided to enable compatibility with legacy data sets only.
    LCIDToLocaleName = declare(kernel32.LCIDToLocaleName, INT, LCID, LPWSTR, INT, DWORD)

    # REGION ***

    # REGION *** Desktop Family ***

    # DEPRECATED: GetDurationFormatEx is preferred
    GetDurationFormat = declare(kernel32.GetDurationFormat, INT, LCID, DWORD, PSYSTEMTIME, ULONGLONG, LPCWSTR, LPWSTR, INT)

    # REGION ***

    # REGION *** Desktop Family or OneCore or Games Family ***

    # DEPRECATED: GetNumberFormatEx is preferred
    GetNumberFormatA = declare(kernel32.GetNumberFormatA, INT, LCID, DWORD, LPCSTR, PNUMBERFMTA, LPSTR, INT)
    # DEPRECATED: GetNumberFormatEx is preferred
    GetNumberFormatW = declare(kernel32.GetNumberFormatW, INT, LCID, DWORD, LPCWSTR, PNUMBERFMTW, LPWSTR, INT)
    GetNumberFormat = unicode(GetNumberFormatW, GetNumberFormatA)
    # DEPRECATED: GetCurrencyFormatEx is preferred
    GetCurrencyFormatA = declare(kernel32.GetCurrencyFormatA, INT, LCID, DWORD, LPCSTR, PCURRENCYFMTA, LPSTR, INT)
    # DEPRECATED: GetCurrencyFormatEx is preferred
    GetCurrencyFormatW = declare(kernel32.GetCurrencyFormatW, INT, LCID, DWORD, LPCWSTR, PCURRENCYFMTW, LPWSTR, INT)
    GetCurrencyFormat = unicode(GetCurrencyFormatW, GetCurrencyFormatA)
    # !UNICODE
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    # DEPRECATED: EnumCalendarInfoExEx is preferred
    EnumCalendarInfoA = declare(kernel32.EnumCalendarInfoA, BOOL, CALINFO_ENUMPROCA, LCID, CALID, CALTYPE)
    # DEPRECATED: EnumCalendarInfoExEx is preferred
    EnumCalendarInfoW = declare(kernel32.EnumCalendarInfoW, BOOL, CALINFO_ENUMPROCW, LCID, CALID, CALTYPE)
    EnumCalendarInfo = unicode(EnumCalendarInfoW, EnumCalendarInfoA)
    # DEPRECATED: EnumCalendarInfoExEx is preferred
    EnumCalendarInfoExA = declare(kernel32.EnumCalendarInfoExA, BOOL, CALINFO_ENUMPROCEXA, LCID, CALID, CALTYPE)
    # DEPRECATED: EnumCalendarInfoExEx is preferred
    EnumCalendarInfoExW = declare(kernel32.EnumCalendarInfoExW, BOOL, CALINFO_ENUMPROCEXW, LCID, CALID, CALTYPE)
    EnumCalendarInfoEx = unicode(EnumCalendarInfoExW, EnumCalendarInfoExA)
    # WINVER >= 0x0500
    # DEPRECATED: EnumTimeFormatsEx is preferred
    EnumTimeFormatsA = declare(kernel32.EnumTimeFormatsA, BOOL, TIMEFMT_ENUMPROCA, LCID, DWORD)
    # DEPRECATED: EnumTimeFormatsEx is preferred
    EnumTimeFormatsW = declare(kernel32.EnumTimeFormatsW, BOOL, TIMEFMT_ENUMPROCW, LCID, DWORD)
    EnumTimeFormats = unicode(EnumTimeFormatsW, EnumTimeFormatsA)
    # !UNICODE
    # DEPRECATED: EnumDateFormatsExEx is preferred
    EnumDateFormatsA = declare(kernel32.EnumDateFormatsA, BOOL, DATEFMT_ENUMPROCA, LCID, DWORD)
    # DEPRECATED: EnumDateFormatsExEx is preferred
    EnumDateFormatsW = declare(kernel32.EnumDateFormatsW, BOOL, DATEFMT_ENUMPROCW, LCID, DWORD)
    EnumDateFormats = unicode(EnumDateFormatsW, EnumDateFormatsA)
    # !UNICODE
    # DEPRECATED: EnumDateFormatsExEx is preferred
    EnumDateFormatsExA = declare(kernel32.EnumDateFormatsExA, BOOL, DATEFMT_ENUMPROCEXA, LCID, DWORD)
    # DEPRECATED: EnumDateFormatsExEx is preferred
    EnumDateFormatsExW = declare(kernel32.EnumDateFormatsExW, BOOL, DATEFMT_ENUMPROCEXW, LCID, DWORD)
    EnumDateFormatsEx = unicode(EnumDateFormatsExW, EnumDateFormatsExA)
    # WINVER >= 0x0500
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    IsValidLanguageGroup = declare(kernel32.IsValidLanguageGroup, BOOL, LGRPID, DWORD)
    # DEPRECATED: GetNLSVersionEx is preferred
    GetNLSVersion = declare(kernel32.GetNLSVersion, BOOL, NLS_FUNCTION, LCID, LPNLSVERSIONINFO)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    # DEPRECATED: IsValidLocaleName is preferred
    IsValidLocale = declare(kernel32.IsValidLocale, BOOL, LCID, DWORD)

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    # GetGeoInfoEx is preferred where available
    GetGeoInfoA = declare(kernel32.GetGeoInfoA, INT, GEOID, GEOTYPE, LPSTR, INT, LANGID)
    # GetGeoInfoEx is preferred where available
    GetGeoInfoW = declare(kernel32.GetGeoInfoW, INT, GEOID, GEOTYPE, LPWSTR, INT, LANGID)
    GetGeoInfo = unicode(GetGeoInfoW, GetGeoInfoA)
    GetGeoInfoEx = declare(kernel32.GetGeoInfoEx, INT, PWSTR, GEOTYPE, PWSTR, INT)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop or PC Family or OneCore Family ***

    # EnumSystemGeoNames is preferred where available
    EnumSystemGeoID = declare(kernel32.EnumSystemGeoID, BOOL, GEOCLASS, GEOID, GEO_ENUMPROC)
    EnumSystemGeoNames = declare(kernel32.EnumSystemGeoNames, BOOL, GEOCLASS, GEO_ENUMNAMEPROC, LPARAM)

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    # GetUserDefaultGeoName is preferred where available
    GetUserGeoID = declare(kernel32.GetUserGeoID, GEOID, GEOCLASS)

    """
    *
    *

    """

    GetUserDefaultGeoName = declare(kernel32.GetUserDefaultGeoName, INT, LPWSTR, INT)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    # GetUserDefaultGeoName is preferred where available
    # Applications are recommended to not change user settings themselves.
    SetUserGeoID = declare(kernel32.SetUserGeoID, BOOL, GEOID)
    # Applications are recommended to not change user settings themselves.
    SetUserGeoName = declare(kernel32.SetUserGeoName, BOOL, PWSTR)
    # DEPRECATED: Please use ResolveLocaleName
    ConvertDefaultLocale = declare(kernel32.ConvertDefaultLocale, LCID, LCID)
    # DEPRECATED: Please use the user's language profile.

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    SetThreadLocale = declare(kernel32.SetThreadLocale, BOOL, LCID)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    # DEPRECATED: Please use the user's language profile.
    # DEPRECATED: Please use GetUserDefaultLocaleName

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    # DEPRECATED: Please use GetUserDefaultLocaleName or the user's Language Profile
    # DEPRECATED: Please use GetUserDefaultLocaleName or the user's Language Profile
    # DEPRECATED: Please use GetUserDefaultLocaleName

    # REGION ***

    # REGION *** Desktop Family ***


    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    GetProcessPreferredUILanguages = declare(kernel32.GetProcessPreferredUILanguages, BOOL, DWORD, PULONG, PZZWSTR, PULONG)
    SetProcessPreferredUILanguages = declare(kernel32.SetProcessPreferredUILanguages, BOOL, DWORD, PCZZWSTR, PULONG)

    # REGION ***

    # REGION *** Desktop Family or Phone Family or OneCore or Games Family ***


    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetThreadPreferredUILanguages = declare(kernel32.GetThreadPreferredUILanguages, BOOL, DWORD, PULONG, PZZWSTR, PULONG)
    SetThreadPreferredUILanguages = declare(kernel32.SetThreadPreferredUILanguages, BOOL, DWORD, PCZZWSTR, PULONG)
    GetFileMUIInfo = declare(kernel32.GetFileMUIInfo, BOOL, DWORD, PCWSTR, PFILEMUIINFO, PDWORD)
    GetFileMUIPath = declare(kernel32.GetFileMUIPath, BOOL, DWORD, PCWSTR, PWSTR, PULONG, PWSTR, PULONG, PULONGLONG)
    GetUILanguageInfo = declare(kernel32.GetUILanguageInfo, BOOL, DWORD, PCZZWSTR, PZZWSTR, PDWORD, PDWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    SetThreadPreferredUILanguages2 = declare(kernelbase.SetThreadPreferredUILanguages2, BOOL, ULONG, PCZZWSTR, PULONG, POINTER(HSAVEDUILANGUAGES))

    # REGION ***

    # REGION *** Desktop Family ***

    NotifyUILanguageChange = declare(kernel32.NotifyUILanguageChange, BOOL, DWORD, PCWSTR, PCWSTR, DWORD, PDWORD)

    # REGION ***
    #
    #  Locale Independent APIs.
    #

    # REGION *** Desktop or OneCore or Application or Games Family ***

    GetStringTypeExA = declare(kernel32.GetStringTypeExA, BOOL, LCID, DWORD, LPCSTR, INT, LPWORD)
    if cpreproc.ifndef("UNICODE"):
            GetStringTypeEx = GetStringTypeExA
    #
    #  NOTE: The parameters for GetStringTypeA and GetStringTypeW are
    #        NOT the same.  The W version was shipped in NT 3.1.  The
    #        A version was then shipped in 16-bit OLE with the wrong
    #        parameters (ported from Win95).  To be compatible, we
    #        must break the relationship between the A and W versions
    #        of GetStringType.  There will be NO function call for the
    #        generic GetStringType.
    #
    #        GetStringTypeEx (above) should be used instead.
    #
    GetStringTypeA = declare(kernel32.GetStringTypeA, BOOL, LCID, DWORD, LPCSTR, INT, LPWORD)
    FoldStringA = declare(kernel32.FoldStringA, INT, DWORD, LPCSTR, INT, LPSTR, INT)
    if cpreproc.ifndef("UNICODE"):
        FoldString = FoldStringA

    # REGION ***

    # REGION *** Desktop Family or OneCore or Games Family ***

    # DEPRECATED, please use Locale Names and call EnumSystemLocalesEx
    EnumSystemLocalesA = declare(kernel32.EnumSystemLocalesA, BOOL, LOCALE_ENUMPROCA, DWORD)
    # DEPRECATED, please use Locale Names and call EnumSystemLocalesEx
    EnumSystemLocalesW = declare(kernel32.EnumSystemLocalesW, BOOL, LOCALE_ENUMPROCW, DWORD)
    EnumSystemLocales = unicode(EnumSystemLocalesW, EnumSystemLocalesA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    EnumSystemLanguageGroupsA = declare(kernel32.EnumSystemLanguageGroupsA, BOOL, LANGUAGEGROUP_ENUMPROCA, DWORD, LONG_PTR)
    EnumSystemLanguageGroupsW = declare(kernel32.EnumSystemLanguageGroupsW, BOOL, LANGUAGEGROUP_ENUMPROCW, DWORD, LONG_PTR)
    EnumSystemLanguageGroups = unicode(EnumSystemLanguageGroupsW, EnumSystemLanguageGroupsA)
    EnumLanguageGroupLocalesA = declare(kernel32.EnumLanguageGroupLocalesA, BOOL, LANGGROUPLOCALE_ENUMPROCA, LGRPID, DWORD, LONG_PTR)
    EnumLanguageGroupLocalesW = declare(kernel32.EnumLanguageGroupLocalesW, BOOL, LANGGROUPLOCALE_ENUMPROCW, LGRPID, DWORD, LONG_PTR)
    EnumLanguageGroupLocales = unicode(EnumLanguageGroupLocalesW, EnumLanguageGroupLocalesA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    # DEPRECATED: use the user language profile instead.
    EnumUILanguagesA = declare(kernel32.EnumUILanguagesA, BOOL, UILANGUAGE_ENUMPROCA, DWORD, LONG_PTR)
    # DEPRECATED: use the user language profile instead.
    EnumUILanguagesW = declare(kernel32.EnumUILanguagesW, BOOL, UILANGUAGE_ENUMPROCW, DWORD, LONG_PTR)
    EnumUILanguages = unicode(EnumUILanguagesW, EnumUILanguagesA)
    # WINVER >= 0x0500
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop or PC Family or OneCore Family ***

    # Please use Unicode instead.  Use of other code pages/encodings is discouraged.
    EnumSystemCodePagesA = declare(kernel32.EnumSystemCodePagesA, BOOL, CODEPAGE_ENUMPROCA, DWORD)
    # Please use Unicode instead.  Use of other code pages/encodings is discouraged.
    EnumSystemCodePagesW = declare(kernel32.EnumSystemCodePagesW, BOOL, CODEPAGE_ENUMPROCW, DWORD)
    EnumSystemCodePages = unicode(EnumSystemCodePagesW, EnumSystemCodePagesA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP  | WINAPI_PARTITION_SYSTEM)

    # REGION ***
    #
    # Windows API Normalization Functions
    #

    # REGION *** Application Family or OneCore or Games Family ***

    #
    # IDN (International Domain Name) Functions
    #

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    # optional behavior flags
    # Locale list of scripts string
    # size of locale script list string
    # test scripts string
    # size of test list string
    # optional behavior flags
    # Unicode character input string
    # size of input string
    # Script list output string
    # size of output string

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    #
    # String based NLS APIs
    #
    LOCALE_NAME_USER_DEFAULT = NULL
    LOCALE_NAME_INVARIANT = u""
    LOCALE_NAME_SYSTEM_DEFAULT = u"!x-sys-default-locale"
    GetLocaleInfoEx = declare(kernel32.GetLocaleInfoEx, INT, LPCWSTR, LCTYPE, LPWSTR, INT)

    # REGION ***

    # REGION *** Desktop or PC Family or OneCore Family ***

    GetCalendarInfoEx = declare(kernel32.GetCalendarInfoEx, INT, LPCWSTR, CALID, LPCWSTR, CALTYPE, LPWSTR, INT, LPDWORD)

    # REGION ***

    # REGION *** Application Family ***

    if cpreproc.ifndef("GetDurationFormatEx_DEFINED"):
        GetDurationFormatEx = declare(kernel32.GetDurationFormatEx, INT, LPCWSTR, DWORD, PSYSTEMTIME, ULONGLONG, LPCWSTR, LPWSTR, INT)

        # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetNumberFormatEx = declare(kernel32.GetNumberFormatEx, INT, LPCWSTR, DWORD, LPCWSTR, PNUMBERFMTW, LPWSTR, INT)
    GetCurrencyFormatEx = declare(kernel32.GetCurrencyFormatEx, INT, LPCWSTR, DWORD, LPCWSTR, PCURRENCYFMTW, LPWSTR, INT)
    GetUserDefaultLocaleName = declare(kernel32.GetUserDefaultLocaleName, INT, LPWSTR, INT)

    # REGION ***

    # REGION *** Desktop or PC Family or OneCore Family ***

    GetSystemDefaultLocaleName = declare(kernel32.GetSystemDefaultLocaleName, INT, LPWSTR, INT)
    IsNLSDefinedString = declare(kernel32.IsNLSDefinedString, BOOL, NLS_FUNCTION, DWORD, LPNLSVERSIONINFO, LPCWSTR, INT)
    GetNLSVersionEx = declare(kernel32.GetNLSVersionEx, BOOL, NLS_FUNCTION, LPCWSTR, LPNLSVERSIONINFOEX)
    IsValidNLSVersion = declare(kernel32.IsValidNLSVersion, DWORD, NLS_FUNCTION, LPCWSTR, LPNLSVERSIONINFOEX)

    # REGION ***

    # REGION *** Application Family or OneCore or Gamaes Family ***

    FindNLSStringEx = declare(kernel32.FindNLSStringEx, INT, LPCWSTR, DWORD, LPCWSTR, INT, LPCWSTR, INT, LPINT, LPNLSVERSIONINFO, LPVOID, LPARAM)
    LCMapStringEx = declare(kernel32.LCMapStringEx, INT, LPCWSTR, DWORD, LPCWSTR, INT, LPWSTR, INT, LPNLSVERSIONINFO, LPVOID, LPARAM)
    IsValidLocaleName = declare(kernel32.IsValidLocaleName, BOOL, LPCWSTR)

    # REGION ***

    # REGION *** Desktop or PC Family or OneCore Family ***

    CALINFO_ENUMPROCEXEX = CALLBACK(BOOL, LPWSTR, CALID, LPWSTR, LPARAM)
    EnumCalendarInfoExEx = declare(kernel32.EnumCalendarInfoExEx, BOOL, CALINFO_ENUMPROCEXEX, LPCWSTR, CALID, LPCWSTR, CALTYPE, LPARAM)
    DATEFMT_ENUMPROCEXEX = CALLBACK(BOOL, LPWSTR, CALID, LPARAM)
    EnumDateFormatsExEx = declare(kernel32.EnumDateFormatsExEx, BOOL, DATEFMT_ENUMPROCEXEX, LPCWSTR, DWORD, LPARAM)
    TIMEFMT_ENUMPROCEX = CALLBACK(BOOL, LPWSTR, LPARAM)
    EnumTimeFormatsEx = declare(kernel32.EnumTimeFormatsEx, BOOL, TIMEFMT_ENUMPROCEX, LPCWSTR, DWORD, LPARAM)

    # REGION ***

    # REGION *** Desktop or PC Family or OneCore or Games Family ***

    LOCALE_ENUMPROCEX = CALLBACK(BOOL, LPWSTR, DWORD, LPARAM)
    EnumSystemLocalesEx = declare(kernel32.EnumSystemLocalesEx, BOOL, LOCALE_ENUMPROCEX, DWORD, LPARAM, LPVOID)

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    ResolveLocaleName = declare(kernel32.ResolveLocaleName, INT, LPCWSTR, LPWSTR, INT)

    # REGION ***

    # REGION *** Desktop Family ***


    # REGION ***
    # NONLS