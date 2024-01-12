# LOAD DATA INTO DATA TABLES
GIT - https://bitbucket.org/MettleAdmin/buyriteapi/src/main/


# clone your repository


# create datebase using the file buyriteapi/db/00-datebase.sql 
# create user using the file buyriteapi/db/01-user.sql 
# create schema using the file buyriteapi/db/02-schema.sql 


# create product table using file buyriteapi/db/ddl/04-table.product.sql 
# create product_sales table using file buyriteapi/db/ddl/05-table.product_sales.sql

# change the location for the access of the excel in the file buyriteapi/tests/dataload/data_load_config.py

In that file change the location in the variable " BASE_LOCATION " as per your system
SELECT the " SEPERATOR " as per the operating system of your system

# run below file to drop all the tables
# run file buyriteapi/tests/dataload/delete_tables.py
This deletes all the tables in the database


# run below file to create all the tables
# run file buyriteapi/tests/dataload/create_tables.py
This creates all the tables in the database

# run dml for store , store_user and vendor table
# /buyriteapi/db/dml/01-test.store.sql - for table store - copy the query in the file and run it in pgadmin
# do the same for store_user and vendor


# run below file to insert data into data table
# run file buyriteapi/tests/dataload/data_load_product_tables.py

In this data_load_product_tables.py file, 
There are two functions 
    generate_product_table - for loading the product table
    generate_product_sales_table - for loading the product_sales table 

Run buyriteapi/web/app.py to run the api

Go to postman
# import the buyriteapi/postman/collections.json
# create environment and run api's