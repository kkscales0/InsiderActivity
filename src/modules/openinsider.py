import requests
from bs4 import BeautifulSoup
from . import constant
from .insideractivity import InsiderActivity
from datetime import date

NUMBER_OF_ROWS_TO_GET = 5 #max=5000

def scrape_insider_activity_for_ticker(ticker: str, from_date: date) -> None:
    today = date.today()
    page = requests.get(f"http://openinsider.com/screener?s={ticker}&fd=730" \
        f"&td=-1&tdr={from_date.month}%2F{from_date.day}%2F{from_date.year}" \
        f"+-+{today.month}%2F{today.day + 1}%2F{today.year}&xp=1sic1=-1" \
        f"&sicl=100&sich=9999&grp=0&sortcol=0&cnt={NUMBER_OF_ROWS_TO_GET}" \
        "&page=1")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", class_='tinytable')
    records = table.tbody

    #TODO: Use most recent InsiderActivity object already retrieved instead of just string
    most_recent_record = "2019-04-20 19:55:14"

    for record in records.contents:
        # Every other row is '\n'
        if record == "\n":
            continue

        # Don't want to insert duplicates into the DB
        filing_date = record.contents[constant.FILING_DATE_COL] \
            .get_text(strip=True)
        if filing_date <= most_recent_record:
            break

        insider_activity = InsiderActivity.from_open_insider_row(record, False)
        print(insider_activity)

def scrape_insider_activity(from_date: date) -> None:
    today = date.today()
    page = requests.get(f"http://openinsider.com/screener?fd=730&td=-1" \
        f"&tdr={from_date.month}%2F{from_date.day}%2F{from_date.year}+-+" \
        f"{today.month}%2F{today.day + 1}%2F{today.year}&xp=1sic1=-1" \
        f"&sicl=100&sich=9999&grp=0&sortcol=0&cnt={NUMBER_OF_ROWS_TO_GET}" \
        "&page=1")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", class_='tinytable')
    records = table.tbody

    #TODO: Use most recent InsiderActivity object already retrieved instead of just string
    most_recent_record = "2021-04-20 19:55:14"

    for record in records.contents:
        # Every other row is '\n'
        if record == "\n":
            continue

        # Don't want to insert duplicates into the DB
        filing_date = record.contents[constant.FILING_DATE_COL] \
            .get_text(strip=True)
        if filing_date <= most_recent_record:
            break

        insider_activity = InsiderActivity.from_open_insider_row(record, True)
        print(insider_activity)