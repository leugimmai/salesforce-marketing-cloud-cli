import FuelSDK
from colorama import Fore, Back, Style
from config.sfmc_creds import sfmc_creds
import sys

def get_bu_client_id_and_secret(business_unit):
    print(f'{Fore.YELLOW}==== Retrieving Credentials For {business_unit} ====')
    credentials = get_secrets(business_unit)

    return FuelSDK.ET_Client(False, False, {
                "clientid": credentials['client_id'],
                "clientsecret": credentials['client_secret']
            })

def get_secrets(business_unit):

    for bu in sfmc_creds:
        if business_unit == bu['name']:
            return bu

    print(f'{Fore.RED}Could Not Find the Business Unit: {business_unit}')
    sys.exit()
