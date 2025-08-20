import colorama
import os
from calccli import run_cli
from dotenv import load_dotenv

load_dotenv()


def warning():
    print(colorama.Fore.RED + "Calc is under it development version..")
    print("therefore, it can have bug and error..")
    print("if, you encounter any, please kindly report them (on github),")
    print("and have valuable place in calc development process")
    print(colorama.Style.RESET_ALL + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print()


if __name__ == "__main__":
    environment = os.getenv("ENVIRONMENT")
    if environment == "Development":
        warning()
    run_cli()
