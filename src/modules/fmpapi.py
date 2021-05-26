from urllib.request import urlopen
import json

def get_jsonparsed_data(url):
    """
    Retrieve the content of ``url``, parse it as JSON to a dictionary.

    Arguments
    url : str -- url to retrieve content from
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def print_all_stocks() -> None:
    url = "https://financialmodelingprep.com/api/v3/stock/list" \
        "?apikey=ec372cc0b6c77b8ef5d6cbcc248d3898"
    stocks_json = get_jsonparsed_data(url)
    for item in stocks_json:
        print(item['symbol'])

