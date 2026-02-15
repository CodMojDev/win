#
# Deprecated
#

raise RuntimeError()

if False:
    class ClassNotRegisteredError(Exception):
        pass

    class ClassAlreadyRegisteredError(Exception):
        pass

    class ClassRegistrationError(Exception):
        pass

    class ClassUnregistrationError(Exception):
        pass