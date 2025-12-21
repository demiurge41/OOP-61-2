import sqlite3

# A4
connect = sqlite3.connect('films.db')
# рука с карандашом
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS film(
            name VARCHAR (50) NOT NULL,
            release_year INTEGER,
            rating INTEGER
        )
''')

connect.commit()

# CRUD - Create Read Update Delete

def create_film(name, release_year, rating):
    cursor.execute(
        'INSERT INTO film(name, release_year, rating) VALUES(?, ?, ?)',
        (name, release_year, rating)

    )
    connect.commit()
    print(f"Фильм добавлен {name}!!")

# create_film("The Babysitters", 1994, "7")
# create_film("Harry Potter", 2001, "9")
# create_film("Nanny McPhee", 2005, "6")
# create_film("Armour of God", 1986, "8")

def get_films():
    cursor.execute('SELECT * FROM film')
    films = cursor.fetchall()
    print(f"Фильмы:")
    for i in films:
        print(f"NAME: {i[0]} AGE:{i[1]} HOBBY {i[2]}")

# get_films()

def update_film_name(row_id, new_name):
    cursor.execute(
        'UPDATE film SET name = ? WHERE rowid = ?',
        (new_name, row_id)
    )
    connect.commit()
    print("Название фильма обновлено")

# update_film_name(1, "Няньки")


def delete_film(row_id):
    cursor.execute(
        'DELETE FROM film WHERE rowid = ?',
        (row_id,)

    )
    connect.commit()
    print("ПОЛЬЗОВАТЕЛЬ УДАЛЕН!")
# delete_film(2)

def get_by_rowid(row_id):
    cursor.execute(
      'SELECT rowid, name, release_year, rating FROM film WHERE rowid = ?',
        (row_id,)
    )
    film = cursor.fetchone()
    print(f"Фильм: {row_id}")
    print(film)

get_by_rowid(3)
