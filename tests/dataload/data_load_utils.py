import psycopg2
import uuid
import psycopg2.extras
from itertools import zip_longest
import io

from data_load_config import Configuration
from data_load_logging import Logger

class DataLoadUtils:
    def __init__(self):
        self.logger = Logger.build_logger()
        self.configure = Configuration()

    '''logging.basicConfig(
        level=configure.log_level,
        format=configure.log_format)'''
    
    def new_guid(self):
        return(str(uuid.uuid4()).lower())
    #End Function


    def connection(self):
        conn = psycopg2.connect(database = self.configure.db_database, 
                                user=self.configure.db_user, 
                                password=self.configure.db_password,  
                                host=self.configure.db_host, 
                                port=self.configure.db_port
        )
        
        return conn


    def write_dml_stmts_file(self, dml_file , dml_records):
        
        with io.open(dml_file, 'w',encoding='utf-8') as dml_file_io:
            dml_file_io.writelines("%s\n" % stmt for stmt in dml_records)
        #Finished writing
        
        self.logger.info("Created file [%s] with [%s] records",dml_file,len(dml_records))
    #End Function

    def group_elements(self, n, iterable, padvalue='select 1;'):
        return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

    def save_db_list(self, dml_query_list,page_size):
        conn = self.connection()
        cur = conn.cursor()
        chunks = self.group_elements(page_size,dml_query_list)
        
        for chunk in chunks:
            dml_query_chunk = ' '.join(chunk)
            self.logger.info("Running DB Queries [%s] in a shot",len(chunk))
            cur.execute(dml_query_chunk) 
        
        cur.close()
        conn.commit()
        conn.close()
    #end-of-function     