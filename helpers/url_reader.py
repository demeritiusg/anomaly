from requests import request
import logging
import json
# TODO add boto3


# TODO add first lambda function
# TODO stock_api_call returns json?

# TODO create function for api call to trigger lambda function
# api key
# stock symbol

def stock_api_call_time_series_daily(symbol, key):

    with open('../jsons/temp.json', 'wb') as js:
        jsondata = json.load(js)
    for sym in symbol:
        try:
            r = request.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}').format(
                sym, key, )
        except ConnectionError:
            logging.exception()

        # TODO double check this works
        jsondata = jsondata.append(r)

    # Save new file to S3 bucket
    return jsondata
