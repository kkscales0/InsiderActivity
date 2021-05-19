import requests
from datetime import datetime
from modules.insideractivity import InsiderActivity
from modules.openinsider import scrape_insider_activity, scrape_insider_activity_for_ticker
from modules.yahoofinance import scrape_stock_prices_on_date, scrape_basic_stock_info
from modules import constant
from bs4 import BeautifulSoup

print(scrape_stock_prices_on_date('LOTZ', datetime.strptime("May 17, 2021", "%b %d, %Y")))
print(scrape_basic_stock_info('LOTZ'))
print(scrape_insider_activity_for_ticker('ATVI', datetime.strptime("May 09, 2021", "%b %d, %Y")))
print(scrape_insider_activity(datetime.strptime("May 09, 2021", "%b %d, %Y")))