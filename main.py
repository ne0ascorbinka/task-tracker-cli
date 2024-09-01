# import argparse
from argparse import ArgumentParser
from typing import Optional

class Args:
    command: str
    description: Optional[str]


def main() -> None:
    parser = ArgumentParser(prog='task-cli', description="Task tracker CLI instrument")

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument("description", type=str, help="A short description of the task")

    args: Args = parser.parse_args()

    if args.command == "add":
        print(f"Task '{args.description}' added successfully (ID: 1)")
    else:
        print("Unknown command. Use --help arg to seek for help (or go to therapy)")
    

if __name__ == '__main__':
    main()
