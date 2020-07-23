from colorama import init
from src.sfmc_cli import start_sfmc_cli

def sfmc_cli():
    init()

    start_sfmc_cli()

if __name__ == "__main__":
    sfmc_cli()
