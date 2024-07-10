from twilio.rest import Client
import pandas as pd
import requests
import json
import time


dict = "C:/path/to/file/file.csv"

df = pd.read_csv(dict)

account_sid = "SID"

auth_token  = "token"

client = Client(account_sid, auth_token)

for i in df['Phone']:
    try:
        message = client.messages.create(
        to = i,
        from_="+10000000000",   
        body = "Text you want to display")
        print(message.sid)
        mess_phone = str(i)
        mess_id = str(message.sid)
        logging.info(mess_phone + " " + mess_id)
    except:
        pass


