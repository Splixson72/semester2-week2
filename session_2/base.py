import sqlite3
# you will need to pip install pandas matplotlib
#--import pandas as pd
#import matplotlib as mpl

def get_connection(db_path="/workspaces/semester2-week2/session_2/orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def main():

    db = get_connection()
    query = '''SELECT * FROM products'''
    cursor = db.execute(query)
    for each in cursor:
        print(each)
    #query = '''SELECT COUNT(customer_id) FROM customers'''
    #cursor = db.execute(query)
    #print(cursor)
    #query = '''SELECT product_id FROM products WHERE price < 2'''
    #db.execute(query)
    #for each in cursor:
    #    print(each)
    db.close()


if __name__=="__main__":
    main()
