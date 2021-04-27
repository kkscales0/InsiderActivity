from . import constant

class InsiderActivity:
    def __init__(self, filingDate, tradeDate, ticker, companyName,
                 insiderName, title, tradeType, price, quantity,
                 quantityOwned, changeInOwnership, value) -> None:
        self.filingDate = filingDate
        self.tradeDate = tradeDate
        self.ticker = ticker
        self.companyName = companyName
        self.insiderName = insiderName
        self.title = title
        self.tradeType = tradeType
        self.price = price
        self.quantity = quantity
        self.quantityOwned = quantityOwned
        self.changeInOwnership = changeInOwnership
        self.value = value

    def __repr__(self):
        return "Filing Date: %s, Trade Date: %s, Ticker: %s, Co Name: %s, " \
            "Ins Name: %s, Title: %s, Trade Type: %s, Price: %s, " \
            "Qty: %s, QtyOwned: %s, DeltaOwn: %s, Value: %s" \
            % (self.filingDate, self.tradeDate, self.ticker,
            self.companyName, self.insiderName, self.title,
            self.tradeType, self.price, self.quantity,
            self.quantityOwned, self.changeInOwnership, self.value)

    @classmethod
    def FromOpenInsiderTableRow(cls, tableRow):
        rowContents = tableRow.contents
        return cls(
            rowContents[constant.FILING_DATE_COL].get_text(strip=True),
            rowContents[constant.TRADE_DATE_COL].get_text(strip=True),
            rowContents[constant.TICKER_COL].get_text(strip=True),
            rowContents[constant.COMPANY_NAME_COL].get_text(strip=True),
            rowContents[constant.INSIDER_NAME_COL].get_text(strip=True),
            rowContents[constant.TITLE_COL].get_text(strip=True),
            rowContents[constant.TRADE_TYPE_COL].get_text(strip=True),
            rowContents[constant.PRICE_COL].get_text(strip=True),
            rowContents[constant.QUANTITY_COL].get_text(strip=True),
            rowContents[constant.QUANTITY_OWNED_COL].get_text(strip=True),
            rowContents[constant.CHANGE_IN_OWNERSHIP_COL].get_text(strip=True),
            rowContents[constant.VALUE_COL].get_text(strip=True))