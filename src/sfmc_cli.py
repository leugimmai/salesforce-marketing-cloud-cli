from figlet.startup import title
from cli_prompts.initial_prompt import initial_prompt

def start_sfmc_cli():
    title()

    response = initial_prompt()
