import sqlite3

# A4
connect = sqlite3.connect('users.db')
# рука с карандашом
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR (50) NOT NULL,
            age INTEGER,
            hobby TEXT
        )
''')

connect.commit()

# CRUD - Create Read Update Delete

def create_user(name, age, hobby=None):
    cursor.execute(
        f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")'

        # f'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
        # (name, age, hobby)
    )



    connect.commit()
    print(f"Пользователь добавлен {name}!!")

# create_user("Zuss", 24, "Читать книги")
# create_user("Welma", 19, "Разгадывать тайны")

def get_users():
    # cursor.execute('SELECT * FROM users')
    # cursor.execute('SELECT name, hobby FROM users')

    users = cursor.fetchall()
    # users1 = cursor.fetchmany(2)
    print(users)

    # for i in users:
    #     print(f"NAME: {i[0]} AGE:{i[1]} HOBBY {i[2]}")

# get_users()

def update_user_name(hobby, name):
    cursor.execute(
        'UPDATE users SET name = ? WHERE hobby = ?',
        (name, hobby)

    )
    connect.commit()
    print("Пользователь обновлен!")
update_user_name('Читать книги', 'Cuzco')

