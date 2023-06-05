from requests_html import HTMLSession

session = HTMLSession()

reqst = session.get('https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx')

print(reqst.text)
