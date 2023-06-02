import mysql.connector


def database_connection(host: str, user: str, password: str, database: str):
    db_con = mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
    )
    cursor = db_con.cursor()
    cursor.execute(f"SHOW DATABASES")
    database_list = cursor.fetchall()

    database_list = [''.join(t) for t in database_list]

    if database not in database_list:
        db_con.cursor().execute(f"CREATE DATABASE {database}")

    db_con.database = database
    return db_con
