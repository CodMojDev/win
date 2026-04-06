#
# Java JNI Definitions
#

from ..minwindef import *

jint = LONG
jlong = INT64
jbyte = c_byte

jboolean = BYTE
jchar = USHORT
jshort = SHORT
jfloat = FLOAT
jdouble = DOUBLE
jsize = jint

class __jobject(CStructure):
    _fields_ = []
    
_jobject = __jobject.PTR()
jobject = _jobject
jclass = jobject
jthrowable = jobject
jstring = jobject
jarray = jobject
jbooleanArray = jobject
jbyteArray = jobject
jcharArray = jobject
jshortArray = jobject
jintArray = jobject
jlongArray = jobject
jfloatArray = jobject
jdoubleArray = jobject
jobjectArray = jobject

jweak = jobject

class jvalue(CUnion):
    _fields_ = [
        ('z', jboolean),
        ('b', jbyte),
        ('c', jchar),
        ('s', jshort),
        ('i', jint),
        ('j', jlong),
        ('f', jfloat),
        ('d', jdouble),
        ('l', jobject)
    ]
    
    z: int
    b: int
    c: int
    s: int
    i: int
    j: int
    f: int
    d: int
    
    l: jobject
    
class __jfieldID(CStructure):
    _fields_ = []
    
_jfieldID = __jfieldID.PTR()
jfieldID = _jfieldID

class __jmethodID(CStructure):
    _fields_ = []

_jmethodID = __jmethodID.PTR()
jmethodID = _jmethodID

# Return values from jobjectRefType
JNIInvalidRefType    = 0
JNILocalRefType      = 1
JNIGlobalRefType     = 2
JNIWeakGlobalRefType = 3
jobjectRefType = UINT

#
# jboolean constants
#

JNI_FALSE = 0
JNI_TRUE = 1

#
# possible return values for JNI functions.
#

JNI_OK           = 0                 # success
JNI_ERR          = (-1)              # unknown error
JNI_EDETACHED    = (-2)              # thread detached from the VM
JNI_EVERSION     = (-3)              # JNI version error
JNI_ENOMEM       = (-4)              # not enough memory
JNI_EEXIST       = (-5)              # VM already created
JNI_EINVAL       = (-6)              # invalid arguments

#
# used in ReleaseScalarArrayElements
#

JNI_COMMIT = 1
JNI_ABORT = 2

class JNINativeMethod(CStructure):
    """
    used in RegisterNatives to describe native method name, signature,
    and function pointer.
    """
    
    _fields_ = [
        ('name', LPSTR), 
        ('signature', LPSTR),
        ('fnPtr', PVOID)
    ]
    
    signature: str
    fnPtr: int
    name: str

class JNIEnv(CStructure):
    """
    JNI Native Method Interface.
    """
    
    vt = VirtualTable('JNIEnv')
    
    # reserved 0-3
    vt.skip_count(4)
    
    @vt.function(jint)
    def GetVersion(self) -> int: ...
    
    
    @vt.function(jclass, LPSTR, jobject, PTR(jbyte), jsize)
    def DefineClass(self, name: bytes, loaded: jobject,
                    buf: IPointer[jbyte], len: int) -> jclass: ...
    
    @vt.function(jclass, LPSTR)
    def FindClass(self, name: bytes) -> jclass: ...
    
    
    @vt.function(jmethodID, jobject)
    def FromReflectedMethod(self, method: jobject) -> jmethodID: ...
    
    @vt.function(jfieldID, jobject)
    def FromReflectedField(self, field: jobject) -> jfieldID: ...
    
    
    @vt.function(jobject, jclass, jmethodID, jboolean)
    def ToReflectedMethod(self, cls: jclass, methodID: jmethodID, isStatic: int) -> jobject: ...
    
    @vt.function(jclass, jclass)
    def GetSuperclass(self, sub: jclass) -> jclass: ...
    
    @vt.function(jboolean, jclass, jclass)
    def IsAssignableFrom(self, sub: jclass, sup: jclass) -> int: ...
    
    @vt.function(jobject, jclass, jfieldID, jboolean)
    def ToReflectedField(self, cls: jclass, fieldID: jfieldID, isStatic: int) -> jobject: ...
    
    @vt.function(jint, jthrowable)
    def Throw(self, obj: jthrowable) -> int: ...
    
    @vt.function(jint, jclass, LPSTR)
    def ThrowNew(self, clazz: jclass, msg: bytes) -> int: ...
    
    @vt.function(jthrowable)
    def ExceptionOccurred(self) -> jthrowable: ...
    
    @vt.function(VOID)
    def ExceptionDescribe(self): ...
    
    @vt.function(VOID)
    def ExceptionClear(self): ...
    
    @vt.function(VOID, LPSTR)
    def FatalError(self, msg: bytes): ...
    
    
    @vt.function(jint, jint)
    def PushLocalFrame(self, capacity: int) -> int: ...
    
    @vt.function(jobject, jobject)
    def PopLocalFrame(self, result: jobject) -> jobject: ...
    
    
    @vt.function(jobject, jobject)
    def NewGlobalRef(self, lobj: jobject) -> jobject: ...
    
    @vt.function(VOID, jobject)
    def DeleteGlobalRef(self, gref: jobject): ...
    
    @vt.function(VOID, jobject)
    def DeleteLocalRef(self, obj: jobject): ...
    
    @vt.function(jboolean, jobject, jobject)
    def IsSameObject(self, obj1: jobject, obj2: jobject) -> int: ...
    
    @vt.function(jobject, jobject)
    def NewLocalRef(self, ref: jobject) -> jobject: ...
    
    @vt.function(jint, jint)
    def EnsureLocalCapacity(self, capacity: int) -> int: ...
    
    
    @vt.function(jobject, jclass)
    def AllocObject(self, clazz: jclass) -> jobject: ...
    
    @vt.function(jobject, jclass, jmethodID)
    def NewObject(self, clazz: jclass, methodID: jmethodID, **kwargs) -> jobject: ...
    
    # va_list & jvalue version
    vt.skip_count(2)
    
    
    @vt.function(jclass, jobject)
    def GetObjectClass(self, obj: jobject) -> jclass: ...
    
    @vt.function(jboolean, jobject, jclass)
    def IsInstanceOf(self, obj: jobject, clazz: jclass) -> int: ...
    
    
    @vt.function(jmethodID, jclass, LPSTR, LPSTR)
    def GetMethodID(self, clazz: jclass, name: bytes, sig: bytes) -> jmethodID: ...
    
    
    @vt.function(jobject, jobject, jmethodID)
    def CallObjectMethod(self, obj: jobject, methodID: jmethodID, **kwargs) -> jobject: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jboolean, jobject, jmethodID)
    def CallBooleanMethod(self, obj: jobject, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jbyte, jobject, jmethodID)
    def CallByteMethod(self, obj: jobject, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jchar, jobject, jmethodID)
    def CallCharMethod(self, obj: jobject, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jshort, jobject, jmethodID)
    def CallShortMethod(self, obj: jobject, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jint, jobject, jmethodID)
    def CallIntMethod(self, obj: jobject, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jlong, jobject, jmethodID)
    def CallLongMethod(self, obj: jobject, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jfloat, jobject, jmethodID)
    def CallFloatMethod(self, obj: jobject, methodID: jmethodID, **kwargs) -> float: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jdouble, jobject, jmethodID)
    def CallDoubleMethod(self, obj: jobject, methodID: jmethodID, **kwargs) -> float: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(VOID, jobject, jmethodID)
    def CallVoidMethod(self, obj: jobject, methodID: jmethodID, **kwargs): ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jobject, jobject, jmethodID)
    def CallNonvirtualObjectMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID) -> jobject: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jboolean, jobject, jmethodID)
    def CallNonvirtualBooleanMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jbyte, jobject, jmethodID)
    def CallNonvirtualByteMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jchar, jobject, jmethodID)
    def CallNonvirtualCharMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jshort, jobject, jmethodID)
    def CallNonvirtualShortMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jint, jobject, jmethodID)
    def CallNonvirtualIntMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jlong, jobject, jmethodID)
    def CallNonvirtualLongMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jfloat, jobject, jmethodID)
    def CallNonvirtualFloatMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID) -> float: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jdouble, jobject, jmethodID)
    def CallNonvirtualDoubleMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID) -> float: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(VOID, jobject, jmethodID)
    def CallNonvirtualVoidMethod(self, obj: jobject, clazz: jclass,
                                   methodID: jmethodID): ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jfieldID, jclass, LPSTR, LPSTR)
    def GetFieldID(self, clazz: jclass, name: bytes, sig: bytes) -> jfieldID: ...
    
    
    @vt.function(jobject, jobject, jfieldID)
    def GetObjectField(self, obj: jobject, fieldID: jfieldID) -> jobject: ...
    
    @vt.function(jboolean, jobject, jfieldID)
    def GetBooleanField(self, obj: jobject, fieldID: jfieldID) -> int: ...
    
    @vt.function(jbyte, jobject, jfieldID)
    def GetByteField(self, obj: jobject, fieldID: jfieldID) -> int: ...
    
    @vt.function(jchar, jobject, jfieldID)
    def GetCharField(self, obj: jobject, fieldID: jfieldID) -> int: ...
    
    @vt.function(jshort, jobject, jfieldID)
    def GetShortField(self, obj: jobject, fieldID: jfieldID) -> int: ...
    
    @vt.function(jint, jobject, jfieldID)
    def GetIntField(self, obj: jobject, fieldID: jfieldID) -> int: ...
    
    @vt.function(jlong, jobject, jfieldID)
    def GetLongField(self, obj: jobject, fieldID: jfieldID) -> int: ...
    
    @vt.function(jfloat, jobject, jfieldID)
    def GetFloatField(self, obj: jobject, fieldID: jfieldID) -> float: ...
    
    @vt.function(jdouble, jobject, jfieldID)
    def GetDoubleField(self, obj: jobject, fieldID: jfieldID) -> float: ...
    
    
    @vt.function(VOID, jobject, jfieldID, jobject)
    def SetObjectField(self, obj: jobject, fieldID: jfieldID, val: jobject): ...
    
    @vt.function(VOID, jobject, jfieldID, jboolean)
    def SetBooleanField(self, obj: jobject, fieldID: jfieldID, val: int): ...
    
    @vt.function(VOID, jobject, jfieldID, jbyte)
    def SetByteField(self, obj: jobject, fieldID: jfieldID, val: int): ...
    
    @vt.function(VOID, jobject, jfieldID, jchar)
    def SetCharField(self, obj: jobject, fieldID: jfieldID, val: int): ...
    
    @vt.function(VOID, jobject, jfieldID, jshort)
    def SetShortField(self, obj: jobject, fieldID: jfieldID, val: int): ...
    
    @vt.function(VOID, jobject, jfieldID, jint)
    def SetIntField(self, obj: jobject, fieldID: jfieldID, val: int): ...
    
    @vt.function(VOID, jobject, jfieldID, jlong)
    def SetLongField(self, obj: jobject, fieldID: jfieldID, val: int): ...
    
    @vt.function(VOID, jobject, jfieldID, jfloat)
    def SetFloatField(self, obj: jobject, fieldID: jfieldID, val: float): ...
    
    @vt.function(VOID, jobject, jfieldID, jdouble)
    def SetDoubleField(self, obj: jobject, fieldID: jfieldID, val: float): ...
    
    
    @vt.function(jmethodID, jclass, LPSTR, LPSTR)
    def GetStaticMethodID(self, clazz: jclass, name: bytes, sig: bytes) -> jmethodID: ...
    
    
    @vt.function(jobject, jclass, jmethodID)
    def CallStaticObjectMethod(self, clazz: jclass, methodID: jmethodID, **kwargs) -> jobject: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jboolean, jclass, jmethodID)
    def CallStaticBooleanMethod(self, clazz: jclass, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jbyte, jclass, jmethodID)
    def CallStaticByteMethod(self, clazz: jclass, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jchar, jclass, jmethodID)
    def CallStaticCharMethod(self, clazz: jclass, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jshort, jclass, jmethodID)
    def CallStaticShortMethod(self, clazz: jclass, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jint, jclass, jmethodID)
    def CallStaticIntMethod(self, clazz: jclass, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jlong, jclass, jmethodID)
    def CallStaticLongMethod(self, clazz: jclass, methodID: jmethodID, **kwargs) -> int: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jfloat, jclass, jmethodID)
    def CallStaticFloatMethod(self, clazz: jclass, methodID: jmethodID, **kwargs) -> float: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jdouble, jclass, jmethodID)
    def CallStaticDoubleMethod(self, clazz: jclass, methodID: jmethodID, **kwargs) -> float: ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(VOID, jclass, jmethodID)
    def CallStaticVoidMethod(self, clazz: jclass, methodID: jmethodID, **kwargs): ...
    
    vt.skip_count(2) # va_list & jvalue version
    
    
    @vt.function(jfieldID, jclass, LPSTR, LPSTR)
    def GetStaticFieldID(self, clazz: jclass, name: bytes, sig: bytes) -> jfieldID: ...
    
    @vt.function(jobject, jclass, jfieldID)
    def GetStaticObjectField(self, clazz: jclass, fieldID: jfieldID) -> jobject: ...
    
    @vt.function(jboolean, jclass, jfieldID)
    def GetStaticBooleanField(self, clazz: jclass, fieldID: jfieldID) -> int: ...
    
    @vt.function(jbyte, jclass, jfieldID)
    def GetStaticByteField(self, clazz: jclass, fieldID: jfieldID) -> int: ...
    
    @vt.function(jchar, jclass, jfieldID)
    def GetStaticCharField(self, clazz: jclass, fieldID: jfieldID) -> int: ...
    
    @vt.function(jshort, jclass, jfieldID)
    def GetStaticShortField(self, clazz: jclass, fieldID: jfieldID) -> int: ...
    
    @vt.function(jint, jclass, jfieldID)
    def GetStaticIntField(self, clazz: jclass, fieldID: jfieldID) -> int: ...
    
    @vt.function(jlong, jclass, jfieldID)
    def GetStaticLongField(self, clazz: jclass, fieldID: jfieldID) -> int: ...
    
    @vt.function(jfloat, jclass, jfieldID)
    def GetStaticFloatField(self, clazz: jclass, fieldID: jfieldID) -> float: ...
    
    @vt.function(jdouble, jclass, jfieldID)
    def GetStaticDoubleField(self, clazz: jclass, fieldID: jfieldID) -> float: ...
    
    
    @vt.function(VOID, jclass, jfieldID, jobject)
    def SetStaticObjectField(self, clazz: jclass, fieldID: jfieldID, value: jobject): ...
    
    @vt.function(VOID, jclass, jfieldID, jboolean)
    def SetStaticBooleanField(self, clazz: jclass, fieldID: jfieldID, value: int): ...
    
    @vt.function(VOID, jclass, jfieldID, jbyte)
    def SetStaticByteField(self, clazz: jclass, fieldID: jfieldID, value: int): ...
    
    @vt.function(VOID, jclass, jfieldID, jchar)
    def SetStaticCharField(self, clazz: jclass, fieldID: jfieldID, value: int): ...
    
    @vt.function(VOID, jclass, jfieldID, jshort)
    def SetStaticShortField(self, clazz: jclass, fieldID: jfieldID, value: int): ...
    
    @vt.function(VOID, jclass, jfieldID, jint)
    def SetStaticIntField(self, clazz: jclass, fieldID: jfieldID, value: int): ...
    
    @vt.function(VOID, jclass, jfieldID, jlong)
    def SetStaticLongField(self, clazz: jclass, fieldID: jfieldID, value: int): ...
    
    @vt.function(VOID, jclass, jfieldID, jfloat)
    def SetStaticFloatField(self, clazz: jclass, fieldID: jfieldID, value: float): ...
    
    @vt.function(VOID, jclass, jfieldID, jdouble)
    def SetStaticDoubleField(self, clazz: jclass, fieldID: jfieldID, value: float): ...
    
    
    @vt.function(jstring, LPWSTR, jsize)
    def NewString(self, unicode: str, len: int) -> jstring: ...
    
    @vt.function(jsize, jstring)
    def GetStringLength(self, str: jstring) -> int: ...
    
    @vt.function(LPWSTR, jstring, PTR(jboolean))
    def GetStringChars(self, str: jstring, isCopy: IPointer[jboolean]) -> LPWSTR: ...
    
    @vt.function(VOID, jstring, LPWSTR)
    def ReleaseStringChars(self, str: jstring, chars: LPWSTR): ...
    
    # UTF-8 not supported
    vt.skip_count(4)
    
    
    @vt.function(jsize, jarray)
    def GetArrayLength(self, array: jarray) -> int: ...
    
    
    @vt.function(jobjectArray, jsize, jclass, jobject)
    def NewObjectArray(self, len: int, clazz: jclass, init: jobject) -> jobjectArray: ...
    
    @vt.function(jobject, jobjectArray, jsize)
    def GetObjectArrayElement(self, array: jobjectArray, index: int) -> jobject: ...
    
    @vt.function(VOID, jobjectArray, jsize, jobject)
    def SetObjectArrayElement(self, array: jobjectArray, index: int, val: jobject): ...
    
    
    @vt.function(jbooleanArray, jsize)
    def NewBooleanArray(self, len: int) -> jbooleanArray: ...
    
    @vt.function(jbyteArray, jsize)
    def NewByteArray(self, len: int) -> jbyteArray: ...
    
    @vt.function(jcharArray, jsize)
    def NewCharArray(self, len: int) -> jcharArray: ...
    
    @vt.function(jshortArray, jsize)
    def NewShortArray(self, len: int) -> jshortArray: ...
    
    @vt.function(jintArray, jsize)
    def NewIntArray(self, len: int) -> jintArray: ...
    
    @vt.function(jlongArray, jsize)
    def NewLongArray(self, len: int) -> jlongArray: ...
    
    @vt.function(jfloatArray, jsize)
    def NewFloatArray(self, len: int) -> jfloatArray: ...
    
    @vt.function(jdoubleArray, jsize)
    def NewDoubleArray(self, len: int) -> jdoubleArray: ...
    
    
    @vt.function(PTR(jboolean), jbooleanArray, PTR(jboolean))
    def GetBooleanArrayElements(self, array: jbooleanArray, isCopy: IPointer[jboolean]) -> IPointer[int]: ...
    
    @vt.function(PTR(jbyte), jbyteArray, PTR(jboolean))
    def GetByteArrayElements(self, array: jbyteArray, isCopy: IPointer[jboolean]) -> IPointer[int]: ...
    
    @vt.function(PTR(jchar), jcharArray, PTR(jboolean))
    def GetCharArrayElements(self, array: jcharArray, isCopy: IPointer[jboolean]) -> IPointer[int]: ...
    
    @vt.function(PTR(jshort), jshortArray, PTR(jboolean))
    def GetShortArrayElements(self, array: jshortArray, isCopy: IPointer[jboolean]) -> IPointer[int]: ...
    
    @vt.function(PTR(jint), jintArray, PTR(jboolean))
    def GetIntArrayElements(self, array: jintArray, isCopy: IPointer[jboolean]) -> IPointer[int]: ...
    
    @vt.function(PTR(jlong), jlongArray, PTR(jboolean))
    def GetLongArrayElements(self, array: jlongArray, isCopy: IPointer[jboolean]) -> IPointer[int]: ...
    
    @vt.function(PTR(jfloat), jfloatArray, PTR(jboolean))
    def GetFloatArrayElements(self, array: jfloatArray, isCopy: IPointer[jboolean]) -> IPointer[int]: ...
    
    @vt.function(PTR(jdouble), jdoubleArray, PTR(jboolean))
    def GetDoubleArrayElements(self, array: jdoubleArray, isCopy: IPointer[jboolean]) -> IPointer[int]: ...
    
    
    @vt.function(VOID, jbooleanArray, PTR(jboolean), jint)
    def ReleaseBooleanArrayElements(self, array: jbooleanArray, elems: IPointer[jboolean], mode: int): ...
    
    @vt.function(VOID, jbyteArray, PTR(jbyte), jint)
    def ReleaseByteArrayElements(self, array: jbyteArray, elems: IPointer[jbyte], mode: int): ...
    
    @vt.function(VOID, jcharArray, PTR(jchar), jint)
    def ReleaseCharArrayElements(self, array: jcharArray, elems: IPointer[jchar], mode: int): ...
    
    @vt.function(VOID, jshortArray, PTR(jshort), jint)
    def ReleaseShortArrayElements(self, array: jshortArray, elems: IPointer[jshort], mode: int): ...
    
    @vt.function(VOID, jintArray, PTR(jint), jint)
    def ReleaseIntArrayElements(self, array: jintArray, elems: IPointer[jint], mode: int): ...
    
    @vt.function(VOID, jlongArray, PTR(jlong), jint)
    def ReleaseLongArrayElements(self, array: jlongArray, elems: IPointer[jlong], mode: int): ...
    
    @vt.function(VOID, jfloatArray, PTR(jfloat), jint)
    def ReleaseFloatArrayElements(self, array: jfloatArray, elems: IPointer[jfloat], mode: int): ...
    
    @vt.function(VOID, jdoubleArray, PTR(jdouble), jint)
    def ReleaseDoubleArrayElements(self, array: jdoubleArray, elems: IPointer[jdouble], mode: int): ...
    
    # 16 Get/Set T ArrayRegion
    vt.skip_count(16)
    
    
    @vt.function(jint, jclass, JNINativeMethod.PTR(), jint)
    def RegisterNatives(self, clazz: jclass, methods: IPointer[JNINativeMethod], nMethods: int) -> int: ...
    
    @vt.function(jint, jclass)
    def UnregisterNatives(self, clazz: jclass) -> int: ...
    
    
    @vt.function(jint, jobject)
    def MonitorEnter(self, obj: jobject) -> int: ...
    
    @vt.function(jint, jobject)
    def MonitorExit(self, obj: jobject) -> int: ...
    
    
    @vt.function(jint, PVOID)
    def GetJavaVM(self, vm: IDoublePtr['JavaVM']) -> int: ...
    
    # GetString(UTF)Region
    vt.skip_count(2)
    
    # Get/ReleasePrimitiveArrayCritical
    vt.skip_count(2)
    
    # Get/ReleaseStringCritical
    vt.skip_count(2)
    
    
    @vt.function(jweak, jobject)
    def NewWeakGlobalRef(self, obj: jobject) -> jweak: ...
    
    @vt.function(VOID, jweak)
    def DeleteWeakGlobalRef(self, ref: jweak): ...
    
    
    @vt.function(jboolean)
    def ExceptionCheck(self) -> int: ...
    
    # 3 DirectBuffer manipulation
    vt.skip_count(3)
    
    
    # New JNI 1.6 Features
    @vt.function(jobjectRefType, jobject)
    def GetObjectRefType(self, obj: jobject) -> int: ...
    
    
    # Module Features
    @vt.function(jobject, jclass)
    def GetModule(self, clazz: jclass) -> jobject: ...
    
    
    # Virtual threads
    @vt.function(jboolean, jobject)
    def IsVirtualThread(self, obj: jobject) -> int: ...
    
    _fields_ = vt.build()

class JavaVMOption(CStructure):
    _fields_ = [
        ('optionString', LPSTR),
        ('extraInfo', PVOID)
    ]
    
    optionString: bytes
    extraInfo: int
    
class JavaVMInitArgs(CStructure):
    _fields_ = [
        ('version', jint),
        
        ('nOptions', jint),
        ('options', JavaVMOption.PTR()),
        ('ignoreUnrecognized', jboolean)
    ]
    
    options: IPointer[JavaVMOption]
    ignoreUnrecognized: int
    nOptions: int
    version: int
    
class JavaVMAttachArgs(CStructure):
    _fields_ = [
        ('version', jint),
        ('name', LPSTR),
        ('group', jobject)
    ]
    
    group: jobject
    version: int
    name: bytes

class JavaVM(CStructure):
    vt = VirtualTable('JavaVM')
    
    # reserved 0-2
    vt.skip_count(3)
    
    @vt.function(jint)
    def DestroyJavaVM(self) -> int: ...
    
    @vt.function(jint, PVOID, PVOID)
    def AttachCurrentThread(self, penv: IDoublePtr[JNIEnv], args: IPointer[JavaVMInitArgs]) -> int: ...
    
    @vt.function(jint)
    def DetachCurrentThread(self) -> int: ...
    
    @vt.function(jint, PVOID, jint)
    def GetEnv(self, penv: IDoublePtr[JNIEnv], version: int) -> int: ...
    
    @vt.function(jint, PVOID, PVOID)
    def AttachCurrentThreadAsDaemon(self, penv: IDoublePtr[JNIEnv], args: IPointer[JavaVMAttachArgs]) -> int: ...
    
    _fields_ = vt.build()
    
JNI_VERSION_1_1 = 0x00010001
JNI_VERSION_1_2 = 0x00010002
JNI_VERSION_1_4 = 0x00010004
JNI_VERSION_1_6 = 0x00010006
JNI_VERSION_1_8 = 0x00010008
JNI_VERSION_9   = 0x00090000
JNI_VERSION_10  = 0x000a0000
JNI_VERSION_19  = 0x00130000
JNI_VERSION_20  = 0x00140000
JNI_VERSION_21  = 0x00150000

JVM_ACC_PUBLIC        = 0x0001
JVM_ACC_PRIVATE       = 0x0002
JVM_ACC_PROTECTED     = 0x0004
JVM_ACC_STATIC        = 0x0008
JVM_ACC_FINAL         = 0x0010
JVM_ACC_SYNCHRONIZED  = 0x0020
JVM_ACC_SUPER         = 0x0020
JVM_ACC_VOLATILE      = 0x0040
JVM_ACC_BRIDGE        = 0x0040
JVM_ACC_TRANSIENT     = 0x0080
JVM_ACC_VARARGS       = 0x0080
JVM_ACC_NATIVE        = 0x0100
JVM_ACC_INTERFACE     = 0x0200
JVM_ACC_ABSTRACT      = 0x0400
JVM_ACC_STRICT        = 0x0800
JVM_ACC_SYNTHETIC     = 0x1000
JVM_ACC_ANNOTATION    = 0x2000
JVM_ACC_ENUM          = 0x4000
JVM_ACC_MODULE        = 0x8000