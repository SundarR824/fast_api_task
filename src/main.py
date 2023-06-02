import pathlib
import sys
cr_path = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(cr_path))

import db_conn
import tables
from fastapi import FastAPI
import scraper

app = FastAPI()


@app.get("/")
def init_fnc():
    db_conn.database_connection(tables.host_nme, "root", "sundar@123", "emp_db")
    # tables.create_user_table()  # creating User table for users
    tables.create_customer_table()  # creating Customer table for scraper list

    return {"message": "Tables Created"}


@app.get("/list")
def user_show():
    try:
        result = tables.show_table_records()
        return {"message": result}
    except Exception as err:
        return {"message": str(err)}


@app.post("/add")
def user_add():
    try:
        tables.insert_records(d_date="01-01-2022", security_code=123, security_name="service", client_name="services",
                              deal_type="new_deal", quantity=234, price=55.6)
        return {"message": "Record added"}

    except Exception as err:
        return {"message": str(err)}


@app.put("/update/{sec_cde}")
def user_update(sec_cde: int):
    try:
        tables.update_records(d_date="01-03-2023", security_code=789, security_name="new_service", client_name="new_services",
                              deal_type="new_deal_1", quantity=567, price=58.9, sec_code=sec_cde)
        return {"message": "user Updated"}

    except Exception as err:
        return {"message": str(err)}


@app.delete("/delete/{u_id}")
def user_delete(u_id: int):
    try:
        tables.delete_records(u_id)
        return {"message": "User Deleted"}
    except Exception as err:
        return {"message": str(err)}


@app.get("/scrape")
def scrape():
    try:
        scraper.pd_dataframe()
        return {'message': 'Scraper done Successfully Please check table'}
    except Exception as err:
        return {'message': str(err)}
