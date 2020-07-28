import FuelSDK
import sys
import json
from colorama import Fore, Back, Style
from sfmc.retrieve_auth_token import retrieve_auth_token
from pathlib import Path

def automation_check():
    print(f"{Fore.CYAN}=====================================================")
    
    with open(f"{Path.home()}/sfmc_cli_automations_to_check.json", "r") as f:
        data = json.loads(f.read())
        
        for account in data:
            auth_token = retrieve_auth_token(account['account'])

            for automation in account['automations']:
                check_automation_is_turned_on(automation, auth_token)
                
                print(f"{Fore.CYAN}=====================================================")
    
def check_automation_is_turned_on(automation_name, authentication):
    
    search_filter = {'Property': 'Name', 'SimpleOperator': 'equals', 'Value': automation_name}
    props = ["Name", "Status", "ScheduledTime", "CustomerKey"]
    
    automation = FuelSDK.ET_Get(auth_stub=authentication, obj_type="Automation", 
                                props=props, search_filter=search_filter)
    
    automation_status = automation.results[0].Status
    customer_key = automation.results[0].CustomerKey
    
    status = get_automation_status(automation_status)
    
    if automation_status == 6 or automation_status == 7:
        print(f'{Fore.GREEN}{automation_name} is set to: {status}{Style.RESET_ALL}')
        
        check_last_time_ran(automation_name, authentication)
    else:
        print(f'{Fore.RED}{automation_name} is currently set to: {status}{Style.RESET_ALL}')
        
        if status != "Running":
            check_last_time_ran(automation_name, authentication)
        
def check_last_time_ran(automation_name, authentication):
    search_filter = {'Property': 'Name', 'SimpleOperator': 'equals', 'Value': automation_name}
    props = ['Name', 'CustomerKey', 'ProgramID', 'CompletedTime', 'Status']
    
    instances = FuelSDK.ET_Get(auth_stub=authentication, obj_type='AutomationInstance',
                               props=props, search_filter=search_filter)
    
    instances.results.sort(key=lambda automation: automation.CompletedTime)
    
    last_instance_completed_time = instances.results[-1].CompletedTime
    last_instance_status = instances.results[-1].StatusMessage

    if last_instance_status == "Error":
        print(f'{automation_name} last ran at {last_instance_completed_time} with status: {Fore.RED}{last_instance_status}{Style.RESET_ALL}')
    else:
        print(f'{automation_name} last ran at {last_instance_completed_time} with status: {Fore.BLUE}{last_instance_status}{Style.RESET_ALL}')
        
def get_automation_status(status_number):
    switcher = {
        -1: "Error",
        0: "Building Error",
        1: "Building",
        2: "Ready",
        3: "Running",
        4: "Paused",
        5: "Stopped",
        6: "Scheduled",
        7: "Awaiting Trigger",
        8: "Inactive Trigger",
    }
    return switcher.get(status_number, "Invalid status")