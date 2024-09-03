import sqlite3

def check_database_content():
    conn = sqlite3.connect('veritabani.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM konular')
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    # Veritabanı içeriğini yazdır!
    for row in rows:
        for col_name, value in zip(column_names, row):
            print(f"{col_name}: {value}")
        print("\n")

    conn.close()


if __name__ == '__main__':
    check_database_content()