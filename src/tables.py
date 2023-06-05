import pathlib
import sys
cr_path = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(cr_path))

import db_conn

host_nme = 'localhost'
# host_nme = 'sql_database'


def create_customer_table():
    my_db = db_conn.database_connection(host_nme, "root", "sundar@123", "emp_db")
    cursor = my_db.cursor()

    query = "CREATE TABLE IF NOT EXISTS customers (deal_date VARCHAR(255), security_code INT, security_name VARCHAR(255)," \
            "client_name VARCHAR(255), deal_type VARCHAR(255), quantity VARCHAR(255), price float(10,7))"
    cursor.execute(query)

    my_db.close()


def show_table_records() -> list:
    my_db = db_conn.database_connection(host_nme, "root", "sundar@123", "emp_db")
    cursor = my_db.cursor()

    query = "Select * from customers"
    cursor.execute(query)

    res = list()
    for i in cursor:
        res.append({"deal_date": i[0], "security_code": i[1], "security_name": i[2], "client_name": i[3],
                    "deal_type": i[4], "quantity": i[5], "price": i[6]})

    my_db.close()
    return res


def insert_records(**values):
    my_db = db_conn.database_connection(host_nme, "root", "sundar@123", "emp_db")
    cursor = my_db.cursor()

    query = f"insert into customers (deal_date, security_code, security_name, client_name, deal_type, quantity, price)" \
            f" values {values['d_date'], values['security_code'], values['security_name'], values['client_name'], values['deal_type'], values['quantity'], values['price']}"

    cursor.execute(query)
    my_db.commit()
    my_db.close()


def update_records(**values):
    my_db = db_conn.database_connection(host_nme, "root", "sundar@123", "emp_db")
    cursor = my_db.cursor()

    query = f"update customers SET deal_date='{values['d_date']}', security_code='{values['security_code']}'," \
            f"security_name='{values['security_name']}', client_name='{values['client_name']}'," \
            f"deal_type='{values['deal_type']}', quantity='{values['quantity']}', price='{values['price']}' WHERE " \
            f"security_code = '{values['sec_code']}'"

    cursor.execute(query)
    my_db.commit()
    my_db.close()


def delete_records(value):
    my_db = db_conn.database_connection(host_nme, "root", "sundar@123", "emp_db")
    cursor = my_db.cursor()

    query = f"DELETE FROM customers WHERE security_code = {value}"

    cursor.execute(query)
    my_db.commit()
    my_db.close()

