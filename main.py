import requests
from modules.insideractivity import InsiderActivity
from modules import constant
from bs4 import BeautifulSoup

NUMBER_OF_ROWS_TO_GET = 5

page = requests.get(f"http://openinsider.com/screener?fd=730&td=0&xp=1sic1=-1&sicl=100&sich=9999&grp=0&sortcol=0&cnt={NUMBER_OF_ROWS_TO_GET}&page=1")
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find("table", class_='tinytable')
headers = table.thead
records = table.tbody

#TODO: Use most recent InsiderActivity object instead of just datetime
mostRecentRecord = "2021-04-20 19:55:14"

for record in records.contents:
    # Every other row is '\n'
    if record == "\n":
        continue

    # Don't want to insert duplicates into the DB
    filingDate = record.contents[constant.FILING_DATE_COL].get_text(strip=True)
    if filingDate <= mostRecentRecord:
        break

    insiderActivity = InsiderActivity.FromOpenInsiderTableRow(record)
    print(insiderActivity)
