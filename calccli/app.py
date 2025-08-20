from os import path
from calc.customerr import CalcException
from calc.executor import calc_execute
from .utils import print_help_msg


def read_code(scriptname):
    with open(scriptname) as script:
        return script.readlines()


def script_executor(scriptname):
    if path.exists(scriptname):
        codelines = read_code(scriptname)
        for codeline in codelines:
            calc_execute(codeline)
    else:
        raise CalcException(f'Script "{scriptname}" not found!!')


def repl_executor():
    print("Welcome to Calc REPL!!!!!")
    print("Type 'help' for help")
    print()

    while True:
        try:
            code = input(">> ")
            if code == "quit" or code == "exit":
                print()
                return 0
            elif code[:4] == "help":
                context = code[5:]
                print_help_msg(context.strip())
            else:
                print(calc_execute(code))
        except CalcException as e:
            print(e)
