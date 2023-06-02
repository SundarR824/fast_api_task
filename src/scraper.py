import pathlib
import sys

cr_path = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(cr_path))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import tables

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chromedriver_path = f"{cr_path}/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path, options=chrome_options)
driver.get("https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx")
time.sleep(7)
page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, "html.parser")
table = soup.find("table", {"id": "ContentPlaceHolder1_gvbulk_deals"})
dct = dict()
for row in table.findAll('tr', attrs={'class': 'tableheading'}):
    for th in row.find_all_next('th'):
        dct[th.text] = list()

whole = list()
data_blocks = table.find_all('tr', class_="tdcolumn")
for block in data_blocks:
    cells = block.find_all("td")
    lst = list()
    for cell in cells:
        cell_text = cell.get_text(strip=True)
        lst.append(cell_text)
    whole.append(lst)

for i in whole:
    dct['Deal Date'].append(i[0])
    dct['Security Code'].append(i[1])
    dct['Security Name'].append(i[2])
    dct['Client Name'].append(i[3])
    dct['Deal Type *'].append(i[4])
    dct['Quantity'].append(i[5])
    dct['Price **'].append(i[6])


def pd_dataframe():
    df = pd.DataFrame(dct)
    for index, rows in df.iterrows():
        tables.insert_records(d_date=rows['Deal Date'], security_code=rows['Security Code'],
                              security_name=rows['Security Name'], client_name=rows['Client Name'],
                              deal_type=rows['Deal Type *'], quantity=rows['Quantity'], price=rows['Price **'])


# query = f"insert into customers (deal_date, security_code, security_name, client_name, deal_type, quantity, price)" \
#         f" values '{row['Deal Date']}', '{row['Security Code']}', '{row['Security Name']}', '{row['Client Name']}'," \
#         f" '{row['Deal Type *']}', '{row['Quantity']}', '{row['Price **']}'"
