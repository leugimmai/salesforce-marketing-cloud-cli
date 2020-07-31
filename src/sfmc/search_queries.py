import FuelSDK
import os
import json
from colorama import Fore, Back, Style
from pathlib import Path
from sfmc.retrieve_auth_token import retrieve_auth_token
from sfmc.soap_requests import retrieve_automation_name_for_query

def search_queries(args):

    create_query_csv()

    with open(f"{Path.home()}/sfmc_cli_credentials.json", "r") as f:

        accounts = json.loads(f.read())

        for account in accounts:
            print(f'{Fore.BLUE}==== Searching in {account["name"]} ====')
            auth_token = retrieve_auth_token(account["name"])

            search_filter = {'Property': 'QueryText', 'SimpleOperator': 'like', 'Value': args}
            props = ["Name", "Status", "QueryText"]

            queries = FuelSDK.ET_Get(auth_stub=auth_token, obj_type="QueryDefinition",
                                props=props, search_filter=search_filter)

            for result in queries.results:
                query_name = result.Name
                automation_name = retrieve_automation_name_for_query(auth_token, query_name)
                print(f'{account["name"]},{result.Name},{automation_name}')
                write_to_query_csv(f'{account["name"]},{result.Name},{automation_name}\n')

        print(f'{Fore.GREEN}==== You can find the csv file at: ~/sfmc_cli_queries_result.csv ====')



def create_query_csv():
    file_path = f'{Path.home()}/sfmc_cli_queries_result.csv'

    with open(file_path, 'w+') as f:
        f.write(f'Account,Query Name,Automation\n')

def write_to_query_csv(row):
    file_path = f'{Path.home()}/sfmc_cli_queries_result.csv'

    with open(file_path, 'a') as f:
        f.write(row)
