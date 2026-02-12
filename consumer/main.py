from mysql_connection import cursor, cnx
from mysql_connection import use_db, create_tables
from mysql_connection import insert_customers, insert_orders
from kafka_consumer import total_tables


if __name__ == "__main__":
    use_db(cursor)
    create_tables(cursor)
    insert_customers(total_tables['customers'])
    insert_orders(total_tables['orders'])

    cursor.close()
    cnx.close()