from datetime import datetime

def convert_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp/1000)