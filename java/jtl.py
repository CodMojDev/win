#
# Java Template Library API
#

from ..com.comtl.baseface import *
from .interop import *

import os

def JtlSetJavaHome(javaHome: str):
    os.environ['JAVA_HOME'] = javaHome

def JtlAddClassLoader(classLoader: JObject):
    env = JtlGetEnv()
    JObject._classLoaders.append(env.NewGlobalRef(classLoader._object))

def JtlInitJVM(jvmPath: str = None):
    if jvmPath is None:
        jvmPath = os.environ.get('JAVA_HOME')
        
        if jvmPath is None:
            raise ValueError('JAVA_HOME is not set but no explicit JVM path providen.')
        
    jvmPath = os.path.normpath(jvmPath)
    
    if os.path.isdir(jvmPath):
        jvmPath2 = os.path.join(jvmPath, 'bin\\server\\jvm.dll')
        
        if not os.path.exists(jvmPath2):
            jvmPath2 = os.path.join(jvmPath, 'bin\\client\\jvm.dll')
            
            if not os.path.exists(jvmPath2):
                jvmPath2 = os.path.join(jvmPath, 'jre\\bin\\server\\jvm.dll')
                
                if not os.path.exists(jvmPath2):
                    jvmPath2 = os.path.join(jvmPath, 'jre\\bin\\client\\jvm.dll')
                    
                    if not os.path.exists(jvmPath2):
                        raise RuntimeError('Java JVM.DLL is not found. Pleasy explicitly provide the path to JVM.DLL.')
                    
        jvmPath = jvmPath2
    else:
        if not os.path.exists(jvmPath):
            raise RuntimeError('Incorrect JVM.DLL location.')

        _, name = os.path.split(jvmPath)
        if name.lower() != 'jvm.dll':
            raise RuntimeError('Incorrect JVM.DLL location.')
        
    jvm = get_win_library(jvmPath)
    
    args = JavaVMInitArgs()
    args.version = JNI_VERSION_1_2
    options = TlMakeArray(JavaVMOption)
    args.options = options
    args.nOptions = len(options)
    
    javaVM = JavaVM.NULL()
    env = JNIEnv.NULL()
    
    jCode = jvm.JNI_CreateJavaVM(byref(javaVM), byref(env), args.ref())
    
    if jCode != JNI_OK:
        if jCode == JNI_EEXIST:
            raise RuntimeError('Java VM Initialization failure: JavaVM already initialized and exists.')
        
        if jCode == JNI_ENOMEM:
            raise MemoryError('Java VM Initialization failure: Not enough memory.')
        
        raise RuntimeError('Java VM Initialization failure: Unknown JNI error.')
    
    JObject._javaVM = javaVM.contents
    JObject._env = env.contents
    
    jEnv = env.contents
    java_lang_Class = jEnv.FindClass(b'java/lang/Class')
    JObject._interopCache['Class.getName'] = jEnv.GetMethodID(
        java_lang_Class, b'getName', b'()Ljava/lang/String;')
    JObject._interopCache['Class.isPrimitive'] = jEnv.GetMethodID(
        java_lang_Class, b'isPrimitive', b'()Z')
    JObject._interopCache['Class.isArray'] = jEnv.GetMethodID(
        java_lang_Class, b'isArray', b'()Z')
    JObject._interopCache['Class.getMethods'] = jEnv.GetMethodID(
        java_lang_Class, b'getMethods', b'()[Ljava/lang/reflect/Method;')
    JObject._interopCache['Class.getFields'] = jEnv.GetMethodID(
        java_lang_Class, b'getFields', b'()[Ljava/lang/reflect/Field;')
    JObject._interopCache['Class.forName'] = jEnv.GetStaticMethodID(
        java_lang_Class, b'forName', b'(Ljava/lang/String;ZLjava/lang/ClassLoader;)Ljava/lang/Class;')
    JObject._interopCache['Class.getClassLoader'] = jEnv.GetMethodID(
        java_lang_Class, b'getClassLoader', b'()Ljava/lang/ClassLoader;')
    JObject._interopCache['Class.getConstructors'] = jEnv.GetMethodID(
        java_lang_Class, b'getConstructors', b'()[Ljava/lang/reflect/Constructor;')
    jEnv.DeleteLocalRef(java_lang_Class)
    java_lang_reflect_Method = jEnv.FindClass(b'java/lang/reflect/Method')
    JObject._interopCache['Method.getName'] = jEnv.GetMethodID(
        java_lang_reflect_Method, b'getName', b'()Ljava/lang/String;')
    JObject._interopCache['Method.getReturnType'] = jEnv.GetMethodID(
        java_lang_reflect_Method, b'getReturnType', b'()Ljava/lang/Class;')
    JObject._interopCache['Method.getParameterTypes'] = jEnv.GetMethodID(
        java_lang_reflect_Method, b'getParameterTypes', b'()[Ljava/lang/Class;')
    JObject._interopCache['Method.getModifiers'] = jEnv.GetMethodID(
        java_lang_reflect_Method, b'getModifiers', b'()I')
    jEnv.DeleteLocalRef(java_lang_reflect_Method)
    java_lang_reflect_Field = jEnv.FindClass(b'java/lang/reflect/Field')
    JObject._interopCache['Field.getType'] = jEnv.GetMethodID(
        java_lang_reflect_Field, b'getType', b'()Ljava/lang/Class;')
    JObject._interopCache['Field.getName'] = jEnv.GetMethodID(
        java_lang_reflect_Field, b'getName', b'()Ljava/lang/String;')
    JObject._interopCache['Field.getModifiers'] = jEnv.GetMethodID(
        java_lang_reflect_Field, b'getModifiers', b'()I')
    jEnv.DeleteLocalRef(java_lang_reflect_Field)
    java_lang_Boolean = jEnv.FindClass(b'java/lang/Boolean')
    JObject._interopCache['Boolean.valueOf'] = jEnv.GetStaticMethodID(
        java_lang_Boolean, b'valueOf', b'(Z)Ljava/lang/Boolean;')
    jEnv.DeleteLocalRef(java_lang_Boolean)
    java_lang_Byte = jEnv.FindClass(b'java/lang/Byte')
    JObject._interopCache['Byte.valueOf'] = jEnv.GetStaticMethodID(
        java_lang_Byte, b'valueOf', b'(B)Ljava/lang/Byte;')
    jEnv.DeleteLocalRef(java_lang_Byte)
    java_lang_Character = jEnv.FindClass(b'java/lang/Character')
    JObject._interopCache['Character.valueOf'] = jEnv.GetStaticMethodID(
        java_lang_Character, b'valueOf', b'(C)Ljava/lang/Character;')
    jEnv.DeleteLocalRef(java_lang_Character)
    java_lang_Short = jEnv.FindClass(b'java/lang/Short')
    JObject._interopCache['Short.valueOf'] = jEnv.GetStaticMethodID(
        java_lang_Short, b'valueOf', b'(S)Ljava/lang/Short;')
    jEnv.DeleteLocalRef(java_lang_Short)
    java_lang_Integer = jEnv.FindClass(b'java/lang/Integer')
    JObject._interopCache['Integer.valueOf'] = jEnv.GetStaticMethodID(
        java_lang_Integer, b'valueOf', b'(I)Ljava/lang/Integer;')
    jEnv.DeleteLocalRef(java_lang_Integer)
    java_lang_Long = jEnv.FindClass(b'java/lang/Long')
    JObject._interopCache['Long.valueOf'] = jEnv.GetStaticMethodID(
        java_lang_Long, b'valueOf', b'(J)Ljava/lang/Long;')
    jEnv.DeleteLocalRef(java_lang_Long)
    java_lang_Float = jEnv.FindClass(b'java/lang/Float')
    JObject._interopCache['Float.valueOf'] = jEnv.GetStaticMethodID(
        java_lang_Float, b'valueOf', b'(F)Ljava/lang/Float;')
    jEnv.DeleteLocalRef(java_lang_Float)
    java_lang_Double = jEnv.FindClass(b'java/lang/Double')
    JObject._interopCache['Double.valueOf'] = jEnv.GetStaticMethodID(
        java_lang_Double, b'valueOf', b'(D)Ljava/lang/Double;')
    jEnv.DeleteLocalRef(java_lang_Double)
    java_io_File = jEnv.FindClass(b'java/io/File')
    JObject._interopCache['File.<init>'] = jEnv.GetMethodID(
        java_io_File, b'<init>', b'(Ljava/lang/String;)V')
    JObject._interopCache['File.toURI'] = jEnv.GetMethodID(
        java_io_File, b'toURI', b'()Ljava/net/URI;')
    jEnv.DeleteLocalRef(java_io_File)
    java_net_URI = jEnv.FindClass(b'java/net/URI')
    JObject._interopCache['URI.toURL'] = jEnv.GetMethodID(
        java_net_URI, b'toURL', b'()Ljava/net/URL;')
    jEnv.DeleteLocalRef(java_net_URI)
    java_net_URLClassLoader = jEnv.FindClass(b'java/net/URLClassLoader')
    JObject._interopCache['URLClassLoader.<init>'] = jEnv.GetMethodID(
        java_net_URLClassLoader, b'<init>', b'([Ljava/net/URL;Ljava/lang/ClassLoader;)V')
    jEnv.DeleteLocalRef(java_net_URLClassLoader)
    java_lang_reflect_Constructor = jEnv.FindClass(b'java/lang/reflect/Constructor')
    JObject._interopCache['Constructor.getParameterTypes'] = jEnv.GetMethodID(
        java_lang_reflect_Constructor, b'getParameterTypes', b'()[Ljava/lang/Class;')
    jEnv.DeleteLocalRef(java_lang_reflect_Constructor)
    
    return True

def JtlUnload():
    javaVM = JObject._javaVM
    
    if javaVM:
        jCode = javaVM.DestroyJavaVM()

        if jCode != JNI_OK:
            if jCode == JNI_EDETACHED:
                raise RuntimeError('Unloading JavaVM failure: Java VM detached.')
            
            raise RuntimeError('Unloading Java VM failure: Unknown JNI error.')
        
        JObject._javaVM = None
        JObject._env = None

def JtlGetJavaVM() -> JavaVM:
    return JObject._javaVM

def JtlGetEnv(javaVM: JavaVM = None, jniVersion: int = JNI_VERSION_1_2) -> JNIEnv:
    if javaVM is None:
        javaVM = JObject._javaVM
        
    if javaVM is None:
        raise RuntimeError('JNIEnv* obtaining failure: JavaVM is not initialized.')
    
    env = JNIEnv.NULL()
    jCode = javaVM.GetEnv(byref(env), jniVersion)
    
    if jCode != JNI_OK:
        if jCode == JNI_EDETACHED:
            raise RuntimeError('JNIEnv* obtaining failure: Java VM detached.')
        if jCode == JNI_ENOMEM:
            raise MemoryError('JNIEnv* obtaining failure: Not enough memory.')
        if jCode == JNI_EVERSION:
            raise ValueError('JNIEnv* obtaining failure: Unsupported JNI version.')
        
        raise RuntimeError('JNIEnv* obtaining failure: Unknown JNI error.')
    
    return env.contents