import pandas as pd
import requests
import json
from config import *

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)

def get_account():
    r = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY})
    return json.loads(r.content)



print(get_account())