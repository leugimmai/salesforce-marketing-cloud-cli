from figlet.startup import title
from cli_prompt import CliPrompt

def start_sfmc_cli():
    title()

    cli_prompt = CliPrompt()

    response = cli_prompt.initial_prompt()

    if response == "Retrieve Object Path":
        cli_prompt.retrieve_object()
    else:
        print("Exiting")

