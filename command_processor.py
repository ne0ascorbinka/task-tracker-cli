from storage import Storage, Status
from utils import Args

class CommandProcessor:
    
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
            if args.status: 
                list_filter = lambda task: task.status.value == args.status

            return self.list_tasks(list_filter)
    
    def add(self, description: str) -> str:
        with Storage() as storage:
            id = storage.add_task(description=description)
            return f"Task added successfully (ID: {id})"
            

    def update(self, id: int, description: str) -> str:
        with Storage() as storage:
            try:
                task = storage[id]
                previous_description = task.description
                task.description = description
                return f"Task '{previous_description}' updated successfully"
            except KeyError:
                return f"Failed: no such task with ID {id}"
        

    def delete(self, id: int) -> str:
        with Storage() as storage:
            description = storage.delete_by_id(id)
            return f"Task '{description}' deleted successfully"

    def mark_in_progress(self, id: int) -> str:
        with Storage() as storage:
            try:
                task = storage[id]
                task.status = Status.IN_PROGRESS
                return f"Task '{task.description}' marked as in-progress successfully"
            except KeyError:
                return f"Failed: no such task with ID {id}"

    def mark_done(self, id: int) -> str:
        with Storage() as storage:
            try:
                task = storage[id]
                task.status = Status.DONE
                return f"Task '{task.description}' marked as done successfully"
            except KeyError:
                return f"Failed: no such task with ID {id}"

    def list_tasks(self, filter: str = None) -> str:
        with Storage() as storage:
            tasks = storage.get_tasks(filter=filter)
            return '\n\n'.join(str(task) for task in tasks) if tasks else f"There are no such tasks yet" if filter else "No tasks yet"