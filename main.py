from argparse import ArgumentParser
from utils import Args
from storage import Storage
from command_processor import CommandProcessor

def main() -> None:
    parser = ArgumentParser(prog='task-cli', description="Task tracker CLI instrument")

    subparsers = parser.add_subparsers(dest='command', help="Commands")

    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument("description", type=str, help="A short description of the task")

    update_parser = subparsers.add_parser('update', help="Update task description by ID")
    update_parser.add_argument('id', type=int,help="Task ID")
    update_parser.add_argument('description', type=str, help="New task description")

    delete_parser = subparsers.add_parser('delete', help="Delete task by ID")
    delete_parser.add_argument('id', type=int, help="Task ID")

    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help="Mark task as in progress")
    mark_in_progress_parser.add_argument('id', type=int, help="Task ID")

    mark_done_parser = subparsers.add_parser('mark-done', help="Mark task as done")
    mark_done_parser.add_argument('id', type=int, help="Task ID")

    list_parser = subparsers.add_parser('list', help="List tasks")
    list_parser.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'],
                             help="Filter tasks by status [done | todo | in-progress]")

    args: Args = parser.parse_args()

    try:
        storage = Storage()
        command_processor = CommandProcessor(storage)

        print(command_processor.process(args))
    except Exception as e:
        print("Error 500!\n\n")
        print(e.with_traceback())

        

if __name__ == '__main__':
    main()
