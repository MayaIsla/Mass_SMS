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
    message = client.messages.create(
    to= i,   
    from_="+00000000000",   
    status_callback = 'https://eni6rjqjavb4.x.pipedream.net', #public.requestbin.com
    body="Text you want to display")
    print(message.sid)