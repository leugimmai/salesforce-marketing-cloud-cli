import FuelSDK
import sys
import json
from colorama import Fore, Back, Style
from pathlib import Path

def retrieve_auth_token(business_unit):
    print(f'{Fore.YELLOW}==== Retrieving Credentials For {business_unit} ====')
    credentials = get_secrets(business_unit)

    return FuelSDK.ET_Client(False, False, {
                "clientid": credentials['client_id'],
                "clientsecret": credentials['client_secret']
            })

def get_secrets(business_unit):

    with open(f"{Path.home()}/sfmc_cli_credentials.json", "r") as f:
        business_units = json.loads(f.read())
        for bu in business_units:
            if business_unit == bu['name']:
                return bu

        print(f'{Fore.RED}Could Not Find the Business Unit: {business_unit}')
        sys.exit()
