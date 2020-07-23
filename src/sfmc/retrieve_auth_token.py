import FuelSDK
from colorama import Fore, Back, Style
from config.sfmc_credentials import sfmc_credentials
import sys

def retrieve_auth_token(business_unit):
    print(f'{Fore.YELLOW}==== Retrieving Credentials For {business_unit} ====')
    credentials = get_secrets(business_unit)

    return FuelSDK.ET_Client(False, False, {
                "clientid": credentials['client_id'],
                "clientsecret": credentials['client_secret']
            })

def get_secrets(business_unit):

    for bu in sfmc_credentials:
        if business_unit == bu['name']:
            return bu

    print(f'{Fore.RED}Could Not Find the Business Unit: {business_unit}')
    sys.exit()
