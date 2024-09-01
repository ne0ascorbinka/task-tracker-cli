from argparse import ArgumentParser
from typing import Optional

class Args:
    command: str
    description: Optional[str]
    id: Optional[int]


def main() -> None:
    parser = ArgumentParser(prog='task-cli', description="Task tracker CLI instrument")

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument("description", type=str, help="A short description of the task")

    update_parser = subparsers.add_parser('update', help="Update task description by ID")
    update_parser.add_argument('id', type=int,help="Task ID")

    delete_parser = subparsers.add_parser('delete', help="Delete task by ID")
    delete_parser.add_argument('id', type=int, help="Task ID")

    args: Args = parser.parse_args()

    if args.command == "add":
        print(f"Task '{args.description}' added successfully (ID: 1)")
    elif args.command == "update":
        print(f"Task updated successfully (ID: {args.id})")
    else:
        print("Unknown command. Use --help arg to seek for help (or go to therapy)")
    

if __name__ == '__main__':
    main()
