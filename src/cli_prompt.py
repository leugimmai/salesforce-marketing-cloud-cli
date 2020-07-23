from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from sfmc.retrieve_business_units import retrieve_business_units
from sfmc.get_object_path import get_object_path

class CliPrompt:
    def __init__(self):
        self.business_unit = None

    def initial_prompt(self):

        action_to_take = [
            {
                "type": "list",
                "name": "action",
                "message": "What would you like to do?",
                "choices": ["Retrieve Object Path", "Exit"],
            }
        ]
        result = prompt(action_to_take)

        return result["action"]

    def choose_business_unit(self):
        business_units = retrieve_business_units()

        business_unit = [
            {
                "type": "list",
                "name": "name",
                "message": "Choose a BU in SFMC:",
                "choices": business_units,
            }
        ]

        result = prompt(business_unit)

        self.business_unit = result["name"]


    def retrieve_object(self):
        object_type = self.sfmc_object()
        name = self.sfmc_object_name(object_type)
        get_object_path(self.business_unit, object_type, name)

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
