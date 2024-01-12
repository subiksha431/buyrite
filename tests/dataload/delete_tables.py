from openpyxl import load_workbook
import re
import logging
from operator import truediv
import psycopg2
from string import Template
import uuid
import psycopg2.extras
from itertools import zip_longest
import io
import datetime
 
from data_load_utils import DataLoadUtils
from data_load_config import Configuration
from data_load_logging import Logger

class DeleteTables:
    def __init__(self):
        self.logger = Logger.build_logger()
        self.configure = Configuration()
        self.utils = DataLoadUtils()

    def deleting_all_talbles(self):

        self.logger.info("Make sure you know what you are doing!!!")

        total_tables=[]

        conn = self.utils.connection()
        cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cur.execute("select table_name from information_schema.tables where table_schema = 'buyrite' ;")
        rows = cur.fetchall()
        for row in rows:
            total_tables.append(row['table_name'])

        self.logger.info("Total [%s] existing tables [%s]",len(total_tables),total_tables)

        DROP_FILE = self.configure.DROP_FILE


        if len(total_tables) != 0:
            with io.open(DROP_FILE, "r+") as f:
                delete_query = f.read()
                self.logger.info("Running delete_query:[\n%s\n]",delete_query)
                cur.execute(delete_query)
                self.logger.info("Dropped all the tables.")
        else:
            self.logger.info("No tables to delete.")

        cur.close()
        conn.commit()
        conn.close()

        self.logger.info("All tabled deleted.")

if __name__=="__main__":
    DeleteTables().deleting_all_talbles()