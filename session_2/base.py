import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def main():

    db = get_connection()
    cursor = db.execute("SELECT category FROM products")
    for i in range[cursor]
        print(cursor[i])
    cursor = db.execute("SELECT COUNT(customer_id) FROM customers")
    print cursor
    db.execute(SELECT product_id FROM products WHERE price < 2)
    for i in range[cursor]
        print(cursor[i])
    db.close()


if __name__=="__main__":
    main()
