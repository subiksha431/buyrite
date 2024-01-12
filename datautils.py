#!/usr/bin/env python

import uuid
from datetime import datetime
from decimal import Decimal

from buyrite.utils.logging import Logger

logger = Logger.build_logger()


def chunks(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def convert_to_decimal(value):
    return Decimal(value).quantize(Decimal('.000001'))


def convert_to_float(value):
    return float(value)


def convert_to_iso_date(value):
    return value.strftime('%Y-%m-%d')


def new_guid():
    return str(uuid.uuid4()).lower()


def get_date():
    # current date and time .strftime("%d-%m-%Y")
    ingestDate = (datetime.now())
    #ingestDate = now.strftime("%m-%d-%Y")
    return ingestDate


class DbDataReader:

    def __init__(self, columns):
        self.indexes = {}
        for i in range(len(columns)):
            self.indexes[columns[i]] = i

    def get_column_index(self, column_name):
        return self.indexes[column_name] if column_name in self.indexes else None

    def read_date(self, row, column_name):
        index = self.get_column_index(column_name)
        return None if index is None else row[index]

    def read_decimal(self, row, column_name):
        index = self.get_column_index(column_name)
        return None if index is None else row[index]

    def read_guid(self, row, column_name):
        index = self.get_column_index(column_name)
        return None if index is None else row[index]

    def read_int(self, row, column_name):
        index = self.get_column_index(column_name)
        return None if index is None else int(row[index])

    def read_string(self, row, column_name):
        index = self.get_column_index(column_name)
        return None if index is None else str(row[index])

    def read_json(self, row, column_name):
        index = self.get_column_index(column_name)
        return None if index is None else row[index]
