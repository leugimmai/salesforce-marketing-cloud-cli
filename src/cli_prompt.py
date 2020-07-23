from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from sfmc.retrieve_accounts import retrieve_accounts
from sfmc.get_object_path import get_object_path
from sfmc.automation_check import automation_check

class CliPrompt:
    def __init__(self):
        self.account = None

    def initial_prompt(self):

        action_to_take = [
            {
                "type": "list",
                "name": "action",
                "message": "What would you like to do?",
                "choices": ["Retrieve Object Path", 
                            "Check Automations", 
                            "Exit"],
            }
        ]
        result = prompt(action_to_take)

        return result["action"]

    def choose_account(self):
        accounts = retrieve_accounts()

        account = [
            {
                "type": "list",
                "name": "name",
                "message": "Choose a Account in SFMC:",
                "choices": accounts,
            }
        ]

        result = prompt(account)

        self.account = result["name"]


    def retrieve_object(self):
        object_type = self.sfmc_object()
        name = self.sfmc_object_name(object_type)
        get_object_path(self.account, object_type, name)

    def sfmc_object(self):
        sfmc_object = [
            {
                "type": "list",
                "name": "object",
                "message": "Which SFMC Object do you need?",
                "choices": ["Data Extension", "Triggered Send", "Data Filter"],
            }
        ]

        result = prompt(sfmc_object)

        return result["object"]

    def sfmc_object_name(self, object_type):

        object_name = [
            {"type": "input", "name": "name", "message": f"Name of the {object_type}:"}
        ]

        result = prompt(object_name)

        return result["name"]

    def check_automations(self):
        automation_check()