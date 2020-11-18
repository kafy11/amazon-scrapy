import sqlite3

conn = sqlite3.connect("products.db")
curr = conn.cursor()
curr.execute("""create table products_price_hist_tb(
                title TEXT,
                price REAL,
                date_inserted DATE
            )""")