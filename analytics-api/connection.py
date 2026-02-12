from consumer.mysql_connection import cursor
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/analytics/top-customers")
def top_customers():
    query = """SELECT customerName, salesRepEmployeeNumber FROM customers
                SORT BY salesRepEmployeeNumber DESC
                LIMIT 10"""
    cursor.execute(query)
    result = cursor.fetchall()
    return {'top ten': result}


@app.get("/analytics/customers-without-orders")
def customers_without_orders():
    query = """SELECT customerName, salesRepEmployeeNumber FROM customers
                WHERE salesRepEmployeeNumber == null"""
    cursor.execute(query)
    result = cursor.fetchall()
    return {"without-orders": result}


@app.get("/analytics/zero-credit-active-customers")
def zero_credit_active_customers():
    query = """SELECT customers.customerName, orders.status, customers.creditLimit FROM customers
                INNER JOIN orders ON customers.customerNumber = orders.customerNumber
                WHERE customers.creditLimit = 0"""
    cursor.execute(query)
    result = cursor.fetchall()
    return {"zero credits": result}