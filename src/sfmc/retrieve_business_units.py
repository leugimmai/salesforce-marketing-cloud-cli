import json
from pathlib import Path

def retrieve_business_units():

    business_units = []

    with open(f"{Path.home()}/sfmc_cli_credentials.json", "r") as f:
        data = json.loads(f.read())
        
        for business in data:
            business_units.append(business['name'])

    return business_units
