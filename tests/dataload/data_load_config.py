#!/usr/bin/env python

import logging


class Configuration:

    def __init__(self):

        self.db_host = '127.0.0.1'
        self.db_port = 5432
        self.db_database = 'buyrite'
        self.db_user = 'postgres'
        self.db_password = 'pgadmin'
        
        self.log_format = '[%(filename)s.%(funcName)s().%(levelname)s:] --> %(message)s'
        #self.log_level = logging.INFO

        self.pretty_print_json = True

        self.beer_markup_percentage = 0.02
        self.wine_markup_percentage = 0.05
        self.liquour_markup_percentage = 0.07


        #windows
        #BASE_LOCATION = "D:/buyrite/buyriteapi/"
        #self.SEPERATOR = "\\"

        #mac
        BASE_LOCATION = "/Users/subikshalalita/Documents/buyrite_test/buyriteapi/"
        self.SEPERATOR = "/"


        DATA_FILE_LOCATION = BASE_LOCATION + "tests/dataload/"
        self.DDL_FILE_LOCATION = BASE_LOCATION + "db/ddl/"
        
        self.DML_BASE_PATH = DATA_FILE_LOCATION + "dml-scripts/"

        self.EXCEL_FILE = DATA_FILE_LOCATION  + "Cranbury-Weekly-Movement.xlsx"
        self.STORE_NAME = "Cranbury"

        self.DROP_FILE = self.DDL_FILE_LOCATION  + "drop_all_tables.sql"
