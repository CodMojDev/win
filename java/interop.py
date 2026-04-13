from .jni import *

import functools
import struct
import io

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
                 boundJobject: TUnion[jobject, 'JObject', type['JObject']],
                 static: bool = False):
        self._methodIDinfo = methodIDinfo
        self._jnidescInfo = jnidescInfo
        self._static = static
        self._name = name
        
        if boundJobject is not None:
            if isinstance(boundJobject, JObject):
                self._boundJobject = boundJobject._object
            elif isinstance(boundJobject, type) and issubclass(boundJobject, JObject):
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
            jnidescReprs = JObject.parse_jnidesc_parameters(jnidesc)
            
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
        env = JObject._ensureEnv()
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
            result = JObject.construct(returnTypeJnidesc).from_object(result)
        
        JObject.jni_check_errors()
        
        for i, jnidescRepr in enumerate(jnidescReprs):
            jnidescRepr.deallocate(arguments[i])
        
        return result

class JClassDescriptor:
    def __get__(self, instance, owner: type['JObject']) -> 'JObject':
        env = JObject._ensureEnv()
        clazz = env.GetObjectClass(owner._clazz)
        return JObject.construct('java/lang/Class').from_object(clazz)

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
        
        env = JObject._ensureEnv()
        jnidesc = self.jnidesc
        
        if PtrUtil.is_pointer(argument):
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.IsInstanceOf(argument, jClass)
            env.DeleteLocalRef(jClass)
            return result == JNI_TRUE
        if isinstance(argument, JObject):
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
        env = JObject._ensureEnv()
        
        if isinstance(value, JObject):
            return env.NewLocalRef(value._object)
        
        jnidesc = self.jnidesc
        
        if jnidesc == 'java/lang/String':
            return env.NewString(value, len(value))
        if jnidesc == 'java/lang/Boolean':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JObject._interopCache['Boolean.valueOf'], 
                JNI_TRUE if value else JNI_FALSE, variadic=(jboolean,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Byte':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JObject._interopCache['Byte.valueOf'], 
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
                jClass, JObject._interopCache['Character.valueOf'], 
                value, variadic=(jchar,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Short':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JObject._interopCache['Short.valueOf'], 
                value, variadic=(jshort,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Integer':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JObject._interopCache['Integer.valueOf'], 
                value, variadic=(jint,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Long':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JObject._interopCache['Long.valueOf'], 
                value, variadic=(jlong,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Float':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JObject._interopCache['Float.valueOf'], 
                value, variadic=(jfloat,))
            env.DeleteLocalRef(jClass)
            return result
        if jnidesc == 'java/lang/Double':
            jClass = env.FindClass(jnidesc.encode('ascii'))
            result = env.CallObjectMethod(
                jClass, JObject._interopCache['Double.valueOf'], 
                value, variadic=(jdouble,))
            env.DeleteLocalRef(jClass)
            return result
        
        return value
    
    def deallocate(self, value):
        env = JObject._ensureEnv()
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
        env = JObject._ensureEnv()
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
            jClass = JObject.find_jni_class(descItemType.jnidesc)
            array = env.NewObjectArray(length, jClass, NULL)
            
            for i in range(length):
                marshalled = descItemType.marshal_value(value[i])
                env.SetObjectArrayElement(array, i, marshalled)
                descItemType.deallocate(marshalled)
                
            env.DeleteLocalRef(jClass)
            return array
        elif isinstance(descItemType, JNIDescArrayRepr):
            jClass = JObject.find_jni_class(self.jnidesc[1:])
            array = env.NewObjectArray(length, jClass, NULL)
            
            for i in range(length):
                marshalled = descItemType.marshal_value(value[i])
                env.SetObjectArrayElement(array, i, marshalled)
                descItemType.deallocate(marshalled)
                
            env.DeleteLocalRef(jClass)
            return array
        
    def deallocate(self, value):
        env = JObject._ensureEnv()
        env.DeleteLocalRef(value)
        
    def get_c_type(self):
        return jarray

class JInteropMeta(type):
    _staticMethodsIDCache: dict[str, tuple[str, jmethodID]] = {}
    _staticFieldsIDCache: dict[str, tuple[str, jfieldID]] = {}
    _staticMethods: dict[str, str | set[str]] = {}
    _classLoaders: list[jobject] = []
    
    _nativeName: str = None
    _clazz: jclass = None
    
    def __getattr__(cls, name: str):
        env = JObject._ensureEnv()
        
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
                return env.GetStaticDoubleField(cls._clazz, fieldID)
            if jnidesc[0] == 'L':
                jObject = env.GetStaticObjectField(cls._clazz, fieldID)
                jInteropObject = JObject.construct(jnidesc).from_object(jObject)
                env.DeleteLocalRef(jObject)
                return jInteropObject
            
        if name in cls._staticMethods:
            return JInteropMethod(name, cls._staticMethods[name], cls._staticMethodsIDCache, cls, True)
            
    def __setattr__(cls, name: str, value):
        if name in JObject.__annotations__: return type.__setattr__(cls, name, value)
        env = JObject._ensureEnv()
        
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
                if isinstance(value, JObject):
                    return env.SetStaticObjectField(cls._clazz, fieldID, value._object)
                return env.SetStaticObjectField(cls._clazz, fieldID, value)
            
    def __del__(cls):
        env = JObject._env
        if env:
            if cls._clazz:
                env.DeleteGlobalRef(cls._clazz)
            if cls.__name__ == 'JInteropObject':
                jInteropCls: type[JObject] = cls
                for classLoader in jInteropCls._classLoaders:
                    env.DeleteGlobalRef(classLoader)
                jInteropCls._classLoaders = []

class JObject(metaclass=JInteropMeta):
    """
    Object representing Java class.
    """
    
    _interopCache: dict[str, jmethodID] = {}
    _classLoaders: list['JObject'] = []
    
    _staticMethodsIDCache: dict[str, jmethodID] = {}
    _staticFieldsIDCache: dict[str, jfieldID] = {}
    _methodsIDCache: dict[str, jmethodID] = {}
    _fieldsIDCache: dict[str, jmethodID] = {}
    
    _classesCache: dict[str, type['JObject']] = {}
    
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
    @overload
    def construct(cls, nativeName: str) -> type['JObject']: 
        ...
    
    @classmethod
    @overload
    def construct(cls, interopObject: 'JObject') -> type['JObject']: 
        ...
    
    @classmethod
    def construct(cls, varObject: TUnion[str, 'JObject']) -> type['JObject']:
        is_str = isinstance(varObject, str)
        if is_str:
            varObject = cls.normalize_L_jnidesc(varObject)
            JClass = JObject._classesCache.get(varObject, None)
        else:
            str_value = str(varObject)
            JClass = JObject._classesCache.get(str_value)
        
        if JClass is not None:
            return JClass
        
        env = JObject._ensureEnv()
        
        if is_str:
            clazz = JObject.find_jni_class(varObject)
        else:
            clazz = varObject._object
        
        if not clazz:
            raise ValueError(f'Not existing class "{varObject}".')
        
        jclass_clazz = env.NewGlobalRef(clazz)
        env.DeleteLocalRef(clazz)
        
        class JClass(JObject):
            _nativeName = varObject
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
        
        if is_str:
            JObject._classesCache[varObject] = JClass
            JClass.__name__ = varObject
        else:
            JObject._classesCache[str_value] = JClass
            JClass.__name__ = str_value
        
        JClass.initialize_type()
        
        return JClass
    
    @classmethod
    def from_object(cls, jObject: jobject) -> 'JObject':
        env = JObject._ensureEnv()
        
        instance = cls.__new__(cls)
        instance._object = env.NewGlobalRef(jObject)
        
        return instance
    
    @classmethod
    def load_jars(cls, jar_paths: list[str]):
        ...
    
    def __init__(self, *args):
        env = JObject._ensureEnv()
        jObject = JInteropMethod('<init>', self._methods['<init>'], self._methodsIDCache, self.__class__)(*args)
        self._object = env.NewGlobalRef(jObject)
        env.DeleteLocalRef(jObject)
    
    def __str__(self) -> str:
        env = JObject._ensureEnv()
        strObject = self.toString()
        jStrObject = strObject._object
        stringChars = env.GetStringChars(jStrObject, NULL)
        string = stringChars.value
        env.ReleaseStringChars(jStrObject, stringChars)
        return string
    
    def __repr__(self) -> str:
        env = JObject._ensureEnv()
        jString = env.CallObjectMethod(self._clazz, JObject._interopCache['Class.getName'])
        stringChars = env.GetStringChars(jString, NULL)
        string = stringChars.value
        env.ReleaseStringChars(jString, stringChars)
        return f'<{string} "{str(self)}">'
    
    def __eq__(self, other: 'JObject') -> bool:
        env = JObject._ensureEnv()
        if other is None:
            return env.IsSameObject(self._object, NULL)
        return env.IsSameObject(self._object, other._object)

    def __getattr__(self, name: str):
        env = JObject._ensureEnv()
        
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
                jInteropObject = JObject.construct(jnidesc).from_object(jObject)
                env.DeleteLocalRef(jObject)
                return jInteropObject
            
        if name in self._methods:
            return JInteropMethod(name, self._methods[name], self._methodsIDCache, self)
            
    def __del__(self):
        env = JObject._env
        if env:
            if self._object:
                env.DeleteGlobalRef(self._object)
            
    def __setattr__(self, name: str, value):
        if name in JObject.__annotations__: return object.__setattr__(self, name, value)
        env = JObject._ensureEnv()
        
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
                return env.SetCharField(self._object, fieldID, value)
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
                if isinstance(value, JObject):
                    return env.SetObjectField(self._object, fieldID, value._object)
                return env.SetObjectField(self._object, fieldID, value)
        
    @classmethod
    def jni_check_errors(cls):
        env = JObject._ensureEnv()
        
        if env.ExceptionCheck():
            env.ExceptionDescribe()
            env.ExceptionClear()
            raise RuntimeError('JNI/Java Exception.')
        
    @classmethod
    def initialize_type(cls):
        env = JObject._ensureEnv()
        
        interopCache = JObject._interopCache
        jMethods = env.CallObjectMethod(cls._clazz, interopCache['Class.getMethods'])
        JObject.jni_check_errors()
        nMethods = env.GetArrayLength(jMethods)
        
        JObject.jni_check_errors()
        
        for iMeth in range(nMethods):
            jMethod = env.GetObjectArrayElement(jMethods, iMeth)
            jParameterTypes = env.CallObjectMethod(jMethod, interopCache['Method.getParameterTypes'])
            JObject.jni_check_errors()
            nParameterTypes = env.GetArrayLength(jParameterTypes)
            
            jnidesc = '('
            for iParamType in range(nParameterTypes):
                jParameterType = env.GetObjectArrayElement(jParameterTypes, iParamType)
                jnidesc += cls.jclass_to_jnidesc(jParameterType)
                env.DeleteLocalRef(jParameterType)
            jnidesc += ')'
            env.DeleteLocalRef(jParameterTypes)
            
            jReturnType = env.CallObjectMethod(jMethod, interopCache['Method.getReturnType'])
            JObject.jni_check_errors()
            jReturnTypeJnidesc = cls.jclass_to_jnidesc(jReturnType)
            jnidesc += jReturnTypeJnidesc
            env.DeleteLocalRef(jReturnType)
            
            jMethodName = env.CallObjectMethod(jMethod, interopCache['Method.getName'])
            JObject.jni_check_errors()
            methNameChars = env.GetStringChars(jMethodName, NULL)
            methodName = methNameChars.value
            env.ReleaseStringChars(jMethodName, methNameChars)
            env.DeleteLocalRef(jMethodName)
            
            jModifiers = env.CallIntMethod(jMethod, interopCache['Method.getModifiers'])
            JObject.jni_check_errors()
            
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
        JObject.jni_check_errors()
        nFields = env.GetArrayLength(jFields)
        
        for iField in range(nFields):
            jField = env.GetObjectArrayElement(jFields, iField)
            jFieldType = env.CallObjectMethod(jField, interopCache['Field.getType'])
            JObject.jni_check_errors()
            jnidesc = cls.jclass_to_jnidesc(jFieldType)
            jFieldName = env.CallObjectMethod(jField, interopCache['Field.getName'])
            JObject.jni_check_errors()
            fieldNameChars = env.GetStringChars(jFieldName, NULL)
            fieldName = fieldNameChars.value
            env.ReleaseStringChars(jFieldName, fieldNameChars)
            env.DeleteLocalRef(jFieldName)
            env.DeleteLocalRef(jFieldType)
            
            jModifiers = env.CallIntMethod(jField, interopCache['Field.getModifiers'])
            JObject.jni_check_errors()
            
            if jModifiers & JVM_ACC_STATIC:
                cls._staticFieldsIDCache[fieldName] = (jnidesc, env.GetStaticFieldID(cls._clazz, fieldName.encode('ascii'), jnidesc.encode('ascii')))
            else:
                cls._fieldsIDCache[fieldName] = (jnidesc, env.GetFieldID(cls._clazz, fieldName.encode('ascii'), jnidesc.encode('ascii')))
            
            env.DeleteLocalRef(jField)
        
        env.DeleteLocalRef(jFields)
        
        jConstructors = env.CallObjectMethod(cls._clazz, interopCache['Class.getConstructors'])
        JObject.jni_check_errors()
        nConstructors = env.GetArrayLength(jConstructors)
        
        for iCtor in range(nConstructors):
            jConstructor = env.GetObjectArrayElement(jConstructors, iCtor)
            jParameterTypes = env.CallObjectMethod(jConstructor, interopCache['Constructor.getParameterTypes'])
            JObject.jni_check_errors()
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
        env = JObject._ensureEnv()
        
        jName = env.CallObjectMethod(clazz, cls._interopCache['Class.getName'])
        chars = env.GetStringChars(jName, NULL)
        name = chars.value
        env.ReleaseStringChars(jName, chars)
        env.DeleteLocalRef(jName)
        
        JObject.jni_check_errors()
        
        jIsPrimitive = env.CallBooleanMethod(clazz, cls._interopCache['Class.isPrimitive'])
        
        JObject.jni_check_errors()
        
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
        
        jIsArray = env.CallBooleanMethod(clazz, cls._interopCache['Class.isArray'])
        
        JObject.jni_check_errors()
        
        if jIsArray == JNI_TRUE:
            JObject.jni_check_errors()
            return name.replace('.', '/')
        
        JObject.jni_check_errors()
        
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
        env = JObject._ensureEnv()
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
        jClassName = env.NewString(nativeName.replace('/', '.'), len(nativeName))
        jClass = env.FindClass(b'java/lang/Class')
        for classLoader in cls._classLoaders:
            clazz = env.CallStaticObjectMethod(
                jClass, JObject._interopCache['Class.forName'],
                jClassName, JNI_TRUE, classLoader, variadic=(jstring, jboolean, jobject))
            if env.ExceptionCheck():
                env.ExceptionDescribe()
                env.ExceptionClear()
                continue
            env.DeleteLocalRef(jClassName)
            env.DeleteLocalRef(jClass)
            return clazz
        env.DeleteLocalRef(jClassName)
        env.DeleteLocalRef(jClass)
        raise RuntimeError(f'Not found class {nativeName}.')
    
class CONSTANT:
    Class = 7
    Fieldref = 9
    Methodref = 10
    InterfaceMethodref = 11
    String = 8
    Integer = 3
    Float = 4
    Long = 5
    Double = 6
    NameAndType = 12
    Utf8 = 1
    MethodHandle = 15
    MethodType = 16
    InvokeDynamic = 18
    
class ClassBuilder:
    nInterfaces_pos: int
    nConstants_pos: int
    nMethods_pos: int
    nFields_pos: int
    
    def __init__(self, classfile: str | io.IOBase):
        if isinstance(classfile, str):
            self.classfile = open(classfile, 'wb+')
        else:
            self.classfile = classfile
        self.classfile.seek(0)
        self.classfile.truncate()
        
        # Java header
        self.writeu4(0xCAFEBABE)
        
        # JVM Class v45.3
        self.writeu2(3)
        self.writeu2(45)
        
        self.nConstants_pos = self.classfile.tell()
        self.writeu2(1)
        
    def write(self, byteValue: bytes, position: int = None):
        if position is None:
            previousPosition = position = self.classfile.tell()
        else:
            previousPosition = self.classfile.tell()
        if previousPosition != position:
            self.classfile.seek(position)
        self.classfile.write(byteValue)
        if previousPosition != position:
            self.classfile.seek(previousPosition)
    
    def writeu1(self, u1: int, position: int = None):
        self.write(struct.pack('>B', u1), position)
    
    def writeu2(self, u2: int, position: int = None):
        self.write(struct.pack('>H', u2), position)
        
    def writeu4(self, u2: int, position: int = None):
        self.write(struct.pack('>I', u2), position)
        
    def writeu8(self, u2: int, position: int = None):
        self.write(struct.pack('>Q', u2), position)
    
    def read(self, size: int, position: int = None):
        if position is None:
            previousPosition = position = self.classfile.tell()
        else:
            previousPosition = self.classfile.tell()
        if previousPosition != position:
            self.classfile.seek(position)
        result = self.classfile.read(size)
        if previousPosition != position:
            self.classfile.seek(previousPosition)
        return result
    
    def readu1(self, position: int = None):
        return struct.unpack('>B', self.read(1, position))[0]
    
    def readu2(self, position: int = None):
        return struct.unpack('>H', self.read(2, position))[0]
    
    def readu4(self, position: int = None):
        return struct.unpack('>I', self.read(4, position))[0]
    
    def readu8(self, position: int = None):
        return struct.unpack('>Q', self.read(8, position))[0]
    
    def new_constant(self) -> int:
        nConstants = self.readu2(self.nConstants_pos)
        self.writeu2(nConstants + 1, self.nConstants_pos)
        return nConstants
    
    def supports_code(self):
        self.CodeAttribute = self.write_const_utf8('Code')
    
    def write_const_utf8(self, string: str) -> int:
        index = self.new_constant()
        self.writeu1(CONSTANT.Utf8)
        self.writeu2(len(string))
        self.write(string.encode('utf-8'))
        return index
    
    def write_const_nameandtype(self, name: str, desc: str) -> int:
        index = self.new_constant()
        nameIndex = self.write_const_utf8(name)
        descIndex = self.write_const_utf8(desc)
        self.writeu1(CONSTANT.NameAndType)
        self.writeu2(nameIndex)
        self.writeu2(descIndex)
        return index
    
    def write_const_methodref(self, name: str, desc: str, clazzIndex: int) -> int:
        index = self.new_constant()
        nameAndTypeIndex = self.write_const_nameandtype(name, desc)
        self.writeu1(CONSTANT.Methodref)
        self.writeu2(clazzIndex)
        self.writeu2(nameAndTypeIndex)
        return index
    
    def write_const_class(self, name: str) -> int:
        nameIndex = self.write_const_utf8(name)
        index = self.new_constant()
        self.writeu1(CONSTANT.Class)
        self.writeu2(nameIndex)
        
        return index
    
    def write_const_method(self, name: str, desc: str) -> tuple[int, int]:
        return self.write_const_utf8(name), self.write_const_utf8(desc)
    
    def write_access_flags(self, accessFlags: int):
        self.writeu2(accessFlags)
        
    def write_this_class(self, classIndex: int):
        self.writeu2(classIndex)
        
    def write_super_class(self, superIndex: int):
        self.writeu2(superIndex)
        
    def begin_interfaces(self):
        self.nInterfaces_pos = self.classfile.tell()
        self.writeu2(0)
        
    def add_interface(self, interfaceIndex: int):
        self.writeu2(self.readu2(self.nInterfaces_pos) + 1, self.nInterfaces_pos)
        self.writeu2(interfaceIndex)
        
    def begin_fields(self):
        self.writeu2(0)
        
    def begin_methods(self):
        self.nMethods_pos = self.classfile.tell()
        self.writeu2(0)
        
    def add_method(self, access_flags: int, nameIndex: int, descIndex: int):
        self.writeu2(self.readu2(self.nMethods_pos) + 1, self.nMethods_pos)
        self.writeu2(access_flags)
        self.writeu2(nameIndex)
        self.writeu2(descIndex)
        self.nCurrentMethodAttributes = self.classfile.tell()
        self.writeu2(0)
        
    def begin_attributes(self):
        self.writeu2(0)
    
    def write_attribute_code(self, code: bytes, maxStack: int, maxLocals: int, 
                             excTable: list[tuple[int, int, int, int]]):
        self.writeu2(self.readu2(self.nCurrentMethodAttributes) + 1, self.nCurrentMethodAttributes)
        self.writeu2(self.CodeAttribute)
        codeLength = len(code)
        excTableLength = len(excTable)
        self.writeu4(8 + codeLength + (excTableLength * 8) + 2)
        self.writeu2(maxStack)
        self.writeu2(maxLocals)
        self.writeu4(codeLength)
        self.write(code)
        for excEntry in excTable:
            startPc, endPc, handlerPc, catchType = excEntry
            self.writeu2(startPc)
            self.writeu2(endPc)
            self.writeu2(handlerPc)
            self.writeu2(catchType)
        self.writeu2(0)
        
class JInteropFlags:
    Override = 0

def JOverride(f): # marker
    return f

def JNISignature(sig: str):
    def _JNISignature(f):
        f._JInteropSignature = sig
        jnidescReprs = JObject.parse_jnidesc_parameters(sig)
        Types = []
        for jnidescRepr in jnidescReprs:
            Types.append(jnidescRepr.get_c_type())
        retType = JObject.parse_jnidesc_parameters('(' + sig.split(')')[-1] + ')')[0].get_c_type()
        callbackType = CALLBACK(retType, Types)
        f._JInteropCallback = callbackType(f)
        def _marshal_func(*f_args):
            arguments = [f._JInteropOwner.from_object(f_args[0])]
            for i, typ in enumerate(Types):
                if typ is jboolean:
                    arguments.append(f_args[i+1] == JNI_TRUE)
                elif arg in (jbyte, jshort, jint, jlong, jfloat, jdouble):
                    arguments.append(f_args[i+1])
                elif arg is jchar:
                    arguments.append(chr(f_args[i+1]))
                else:
                    arguments.append(JObject.construct(jnidescReprs[i].jnidesc).from_object(f_args[i+1]))
            return f(*arguments)
        return functools.wraps(f)(_marshal_func)
    return _JNISignature

def JSignature(*args):
    def _JSignature(f):        
        callbackTypes = [THIS]
        retType = None
        sig = '('
        ret = ''
        
        def add(jnidesc, ctype, i):
            nonlocal ret, sig, callbackTypes, retType
            if i == 0:
                ret = jnidesc
                callbackTypes.append(ctype)
            else:
                sig += jnidesc
                retType = ctype
        
        for i, arg in enumerate(args):
            if arg == 'boolean':
                add('Z', jboolean, i)
            elif arg == 'byte':
                add('B', jbyte, i)
            elif arg == 'char':
                add('C', jchar, i)
            elif arg == 'short':
                add('S', jshort, i)
            elif arg == 'int':
                add('I', jint, i)
            elif arg == 'long':
                add('J', jlong, i)
            elif arg == 'float':
                add('F', jfloat, i)
            elif arg == 'double':
                add('D', jdouble, i)
            elif arg == 'void':
                if i != 0:
                    raise ValueError('"void"')
                retType = VOID
                ret = 'V'
            else:
                add('L' + arg.replace('.', '/') + ';', PVOID, i)
        
        sig += ')' + ret
        
        def _marshal_func(*f_args):
            arguments = [f._JInteropOwner.from_object(f_args[0])]
            for i, arg in enumerate(args):
                if arg == 'boolean':
                    arguments.append(f_args[i+1] == JNI_TRUE)
                elif arg in ('byte', 'short', 'int', 'long', 'float', 'double'):
                    arguments.append(f_args[i+1])
                elif arg == 'char':
                    arguments.append(chr(f_args[i+1]))
                else:
                    arguments.append(JObject.construct(arg).from_object(f_args[i+1]))
            return f(*arguments)
        
        f._JInteropSignature = sig
        f._JInteropCallback = CALLBACK(retType, *callbackTypes)(_marshal_func)
        
        return functools.wraps(f)(_marshal_func)
        
    return _JSignature

def JMethod(decl: str, *args):
    def _JMethod(f):
        nonlocal decl
        if args:
            f = JSignature(*args)(f)
        f._JInteropFlags = JVM_ACC_NATIVE
        decl = decl.split(' ')
        
        for value in decl:
            if value == 'public':
                f._JInteropFlags |= JVM_ACC_PUBLIC
            elif value == 'private':
                f._JInteropFlags |= JVM_ACC_PRIVATE
            elif value == 'protected':
                f._JInteropFlags |= JVM_ACC_PROTECTED
            elif value == 'strictfp':
                f._JInteropFlags |= JVM_ACC_STRICT
            elif value == 'synchronized':
                f._JInteropFlags |= JVM_ACC_SYNCHRONIZED
            elif value == 'abstract':
                f._JInteropFlags &= ~JVM_ACC_NATIVE
                f._JInteropFlags |= JVM_ACC_ABSTRACT
            elif value == 'static':
                f._JInteropFlags |= JVM_ACC_STATIC
            elif value == 'native':
                pass
            else:
                raise ValueError(f'"{value}"')
        return f
    return _JMethod
    
def JClass(decl: str, super=None):
    env = JObject._ensureEnv()
    decl = decl.split(' ')
    
    def _JClass(cls):
        nonlocal super
        cls.__annotations__['_JInteropFlags'] = int
        type.__setattr__(cls, '_JInteropFlags', 0)
        for value in decl[:-1]:
            if value == 'public':
                cls._JInteropFlags |= JVM_ACC_PUBLIC
            elif value == 'private':
                cls._JInteropFlags |= JVM_ACC_PRIVATE
            elif value == 'protected':
                cls._JInteropFlags |= JVM_ACC_PROTECTED
            elif value == 'abstract':
                cls._JInteropFlags |= JVM_ACC_ABSTRACT
            elif value == 'static':
                cls._JInteropFlags |= JVM_ACC_STATIC
            elif value == 'final':
                cls._JInteropFlags |= JVM_ACC_FINAL
            else:
                raise ValueError(f'"{value}"')
        className = decl[-1]
        if super is None:
            super = 'java/lang/Object'
        elif isinstance(super, JObject):
            super = object.__getattribute__(super, '_nativeName')
        elif isinstance(super, JInteropMeta):
            super = type.__getattribute__(super, '_nativeName')
        else:
            super = JObject.normalize_L_jnidesc(super)
        type.__setattr__(cls, '_JInteropSuper', super)
        type.__setattr__(cls, '_JInteropName', JObject.normalize_L_jnidesc(className))
        
        for method in dir(cls):
            meth = getattr(cls, method)
            if JInteropIsMethod(meth):
                if hasattr(meth, '_JInteropOwner'):
                    if JInteropIsOwner(meth, cls):
                        meth._JInteropOwner = cls
                else:
                    meth._JInteropOwner = cls
        
        JInteropParseClass(cls)
        return cls
    return _JClass
    
def JInterface(decl: str, super=None):
    def _JInterface(cls):
        cls = JClass(decl, super)(cls)
        cls._JInteropFlags |= JVM_ACC_INTERFACE
        return cls
    return _JInterface

def JInteropIsMethod(meth):
    return hasattr(meth, '_JInteropFlags')

def JInteropIsOwner(meth, cls):
    return meth._JInteropOwner is cls

def JInteropParseClass(cls):
    clz = io.BytesIO()
    builder = ClassBuilder(clz)
    this = builder.write_const_class(cls._JInteropName)
    javaLangObject = builder.write_const_class('java/lang/Object')
    ctorRef = builder.write_const_methodref('<init>', '()V', javaLangObject)
    initName, initDesc = builder.write_const_method('<init>', '()V')
    callbacks = []
    methods = []
    methodsStr = []
    for method in dir(cls):
        method = getattr(cls, method)
        if JInteropIsMethod(method) and JInteropIsOwner(method, cls):
            meth_desc = builder.write_const_method(method.__name__, method._JInteropSignature)
            methods.append((*meth_desc, method._JInteropFlags))
            methodsStr.append((method.__name__, method._JInteropSignature))
            callbacks.append(method._JInteropCallback)
    super = builder.write_const_class(type.__getattribute__(cls, '_JInteropSuper'))
    builder.supports_code()
    builder.write_access_flags(cls._JInteropFlags)
    builder.write_this_class(this)
    builder.write_super_class(super)
    builder.begin_interfaces()
    builder.begin_fields()
    builder.begin_methods()
    builder.add_method(JVM_ACC_PUBLIC, initName, initDesc)
    # aload_0
    # invokespecial java/lang/Object.<init>()V
    # return
    builder.write_attribute_code(bytes([0x2a, 0xb7, ctorRef, 0xb1]), 2, 0, [])
    for method, desc, access in methods:
        builder.add_method(access, method, desc)
    builder.begin_attributes()
    env = JObject._ensureEnv()
    clz.seek(0)
    content = clz.read()
    print(content)
    buf = create_string_buffer(content)
    nativeName = create_string_buffer(cls._JInteropName.encode('ascii'))
    clazz = env.DefineClass(nativeName, NULL, i_cast(buf, PTR(jbyte)), clz.tell())
    JObject.jni_check_errors()
    nativeMethods = []
    for i, callback in enumerate(callbacks):
        name, desc = methodsStr[i]
        nativeMethods.append(JNINativeMethod(name.encode('ascii'), desc.encode('ascii'), i_cast(callback, PVOID)))
    arrNativeMethods = (JNINativeMethod * len(nativeMethods))(*nativeMethods)
    jCode = env.RegisterNatives(clazz, arrNativeMethods, len(nativeMethods))
    if jCode != JNI_OK:
        clz.close()
        raise RuntimeError('"env.RegisterNatives" failure.')
    clz.close()
    JObject.construct(cls._nativeName)