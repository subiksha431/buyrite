import psycopg2
import psycopg2.extras
import io
import glob
 
from data_load_utils import DataLoadUtils
from data_load_config import Configuration
from data_load_logging import Logger

class CreateTables:
    def __init__(self):
        self.logger = Logger.build_logger()
        self.configure = Configuration()
        self.utils = DataLoadUtils()

    def creating_all_talbles(self):

        DDL_LOCATION = self.configure.DDL_FILE_LOCATION
        SEPERATOR = self.configure.SEPERATOR

        conn = self.utils.connection()
        cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        self.logger.info("Creating tables required for buyrite accounts tracker platform.")

        SQL_FILE_FILTER = (DDL_LOCATION+"*.sql")
        sql_file_names_list = []

        for create_file_path in glob.glob(SQL_FILE_FILTER):
            file_name = create_file_path.split(SEPERATOR).pop()
            if "drop_all_tables.sql" != file_name:
                sql_file_names_list.append(file_name)
            #drop file check
        #Finshed files
        
        self.logger.info("sql_file_names_list[%s]",sql_file_names_list.sort(reverse=False))
        for file_name in sql_file_names_list:
            create_file_path = (DDL_LOCATION + file_name)
            self.logger.info("Executing file:[%s]",file_name)
            with io.open(create_file_path, "r+") as f:
                create_table_query = f.read()
                cur.execute(create_table_query)

        #Finshed files
        cur.close()
        conn.commit()
        conn.close()

    #End Function

if __name__=="__main__":
    CreateTables().creating_all_talbles()