#!/usr/bin/env python

import datetime
import decimal
import json

from buyrite.api.model.base import ApiModelABC
from buyrite.utils.config import Configuration


class JsonDeserializer:

    @classmethod
    def read_json_date(cls, obj, key):
        return obj[key] if key in obj else None

    @classmethod
    def read_json_decimal(cls, obj, key):
        return obj[key] if key in obj else None

    @classmethod
    def read_json_int(cls, obj, key):
        return int(obj[key]) if key in obj else None

    @classmethod
    def read_json_string(cls, obj, key):
        return str(obj[key]) if key in obj else None

    @classmethod
    def read_json_json_array(cls, obj, key):
        return obj[key] if key in obj else None


class JsonSerializer:

    @classmethod
    def serialize(cls, obj) -> str:
        obj = cls.to_json(obj)
        config = Configuration()

        if config.pretty_print_json:
            return json.dumps(obj, sort_keys=True, default=str, indent=4)
        else:
            return json.dumps(obj, sort_keys=True, default=str)

    @classmethod
    def to_json(cls, obj):
        if isinstance(obj, ApiModelABC):
            result = {}

            for attr in vars(obj):
                attr_value = getattr(obj, attr)

                # zero and False are excluded if we check "if attr_value:"
                if attr_value is not None:
                    result[attr] = cls.to_json(attr_value)

            return result

        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')

        elif isinstance(obj, decimal.Decimal):
            # This is a workaround for: http://bugs.python.org/issue16535
            # return '{:.2f}'.format(float(obj))
            return float(obj)

        elif isinstance(obj, list):
            return [cls.to_json(x) for x in obj]

        else:
            return obj
