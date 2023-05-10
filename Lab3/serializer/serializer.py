import inspect
import re
from frozendict import frozendict
from constants import *


class Serializer:
    def serialize(self, obj):
        result = {}

        if inspect.isclass(obj):
            result = self.serialize_class(obj)
            obj_type_string = CLASS_NAME
        else:
            obj_type = type(obj)
            obj_type_string = re.search(OBJECT_TYPE_REGEX, str(obj_type)).group(1)

            if obj_type == dict:
                result = self.serialize_dict(obj)
            elif isinstance(obj, (int, float, complex, bool, str, type(None))) or obj is None:
                result = self.serialize_types(obj)

        result[TYPE_FIELD] = obj_type_string

        return frozendict(result)

    def serialize_types(self, obj):
        result = {VALUE_FIELD: str(obj)}

        return result

    def deserialize_types(self, obj):
        result = object
        if obj[TYPE_FIELD] == TYPES_NAMES[0]:
            result = int(obj[VALUE_FIELD])
        elif obj[TYPE_FIELD] == TYPES_NAMES[1]:
            result = float(obj[VALUE_FIELD])
        elif obj[TYPE_FIELD] == TYPES_NAMES[2]:
            result = complex(obj[VALUE_FIELD])
        elif obj[TYPE_FIELD] == TYPES_NAMES[3]:
            result = (obj[VALUE_FIELD] == "True")
        elif obj[TYPE_FIELD] == TYPES_NAMES[5]:
            result = None
        else:
            result = obj[VALUE_FIELD]

        return result

    def serialize_dict(self, obj: dict):
        result = {VALUE_FIELD: {}}

        for key, value in obj.items():
            result_key = self.serialize(key)
            result_value = self.serialize(value)

            result[VALUE_FIELD][result_key] = result_value
        return result

    def deserialize_dict(self, obj):
        result = {}

        if type(obj[VALUE_FIELD]) == tuple:
            return {}

        for key, value in obj[VALUE_FIELD].items():
            result_key = self.deserialize(key)
            result_value = self.deserialize(value)
            result[result_key] = result_value

        return result

    def serialize_class(self, obj):
        result = {VALUE_FIELD: {}}
        members = []
        bases = []

        for base in obj.__bases__:
            if base.__name__ != OBJECT_NAME:
                bases.append(base)
        result[VALUE_FIELD][self.serialize(BASE_NAME)] = self.serialize(bases)

        for member in inspect.getmembers(obj):
            if member[0] not in CLASS_ATTRIBUTE_NAMES:
                members.append(member)

        result_data = self.serialize(DATA_NAME)

        new_dict = {NAME_FIELD: obj.__name__}

        for member in members:
            new_dict[member[0]] = member[1]

        result[VALUE_FIELD][result_data] = self.serialize(new_dict)

        return result
