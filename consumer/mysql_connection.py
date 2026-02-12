import mysql.connector
from _mysql_connector import errorcode

cnx = mysql.connector.connect(user='root',
                              password='password',
                              host='127.0.0.1')
cursor = cnx.cursor()

DB_NAME = 'suspicious_customers_orders'

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def use_db(cursor):
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

def create_tables(cursor):
    TABLES = {}
    TABLES['customers'] = "CREATE TABLE IF NOT EXISTS customers(" \
    "id int auto increment primery key," \
    "type varchar(20)," \
    "customeNumber int not null," \
    "customerName varchar(100)," \
    "contactLastName varchar(100)," \
    "contactFirstName varchar(100)," \
    "phone varchar (20)," \
    "addressLine1 varchar (100)," \
    "addressLine2 varchar (100)," \
    "city varchar(100)," \
    "state varchar(100)," \
    "postalCode varchar(100)," \
    "country varchar(100)," \
    "salesRepEmployeeNumber varchar(50)," \
    "creditLimit varchar(50))"

    TABLES['orders'] = "CREATE TABLE IF NOT EXISTS orders(" \
    "id int auto increment primery key," \
    "type varchar(20)," \
    "orderNumber int not null," \
    "orderDate varchar(100)," \
    "requiredDate varchar(100)," \
    "shippedDate varchar(100)," \
    "status varchar (20)," \
    "comments varchar (200)," \
    "customerNumber int (100))"

    for table_name in TABLES:
        table_description = TABLES[table_name]
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
        print("OK")


def insert_customers(customers_lst, cursor):
    add_customer = ("INSERT INTO customers "
               "(type, customeNumber, customerName, contactLastName, contactFirstName, phone, addressLine1," \
               "addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    for customer in customers_lst:
        data_customer = customer
        cursor.execute(add_customer, data_customer)
        cnx.commit()


def insert_orders(orders_lst, cursor):
    add_customer = ("INSERT INTO customers "
               "(type, orderNumber, orderDate, requiredDate, shippedDate, status, comments," \
               "customerNumber) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    for order in orders_lst:
        data_order = order
        cursor.execute(add_customer, data_order)
        cnx.commit()
