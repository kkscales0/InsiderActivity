import requests
from bs4 import BeautifulSoup
from . import constant


def GetBasicStockInfo(ticker):
    """Returns sector, industry, and description about passed ticker
    
    Arguments:
    ticker -- stock ticker (ex: 'AAPL')
    """

    url = f"https://finance.yahoo.com/quote/{ticker}/profile"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    profileSection = soup.find("div", class_='asset-profile-container')
    if (profileSection is None):
        print(f'Couldn\'t load profile section from url={url}')
        return False

    sectorTag = profileSection.find('span', text='Sector(s)')
    if (sectorTag is None):
        print(f'Couldn\'t find span with text=Sector(s) at url={url}')
        return False

    sector = sectorTag.findNext('span').get_text(strip=True)

    industryTag = profileSection.find('span', text='Industry')
    if (industryTag is None):
        print(f'Couldn\'t find span with text=Industry at url={url}')
        return False

    industry = industryTag.findNext('span').get_text(strip=True)

    print(sector, ' - ', industry)

    descriptionSection = soup.find(class_='quote-sub-section')
    if (descriptionSection is None):
        print(f'Couldn\'t load description section from url={url}')
        return False

    description = descriptionSection.findNext('p').get_text(strip=True)

    print(description)
    return True

def GetStockPricesOnDate(ticker, date):
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

    dateSpan = table.find('span', text=date)
    if (dateSpan is None):
        print(f'Couldn\'t find row for date={date} at url={url}')
        return False

    dataRowList = list(dateSpan.findParent('tr'))
    if (dataRowList is None or len(dataRowList) < constant.YF_TOTAL_COL):
        print(f'Couldn\'t find tr parent or there aren\'t enough columns in the table, for date={date} at url={url}')
        return False
    

    openPrice = dataRowList[constant.YF_OPEN_COL].get_text(strip=True)
    closePrice = dataRowList[constant.YF_CLOSE_COL].get_text(strip=True)

    print('open: ', openPrice, ' close: ', closePrice)
    return True