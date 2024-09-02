from storage import Storage, Status
from utils import Args

class CommandProcessor:
    """
    Command processes proccess. 
    """

    def process(self, args: Args) -> str:
        command = args.command

        if command == "add":
            return self.add(args.description)
        
        elif command == "update":
            return self.update(args.id, args.description)
        
        elif command == "delete":
            return self.delete(args.id)
        
        elif command == "mark-in-progress":
            return self.mark_in_progress(args.id)
        
        elif command == "mark-done":
            return self.mark_done(args.id)
        
        elif command == "list":
            list_filter = None
            if args.status: list_filter = lambda task: task["status"] == args.status

            return self.list_tasks(list_filter)
    
    def add(self, description: str) -> str:
        with Storage() as storage:
            id = storage.add_task(description=description)
            return f"Task added successfully (ID: {id})"
            


    def update(self, id: int, description: str) -> str:
        with Storage() as storage:
            try:
                task = storage[id]
                task.description = description
            except KeyError:
                return f"Failed: no such task with ID {id}"
        
        return f"Task updated successfully (ID: {id})"

    def delete(self, id: int) -> str:
        with Storage() as storage:
            storage.delete_by_id(id)
            return f"Task deleted successfully (ID: {id})"

    def mark_in_progress(self, id: int) -> str:
        with Storage() as storage:
            try:
                storage[id].status = Status.IN_PROGRESS
                return f"Task marked as in-progress successfully (ID: {id})"
            except KeyError:
                return f"Failed: no such task with ID {id}"

    def mark_done(self, id: int) -> str:
        with Storage() as storage:
            try:
                storage[id].status = Status.DONE
                return f"Task marked as done successfully (ID: {id})"
            except KeyError:
                return f"Failed: no such task with ID {id}"

    def list_tasks(self, filter: str = None) -> str:
        pass