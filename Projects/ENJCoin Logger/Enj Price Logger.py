from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os

# api endpoint url
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

# api request parameters
# set slug to your coin
parameters = {"slug": "enjin-coin", "convert": "USD"}


# sets a session header
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


# grabs coin data from endpoint
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


# set the header
headers = set_header()

# send your request
data = pull_data(url, parameters, headers)

# convert to a dataframe from json
df = pd.json_normalize(data)

# save the raw data
df.to_csv("raw_data.csv")
# load a new dataframe
data = pd.read_csv("raw_data.csv")

# data cleaning
data.drop(
    labels=[
        "Unnamed: 0",
        "status.error_code",
        "status.error_message",
        "status.elapsed",
        "status.credit_count",
        "status.notice",
        "data.2130.slug",
        "data.2130.num_market_pairs",
        "data.2130.date_added",
        "data.2130.tags",
        "data.2130.max_supply",
        "data.2130.circulating_supply",
        "data.2130.total_supply",
        "data.2130.platform.id",
        "data.2130.platform.name",
        "data.2130.platform.symbol",
        "data.2130.platform.slug",
        "data.2130.platform.token_address",
        "data.2130.is_active",
        "data.2130.cmc_rank",
        "data.2130.is_fiat",
        "data.2130.last_updated",
        "data.2130.quote.USD.market_cap",
        "data.2130.quote.USD.market_cap_dominance",
        "data.2130.quote.USD.fully_diluted_market_cap",
    ],
    axis=1,
    inplace=True,
)

new_names = {
    "status.timestamp": "datetime",
    "data.2130.id": "id",
    "data.2130.name": "name",
    "data.2130.symbol": "symbol",
    "data.2130.quote.USD.price": "price_usd",
    "data.2130.quote.USD.volume_24h": "volume_24h",
    "data.2130.quote.USD.volume_change_24h": " volume_change_24h",
    "data.2130.quote.USD.percent_change_1h": "percent_change_1h",
    "data.2130.quote.USD.percent_change_24h": "percent_change_24h",
    "data.2130.quote.USD.percent_change_7d": "percent_change_7d",
    "data.2130.quote.USD.percent_change_30d": "percent_change_30d",
    "data.2130.quote.USD.percent_change_60d": "percent_change_60d",
    "data.2130.quote.USD.percent_change_90d": "percent_change_90d",
    "data.2130.quote.USD.last_updated": "price_last_updated",
}
data.rename(new_names, axis=1, inplace=True)

# append cleaned data to an existing csv
# if file does not exist write a header
if not os.path.isfile("enj_price_log.csv"):
    data.to_csv("enj_price_log.csv", header="column_names")
else:  # else it exists so append without writing the header
    data.to_csv("enj_price_log.csv", mode="a", header=False)
