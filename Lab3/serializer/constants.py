TYPE_FIELD = "TYPE"
VALUE_FIELD = "VALUE"

OBJECT_TYPE_REGEX = "\'([\w\W]+)\'"


CLASS_NAME = "class"
OBJECT_NAME = "object"
DICTIONARY_NAME = "dict"
FUNCTION_NAME = "function"

BASE_NAME = "base"
DATA_NAME = "data"
NAME_FIELD = "__name__"

TYPES_NAMES = [
    "int",
    "float",
    "complex",
    "bool",
    "str",
    "NoneType"

]

ITERABLE_NAMES = [
    "list",
    "tuple",
    "bytes",
    "set"
]

CLASS_ATTRIBUTE_NAMES = ["__class__",
                         "__doc__",
                         "__getattribute__",
                         "__new__",
                         "__setattr__"
]