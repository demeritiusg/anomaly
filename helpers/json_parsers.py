from helpers import url_reader as ur
import json
# TODO add panadas
# TODO add time
# TODO add datetime

# TODO create function parsing open
# json file, text, or object

# TODO call api function to grab json object

data = ur.stock_api_call_time_series_daily()

def open_parse(data):
    # TODO convert json to dataframe -> to whatever is going to be converted into dashboard
    # data['Time Series (5min)']['2018-10-29 14:10:00']['1. open'] = to get the opening price
    return 'new json or dataframe'
# TODO create function parsing close
# def close_parse():
# TODO create function parsing high
# def high_parse():
# TODO create function parsing low
# def low_parse():
# TODO create function parsing volume
# def volume_parse():