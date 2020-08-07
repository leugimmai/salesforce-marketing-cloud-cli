from figlet.startup import title
from src.cli_prompt import CliPrompt

def start_sfmc_cli():
    title()

    cli_prompt = CliPrompt()

    response = cli_prompt.initial_prompt()

    if response == "Retrieve Object Path":
        cli_prompt.choose_account()
        cli_prompt.retrieve_object()
    elif response == "Check Automations":
        cli_prompt.check_automations()
    elif response == "Search Queries":
        cli_prompt.search_queries()
    else:
        print("Exiting")

