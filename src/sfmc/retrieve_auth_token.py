import FuelSDK
import sys
import json
from colorama import Fore, Back, Style
from pathlib import Path

def retrieve_auth_token(account):
    print(f'{Fore.YELLOW}==== Retrieving Credentials for {account} ====')
    credentials = get_secrets(account)

    return FuelSDK.ET_Client(False, False, {
                "clientid": credentials['client_id'],
                "clientsecret": credentials['client_secret']
            })

def get_secrets(account_name):

    with open(f"{Path.home()}/sfmc_cli_credentials.json", "r") as f:
        accounts = json.loads(f.read())
        for account in accounts:
            if account_name == account['name']:
                return account

        print(f'{Fore.RED}Could Not Find the Account: {account}')
        sys.exit()
