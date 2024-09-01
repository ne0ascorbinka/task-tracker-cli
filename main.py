from argparse import ArgumentParser
from typing import Optional, Literal

Status = Literal['done', 'todo', 'in-progress']

class Args:
    command: str
    description: Optional[str]
    id: Optional[int]
    status: Optional[Literal['done', 'todo', 'in-progress']]


def main() -> None:
    parser = ArgumentParser(prog='task-cli', description="Task tracker CLI instrument")

    subparsers = parser.add_subparsers(dest='command', help="Basic commands")

    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument("description", type=str, help="A short description of the task")

    update_parser = subparsers.add_parser('update', help="Update task description by ID")
    update_parser.add_argument('id', type=int,help="Task ID")

    delete_parser = subparsers.add_parser('delete', help="Delete task by ID")
    delete_parser.add_argument('id', type=int, help="Task ID")

    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help="Mark task as in progress")
    mark_in_progress_parser.add_argument('id', type=int, help="Task ID")

    mark_done_parser = subparsers.add_parser('mark-done', help="Mark task as done")
    mark_done_parser.add_argument('id', type=int, help="Task ID")

    list_parser = subparsers.add_parser('list', help="List tasks")
    list_parser.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'])

    args: Args = parser.parse_args()

    if args.command == "add":
        print(f"Task '{args.description}' added successfully (ID: 1)")
    elif args.command == "update":
        print(f"Task updated successfully (ID: {args.id})")
    elif args.command == "list":
        print(f"Listing task by {args.status}: 1, 2, 4")
    else:
        print("Unknown command. Use --help arg to seek for help (or go to therapy)")
    

if __name__ == '__main__':
    main()
