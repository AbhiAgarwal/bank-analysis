import os, json

from plaid import Client
from plaid import errors as plaid_errors

plaid_client_id = os.getenv('plaid_client_id', '')
plaid_secret = os.getenv('plaid_secret', '')
plaid_access_token = os.getenv('plaid_access_token', '')

Client.config({
    'url': 'https://api.plaid.com',
    'suppress_http_errors': True,
})

client = Client(client_id=plaid_client_id, secret=plaid_secret, access_token=plaid_access_token)

response = client.balance()
balance = json.loads(response.content)

response = client.connect_get()
transactions = json.loads(response.content)