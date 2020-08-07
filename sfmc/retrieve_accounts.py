import json
from pathlib import Path

def retrieve_accounts():

    accounts = []

    with open(f"{Path.home()}/sfmc_cli_credentials.json", "r") as f:
        data = json.loads(f.read())
        
        for account in data:
            accounts.append(account['name'])

    return accounts
