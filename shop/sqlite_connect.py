import sqlite3
conn=sqlite3.connect("sqlite.db")

cursor = conn.cursor()
cursor.execute("""
    Create table products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        slug TEXT UNIQUE NOT NULL,
        description TEXT,
        image BLOB
    )
""")

# Insert the product data into the database
with open('static/image1.jpg', 'rb') as file:
    image_data = file.read()

cursor = conn.cursor()
cursor.execute("INSERT INTO products (id, name, price, slug, description, image) VALUES (?, ?, ?, ?, ?, ?)", 
               ('Smartphone Case', 19.99, 'smartphone-case', 'Protective case for smartphones.', image_data))
conn.commit()

with open('static/image2.jpg', 'rb') as file:
    image_data = file.read()

cursor.execute("INSERT INTO products (id, name, price, slug, description, image) VALUES (?, ?, ?, ?, ?, ?)", 
               ('Bluetooth Earbuds', 39.99, 'Bluetooth-earbuds', 'Wireless earbuds with Bluetooth connectivity.', image_data))
conn.commit()

with open('static/image3.jpg', 'rb') as file:
    image_data = file.read()

cursor.execute("INSERT INTO products (id, name, price, slug, description, image) VALUES (?, ?, ?, ?, ?, ?)", 
               ('Smartwatch', 99.99, 'smartwatch', 'Digital watch with fitness and health tracking features.', image_data))
conn.commit()


conn.close()
