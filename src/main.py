import requests
from modules.insideractivity import InsiderActivity
from modules.yahoofinance import get_basic_stock_info, get_stock_prices_on_date
from modules import constant
from bs4 import BeautifulSoup

NUMBER_OF_ROWS_TO_GET = 5

#TODO: Move this to a module
page = requests.get(f"http://openinsider.com/screener?fd=730&td=0&xp=1sic1=-1&sicl=100&sich=9999&grp=0&sortcol=0&cnt={NUMBER_OF_ROWS_TO_GET}&page=1")
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find("table", class_='tinytable')
headers = table.thead
records = table.tbody

#TODO: Use most recent InsiderActivity object already retrieved instead of just string
most_recent_record = "2021-04-20 19:55:14"

for record in records.contents:
    # Every other row is '\n'
    if record == "\n":
        continue

    # Don't want to insert duplicates into the DB
    filing_date = record.contents[constant.FILING_DATE_COL].get_text(strip=True)
    if filing_date <= most_recent_record:
        break

    insider_activity = InsiderActivity.from_open_insider_table_row(record)
    print(insider_activity)

#print(get_stock_prices_on_date('BH', 'May 05, 2021'))
