from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

# endpoint url
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
# "id": 2130,
# "name": "Enjin Coin",
# "symbol": "ENJ",
# "slug": "enjin-coin",

# api request parameters
# parameters = {"start": "1", "limit": "5", "convert": "USD"}
parameters = {"slug": "enjin-coin", "convert": "USD"}


def set_header():
    # session header
    # contains api key for request
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "",
    }

    print("Please enter your api key")
    headers["X-CMC_PRO_API_KEY"] = str(input())

    # check
    # print(headers["X-CMC_PRO_API_KEY"])
    return headers


# grabs data from endpoint
def pull_data(url, parameters, headers):
    # start a new http session
    session = Session()
    # set header for api key
    session.headers.update(headers)

    # try to pull data
    try:
        # new http response
        response = session.get(url, params=parameters)
        # decode json
        data = json.loads(response.text)
        # print(data)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


headers = set_header()
data = pull_data(url, parameters, headers)

df = pd.json_normalize(data)

df.to_csv("enj_log.csv")


"status.error_code", "status.error_message", "status.elapsed", "status.credit_count", "status.notice", "data.2130.slug", "data.2130.num_market_pairs", "data.2130.date_added", "data.2130.tags", "data.2130.max_supply", "data.2130.circulating_supply", "data.2130.total_supply", "data.2130.platform.id", "data.2130.platform.name", "data.2130.platform.symbol", "data.2130.platform.slug", "data.2130.platform.token_address", "data.2130.is_active", "data.2130.cmc_rank", "data.2130.is_fiat", "data.2130.last_updated", "data.2130.quote.USD.market_cap", "data.2130.quote.USD.market_cap_dominance", "data.2130.quote.USD.fully_diluted_market_cap"
