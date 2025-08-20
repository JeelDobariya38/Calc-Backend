import sys
from . import repl_executor, script_executor
from .utils import print_help_msg, print_version


def arg_parse():
    if len(sys.argv) >= 1:
        return sys.argv[1:]
    return False


def run_cli():
    args = arg_parse()
    if args:
        if args[0].startswith("--"):
            if args[0] == "--version":
                print_version()
                return 0
            elif args[0] == "--help":
                print_help_msg()
                return 0
            else:
                raise ValueError(f'Invalid argument "{args[0]}"')
        else:
            return script_executor(args[0])
    else:
        return repl_executor()
