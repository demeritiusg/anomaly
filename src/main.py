from helpers import url_reader as ur

# TODO add boto3
# TODO add json
# TODO add time

# TODO Where are we hiding keys? Cognito is a thing

stock_list = []  # TODO load a list from a text file

apiKey = ''  # loading keys from AWS service?

# if dataset == 5 min dataset then:
    # run 5 min funtion
# elif dataset == some other dataset then:
    # run some other dataset

ur.stock_api_call_time_series_daily(symbol=stock_list, key=apiKey)