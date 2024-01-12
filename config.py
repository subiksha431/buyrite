#!/usr/bin/env python

import logging


class Configuration:

    def __init__(self):
        self.allowed_extensions = {'xlsx'}

        self.cognito_pool_name = 'dev-revise-user-pool'
        self.cognito_pool_id = 'us-east-2_kyScV4Qkh'
        self.cognito_client_id = '7j3kc4gta69e24ggshprjceeh9'
        

        self.db_host = '127.0.0.1'
        self.db_port = 5432
        self.db_database = 'buyrite'
        self.db_user = 'postgres'
        self.db_password = 'pgadmin'
        
        self.log_format = '[%(filename)s.%(funcName)s().%(levelname)s:] --> %(message)s'
        self.log_level = logging.DEBUG

        self.pretty_print_json = True
