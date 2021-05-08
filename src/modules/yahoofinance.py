import requests
from bs4 import BeautifulSoup
from . import constant


def get_basic_stock_info(ticker):
    """Returns sector, industry, and description about passed ticker
    
    Arguments:
    ticker -- stock ticker (ex: 'AAPL')
    """

    url = f"https://finance.yahoo.com/quote/{ticker}/profile"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    profile_section = soup.find("div", class_='asset-profile-container')
    if (profile_section is None):
        print(f'Couldn\'t load profile section from url={url}')
        return False

    sector_tag = profile_section.find('span', text='Sector(s)')
    if (sector_tag is None):
        print(f'Couldn\'t find span with text=Sector(s) at url={url}')
        return False

    sector = sector_tag.findNext('span').get_text(strip=True)

    industry_tag = profile_section.find('span', text='Industry')
    if (industry_tag is None):
        print(f'Couldn\'t find span with text=Industry at url={url}')
        return False

    industry = industry_tag.findNext('span').get_text(strip=True)

    print(sector, ' - ', industry)

    description_section = soup.find(class_='quote-sub-section')
    if (description_section is None):
        print(f'Couldn\'t load description section from url={url}')
        return False

    description = description_section.findNext('p').get_text(strip=True)

    print(description)
    return True

def get_stock_prices_on_date(ticker, date):
    """Returns open and close price for ticker passed on date passed
    
    Arguments:
    ticker -- stock ticker (ex: 'AAPL')
    date -- date to find data for (format Mmm dd, yyyy ex: 'May 05, 2021')
    """
    
    url = f"https://finance.yahoo.com/quote/{ticker}/history"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    table = soup.find('table')
    if (table is None):
        print(f'Couldn\'t load price table from url={url}')
        return False

    date_span = table.find('span', text=date)
    if (date_span is None):
        print(f'Couldn\'t find row for date={date} at url={url}')
        return False

    date_row_list = list(date_span.findParent('tr'))
    if (date_row_list is None or len(date_row_list) < constant.YF_TOTAL_COL):
        print(f'Couldn\'t find tr parent or there aren\'t enough columns in the table, for date={date} at url={url}')
        return False
    

    open_price = date_row_list[constant.YF_OPEN_COL].get_text(strip=True)
    close_price = date_row_list[constant.YF_CLOSE_COL].get_text(strip=True)

    print('open: ', open_price, ' close: ', close_price)
    return True