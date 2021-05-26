from __future__ import annotations
from datetime import datetime, date
from . import constant

class InsiderActivity:
    def __init__(self,
                filing_date: datetime,
                trade_date: date,
                ticker: str,
                company_name: str,
                insider_name: str,
                title: str,
                trade_type: str,
                price: float,
                quantity: int,
                quantity_owned: int,
                change_in_ownership: str,
                value: int) -> None:
        self.filing_date = filing_date
        self.trade_date = trade_date
        self.ticker = ticker
        self.company_name = company_name
        self.insider_name = insider_name
        self.title = title
        self.trade_type = trade_type
        self.price = price
        self.quantity = quantity
        self.quantity_owned = quantity_owned
        self.change_in_ownership = change_in_ownership
        self.value = value

    def __repr__(self) -> str:
        return "Filing Date: %s, Trade Date: %s, Ticker: %s, Co Name: %s, " \
            "Ins Name: %s, Title: %s, Trade Type: %s, Price: %s, " \
            "Qty: %s, QtyOwned: %s, DeltaOwn: %s, Value: %s" \
            % (self.filing_date, self.trade_date, self.ticker,
            self.company_name, self.insider_name, self.title,
            self.trade_type, self.price, self.quantity,
            self.quantity_owned, self.change_in_ownership, self.value)

    @classmethod
    def from_open_insider_row(cls,
                             table_row: str,
                             has_company_name: bool) -> InsiderActivity:
        """
        Creates InsiderActivity object using a row from the html table on
        openinsider

        Arguments:
        table_row -- html table row from openinsider
        has_company_name -- indicates if table has company name or not
        it should be false when getting insider activity for a specific ticker
        """
        
        rowContents = table_row.contents
        shift = 0 if has_company_name else -1
        return cls(
            datetime.strptime(
                rowContents[constant.FILING_DATE_COL].get_text(strip=True),
                "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(
                rowContents[constant.TRADE_DATE_COL].get_text(strip=True),
                "%Y-%m-%d"),
            rowContents[constant.TICKER_COL].get_text(strip=True),
            rowContents[constant.COMPANY_NAME_COL].get_text(strip=True) \
                if has_company_name else "N/A",
            rowContents[constant.INSIDER_NAME_COL + shift] \
                .get_text(strip=True),
            rowContents[constant.TITLE_COL + shift].get_text(strip=True),
            rowContents[constant.TRADE_TYPE_COL + shift].get_text(strip=True),
            float(rowContents[constant.PRICE_COL + shift] \
                .get_text(strip=True).replace("$", "").replace(",", "")),
            int(rowContents[constant.QUANTITY_COL + shift] \
                .get_text(strip=True).replace("+", "").replace(",", "")),
            int(rowContents[constant.QUANTITY_OWNED_COL + shift \
                ].get_text(strip=True).replace(",", "")),
            rowContents[constant.CHANGE_IN_OWNERSHIP_COL + shift] \
                .get_text(strip=True),
            int(rowContents[constant.VALUE_COL + shift] \
                .get_text(strip=True).replace("+$", "").replace(",", "")))