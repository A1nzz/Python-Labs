import inspect
from constants import *


class Serializer:

    #consts for key words

    TYPE_KW = "type"
    SOURCE_KW = "source"

    CODE_KW = "__code__"
    GLOBALS_KW = functype.__globals__.__name__
    NAME_KW = "__name__"
    DEFAULTS_KW = "__defaults__"
    CLOSURE_KW = functype.__closure__.__name__

    BASES_KW = "__bases__"
    DICT_KW = "__dict__"

    CLASS_KW = "__class__"

    OBJECT_KW = "object"

    @classmethod
    def serialize(cls, obj, is_inner_func=False):
        if type(obj) in (int, float, bool, str, nonetype):
            return obj

        if type(obj) is list:
            return [cls.serialize(o) for o in obj]

        if type(obj) is dict:
            # Since the key in the dictionary can be a hashable object, which will be represented as a non-hashable
            # dictionary, it is easier to represent the dictionary as a list of key-value pairs
            return {cls.TYPE_KW: dict.__name__,
                    cls.SOURCE_KW: [[cls.serialize(item[0]), cls.serialize(item[1])] for item in obj.items()]}

        if type(obj) in (set, frozenset, tuple, bytes, bytearray):
            return {cls.TYPE_KW: type(obj).__name__,
                    cls.SOURCE_KW: cls.serialize([*obj])}

        if type(obj) is complex:
            return {cls.TYPE_KW: complex.__name__,
                    cls.SOURCE_KW: {complex.real.__name__: obj.real,
                                    complex.imag.__name__: obj.imag}}

        if type(obj) is moduletype:
            return {cls.TYPE_KW: moduletype.__name__,
                    cls.SOURCE_KW: obj.__name__}

        if type(obj) is codetype:
            code = {cls.TYPE_KW: codetype.__name__}
            source = {}

            for (key, value) in inspect.getmembers(obj):
                if key in CODE_PROPS:
                    source[key] = cls.serialize(value)

            code.update({cls.SOURCE_KW: source})
            return code

        if type(obj) is celltype:
            return {cls.TYPE_KW: celltype.__name__,
                    cls.SOURCE_KW: cls.serialize(obj.cell_contents)}

        if type(obj) in (staticmethod, classmethod):
            return {cls.TYPE_KW: type(obj).__name__,
                    cls.SOURCE_KW: cls.serialize(obj.__func__, is_inner_func)}

        if inspect.isroutine(obj):
            source = {}

            # Code
            source[cls.CODE_KW] = cls.serialize(obj.__code__)

            # Global vars
            gvars = cls.__get_gvars(obj, is_inner_func)
            source[cls.GLOBALS_KW] = cls.serialize(gvars)

            # Name
            source[cls.NAME_KW] = cls.serialize(obj.__name__)

            # Defaults
            source[cls.DEFAULTS_KW] = cls.serialize(obj.__defaults__)

            # Closure
            source[cls.CLOSURE_KW] = cls.serialize(obj.__closure__)

            return {cls.TYPE_KW: functype.__name__,
                    cls.SOURCE_KW: source}

        elif inspect.isclass(obj):
            source = {}

            # Name
            source[cls.NAME_KW] = cls.serialize(obj.__name__)

            # Bases
            source[cls.BASES_KW] = cls.serialize(tuple(b for b in obj.__bases__ if b != object))

            # Dict
            source[cls.DICT_KW] = cls.__get_obj_dict(obj)

            return {cls.TYPE_KW: type.__name__,
                    cls.SOURCE_KW: source}

        else:
            source = {}

            # Class
            source[cls.CLASS_KW] = cls.serialize(obj.__class__)

            # Dict
            source[cls.DICT_KW] = cls.__get_obj_dict(obj)

            return {cls.TYPE_KW: cls.OBJECT_KW,
                    cls.SOURCE_KW: source}

    @classmethod
    def __get_gvars(cls, func, is_inner_func):
        name = func.__name__
        gvars = {}

        for gvar_name in func.__code__.co_names:
            # Separating the variables that the function needs
            if gvar_name in func.__globals__:

                # Module
                if type(func.__globals__[gvar_name]) is moduletype:
                    gvars[gvar_name] = func.__globals__[gvar_name]

                # Class
                elif inspect.isclass(func.__globals__[gvar_name]):
                    # To prevent recursion, the class in which this method is declared is replaced with the
                    # name of the class. In the future, this name will be replaced by the class type
                    c = func.__globals__[gvar_name]
                    if is_inner_func and name in c.__dict__ and func == c.__dict__[name].__func__:  # !!!!
                        gvars[gvar_name] = c.__name__
                    else:
                        gvars[gvar_name] = c

                # Recursion protection
                elif gvar_name == func.__code__.co_name:
                    gvars[gvar_name] = func.__name__

                else:
                    gvars[gvar_name] = func.__globals__[gvar_name]

        return gvars

    @classmethod
    def __get_obj_dict(cls, obj):
        dct = {item[0]: item[1] for item in obj.__dict__.items()}
        dct2 = {}

        for key, value in dct.items():
            if type(value) not in UNIQUE_TYPES:
                if inspect.isroutine(value):
                    # Recursion protection
                    dct2[cls.serialize(key)] = cls.serialize(value, is_inner_func=True)
                else:
                    dct2[cls.serialize(key)] = cls.serialize(value)

        return dct2
