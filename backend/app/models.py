import sqlite3
from flask import Flask, request, jsonify

def init_db():
    with sqlite3.connect('products.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        img_path TEXT NOT NULL,
        price INTEGER,
        amount INTEGER)
""")
        
        conn.commit()
init_db()
class Book:
    def add_product(self):
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            data = request.get_json()
            for item in data:
                cursor.execute("INSERT INTO products (title, img_path, price, amount) VALUES (?, ?, ?, ?)",
                                (item['title'], item['img_path'], item['price'], item['amount']))

            conn.commit()

    def delete_product(self, id):
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT amount FROM products')
            for product in cursor.fetchall():
                if product == 0:
                    cursor.execute('DELETE FROM products WHERE id=? ', (id, ))

            conn.commit()

    def get_all_products(self ):
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM products')
            dict_products = cursor.fetchall()

            return dict_products
        
