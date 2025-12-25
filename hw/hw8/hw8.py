import sqlite3

connect = sqlite3.connect('shop_hw8.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    price INTEGER,
    client_id INTEGER,
    FOREIGN KEY (client_id) REFERENCES clients(id)
    )
''')
connect.commit()

def create_client(name, address):
    cursor.execute(
        'INSERT INTO clients (name, address) VALUES (?, ?)',
        (name, address)
    )

    connect.commit()
    print(f"Клиент добавлен: {name}.")

def create_order(client_id, product, price):
    cursor.execute('INSERT INTO orders (client_id, product, price) VALUES (?, ?, ?)'
                   , (client_id, product, price))
    connect.commit()
    print(f"Заказ добавлен: {product}.")

def show_clients_orders():
    cursor.execute('''
        SELECT clients.name, orders.product, orders.price
        FROM clients
        LEFT JOIN orders ON clients.id = orders.client_id
    ''')
    show_orders = cursor.fetchall()

    for order in show_orders:
        print(f"КЛИЕНТ: {order[0]},     ТОВАР: {order[1]},      ЦЕНА: {order[2]}")

def orders_count():
    cursor.execute('SELECT COUNT(*) FROM orders')
    print(f"Количество заказов: {cursor.fetchone()[0]}")

def avg_price():
    cursor.execute('SELECT AVG(price) FROM orders')
    print(f"Средняя цена: {cursor.fetchone()[0]}")

def max_price():
    cursor.execute('SELECT MAX(price) FROM orders')
    print(f"Максимальная цена: {cursor.fetchone()[0]}")

def min_price():
    cursor.execute('SELECT MIN(price) FROM orders')
    print(f"Минимальная цена: {cursor.fetchone()[0]}")

def sum_price():
    cursor.execute('SELECT SUM(price) FROM orders')
    print(f"Сумма price: {cursor.fetchone()[0]}")

def orders_client():
    cursor.execute("""
        SELECT clients.name, COUNT(orders.id)
        FROM clients
        LEFT JOIN orders ON clients.id = orders.client_id
        GROUP BY clients.id
    """)
    orders = cursor.fetchall()
    for order in orders:
        print(f"КЛИЕНТ: {order[0]},     Заказы: {order[1]}")


def clients_with_product(product_name):
    cursor.execute("""
        SELECT name FROM clients
        WHERE id IN (
            SELECT client_id FROM orders
            WHERE product = ?
        )
    """, (product_name,))
    clients = cursor.fetchall()
    print(f"Клиенты с товаром '{product_name}':")
    for client in clients:
        print(client[0])

def create_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS clients_orders_view AS
        SELECT 
            clients.name,
            orders.product,
            orders.price
        FROM clients
        LEFT JOIN orders ON clients.id = orders.client_id
    """)
    connect.commit()
    print("VIEW создан")

def read_view():
    cursor.execute("SELECT * FROM clients_orders_view")
    orders = cursor.fetchall()
    for order in orders:
        print(order)


create_client("Zara", "Бишкек")
create_client("Mari", "Ош")

create_order(1, "Ноутбук", 120000)
create_order(1, "Мышь", 3000)
create_order(2, "IPhone17pro-max", 80000)

show_clients_orders()
orders_count()
max_price()
avg_price()
orders_client()
clients_with_product("Ноутбук")
create_view()
read_view()
