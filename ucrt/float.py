#
# float.h
#
#      Copyright (c) Microsoft Corporation. All rights reserved.
#
# Implementation-defined values commonly used by sophisticated numerical
# (floating point) programs.
#

from .. import cpreproc

from ..minwindef import *

from ..defbase import declare

cpreproc.define("_INC_FLOAT")

ucrtbase = W_WinDLL("ucrtbase.dll")

# Define the floating point precision used.
#
# For x86, results are in double precision (unless /arch:sse2 is used, in which
# case results are in source precision.
#
# For x64 and ARM, results are in source precision.
#
# If the compiler is invoked with /fp:fast, the compiler is allowed to use the
# fastest precision and even mix within a single function, so precision is
# indeterminable.
#
# Note that manipulating the floating point behavior using the float_control/
# fenv_access/fp_contract #pragmas may alter the actual floating point evaluation
# method, which may in turn invalidate the value of FLT_EVAL_METHOD.
FLT_EVAL_METHOD = 2
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Constants
#
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
DBL_DECIMAL_DIG = 17 # # of decimal digits of rounding precision
DBL_DIG = 15 # # of decimal digits of precision
DBL_EPSILON = 2.2204460492503131e-016 # smallest such that 1.0+DBL_EPSILON != 1.0
DBL_HAS_SUBNORM = 1 # type does support subnormal numbers
DBL_MANT_DIG = 53 # # of bits in mantissa
DBL_MAX = 1.7976931348623158e+308 # max value
DBL_MAX_10_EXP = 308 # max decimal exponent
DBL_MAX_EXP = 1024 # max binary exponent
DBL_MIN = 2.2250738585072014e-308 # min positive value
DBL_MIN_10_EXP = (-307) # min decimal exponent
DBL_MIN_EXP = (-1021) # min binary exponent
DBL_RADIX = 2 # exponent radix
DBL_TRUE_MIN = 4.9406564584124654e-324 # min positive value
FLT_DECIMAL_DIG = 9 # # of decimal digits of rounding precision
FLT_DIG = 6 # # of decimal digits of precision
FLT_EPSILON = 1.192092896e-07 # smallest such that 1.0+FLT_EPSILON != 1.0
FLT_HAS_SUBNORM = 1 # type does support subnormal numbers
FLT_GUARD = 0
FLT_MANT_DIG = 24 # # of bits in mantissa
FLT_MAX = 3.402823466e+38 # max value
FLT_MAX_10_EXP = 38 # max decimal exponent
FLT_MAX_EXP = 128 # max binary exponent
FLT_MIN = 1.175494351e-38 # min normalized positive value
FLT_MIN_10_EXP = (-37) # min decimal exponent
FLT_MIN_EXP = (-125) # min binary exponent
FLT_NORMALIZE = 0
FLT__RADIX = 2 # exponent radix
FLT_TRUE_MIN = 1.401298464e-45 # min positive value
LDBL_DIG = DBL_DIG # # of decimal digits of precision
LDBL_EPSILON = DBL_EPSILON # smallest such that 1.0+LDBL_EPSILON != 1.0
LDBL__HAS_SUBNORM = DBL_HAS_SUBNORM # type does support subnormal numbers
LDBL_MANT_DIG = DBL_MANT_DIG # # of bits in mantissa
LDBL_MAX = DBL_MAX # max value
LDBL_MAX_10_EXP = DBL_MAX_10_EXP # max decimal exponent
LDBL_MAX_EXP = DBL_MAX_EXP # max binary exponent
LDBL_MIN = DBL_MIN # min normalized positive value
LDBL_MIN_10_EXP = DBL_MIN_10_EXP # min decimal exponent
LDBL_MIN_EXP = DBL_MIN_EXP # min binary exponent
LDBL_RADIX = DBL_RADIX # exponent radix
LDBL_TRUE_MIN = DBL_TRUE_MIN # min positive value
DECIMAL_DIG = DBL_DECIMAL_DIG
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Flags
#
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
SW_INEXACT = 0x00000001 # Inexact (precision)
SW_UNDERFLOW = 0x00000002 # Underflow
SW_OVERFLOW = 0x00000004 # Overflow
SW_ZERODIVIDE = 0x00000008 # Divide by zero
SW_INVALID = 0x00000010 # Invalid
SW_DENORMAL = 0x00080000 # Denormal status bit
# New Control Bit that specifies the ambiguity in control word.
EM_AMBIGUIOUS = 0x80000000 # For backwards compatibility
EM_AMBIGUOUS = 0x80000000
# Abstract User Control Word Mask and bit definitions
MCW_EM = 0x0008001f # Interrupt Exception Masks
EM_INEXACT = 0x00000001 #     inexact (precision)
EM_UNDERFLOW = 0x00000002 #     underflow
EM_OVERFLOW = 0x00000004 #     overflow
EM_ZERODIVIDE = 0x00000008 #     zero divide
EM_INVALID = 0x00000010 #     invalid
EM_DENORMAL = 0x00080000 # Denormal exception mask (_control87 only)
MCW_RC = 0x00000300 # Rounding Control
RC_NEAR = 0x00000000 #     near
RC_DOWN = 0x00000100 #     down
RC_UP = 0x00000200 #     up
RC_CHOP = 0x00000300 #     chop
# i386 specific definitions
MCW_PC = 0x00030000 # Precision Control
PC_64 = 0x00000000 #     64 bits
PC_53 = 0x00010000 #     53 bits
PC_24 = 0x00020000 #     24 bits
MCW_IC = 0x00040000 # Infinity Control
IC_AFFINE = 0x00040000 #     affine
IC_PROJECTIVE = 0x00000000 #     projective
# RISC specific definitions
MCW_DN = 0x03000000 # Denormal Control
DN_SAVE = 0x00000000 #   save denormal results and operands
DN_FLUSH = 0x01000000 #   flush denormal results and operands to zero
DN_FLUSH_OPERANDS_SAVE_RESULTS = 0x02000000 # flush operands to zero and save results
DN_SAVE_OPERANDS_FLUSH_RESULTS = 0x03000000 # save operands and flush results to zero
# Invalid subconditions (_SW_INVALID also set)
SW_UNEMULATED = 0x0040 # Unemulated instruction
SW_SQRTNEG = 0x0080 # Square root of a negative number
SW_STACKOVERFLOW = 0x0200 # FP stack overflow
SW_STACKUNDERFLOW = 0x0400 # FP stack underflow
# Floating point error signals and return codes
FPE_INVALID = 0x81
FPE_DENORMAL = 0x82
FPE_ZERODIVIDE = 0x83
FPE_OVERFLOW = 0x84
FPE_UNDERFLOW = 0x85
FPE_INEXACT = 0x86
FPE_UNEMULATED = 0x87
FPE_SQRTNEG = 0x88
FPE_STACKOVERFLOW = 0x8a
FPE_STACKUNDERFLOW = 0x8b
FPE_EXPLICITGEN = 0x8c # raise(SIGFPE);
# On x86 with arch:SSE2, the OS returns these exceptions
FPE_MULTIPLE_TRAPS = 0x8d
FPE_MULTIPLE_FAULTS = 0x8e
FPCLASS_SNAN = 0x0001 # signaling NaN
FPCLASS_QNAN = 0x0002 # quiet NaN
FPCLASS_NINF = 0x0004 # negative infinity
FPCLASS_NN = 0x0008 # negative normal
FPCLASS_ND = 0x0010 # negative denormal
FPCLASS_NZ = 0x0020 # -0
FPCLASS_PZ = 0x0040 # +0
FPCLASS_PD = 0x0080 # positive denormal
FPCLASS_PN = 0x0100 # positive normal
FPCLASS_PINF = 0x0200 # positive infinity
# Initial Control Word value
CW_DEFAULT = (RC_NEAR + PC_53 + EM_INVALID + EM_ZERODIVIDE + EM_OVERFLOW + EM_UNDERFLOW + EM_INEXACT + EM_DENORMAL)

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# State Manipulation
#
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Note that reading or writing the floating point control or status words is
# not supported in managed code.
clearfp = declare(ucrtbase._clearfp, UINT, VOID)
controlfp = declare(ucrtbase._controlfp, UINT, UINT, UINT)
set_controlfp = declare(ucrtbase._set_controlfp, VOID, UINT, UINT)
controlfp_s = declare(ucrtbase._controlfp_s, INT, PUINT, UINT, UINT)
statusfp = declare(ucrtbase._statusfp, UINT, VOID)
fpreset = declare(ucrtbase._fpreset, VOID, VOID)
#statusfp2 = declare(ucrtbase._statusfp2, VOID, PUINT, PUINT)
clear87 = clearfp
status87 = statusfp
control87 = declare(ucrtbase._control87, UINT, UINT, UINT)
#control87_2 = declare(ucrtbase._control87_2, INT, UINT, UINT, PUINT, PUINT)
# Global variable holding floating point error code
_fpecode = declare(ucrtbase.__fpecode, PINT, VOID)
fpecode = lambda: cast(_fpecode(), PINT).value
_fpe_flt_rounds = declare(ucrtbase.__fpe_flt_rounds, INT, VOID)
FLT_ROUNDS = lambda: _fpe_flt_rounds()
DBL_ROUNDS = FLT_ROUNDS
LDBL_ROUNDS = DBL_ROUNDS

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# IEEE Recommended Functions
#
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
copysign = declare(ucrtbase._copysign, DOUBLE, DOUBLE, DOUBLE)
chgsign = declare(ucrtbase._chgsign, DOUBLE, DOUBLE)
scalb = declare(ucrtbase._scalb, DOUBLE, DOUBLE, LONG)
logb = declare(ucrtbase._logb, DOUBLE, DOUBLE)
nextafter = declare(ucrtbase._nextafter, DOUBLE, DOUBLE, DOUBLE)
finite = declare(ucrtbase._finite, INT, DOUBLE)
isnan = declare(ucrtbase._isnan, INT, DOUBLE)
fpclass = declare(ucrtbase._fpclass, INT, DOUBLE)
scalbf = declare(ucrtbase._scalbf, FLOAT, FLOAT, LONG)