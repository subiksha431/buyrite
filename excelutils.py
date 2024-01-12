#!/usr/bin/env python


class ExcelReader:

    @classmethod
    def read_excel_date(cls, key):
        return key if key else None

    @classmethod
    def read_excel_decimal(cls, key):
        return key if key else None

    @classmethod
    def read_excel_string(cls, key):
        return str(key) if key else None
