from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

class CliPrompt:
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

    def retrieve_object(self):
        object_type = self.sfmc_object()
        name = self.sfmc_object_name(object_type)

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
