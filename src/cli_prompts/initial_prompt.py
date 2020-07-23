from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

def initial_prompt():

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
