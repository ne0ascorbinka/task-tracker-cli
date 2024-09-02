from __future__ import annotations
from typing import Optional, Type, Any, Callable
import json
import os
from itertools import count
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


@dataclass
class Task:
    id: int
    description: str
    status: Status
    createdAt: datetime
    updatedAt: Optional[datetime] = None

    @classmethod
    def from_json(cls, task_dict: dict) -> Task:
        return cls(
            task_dict["id"],
            task_dict["description"],
            Status(task_dict["status"]),
            datetime.fromisoformat(task_dict["createdAt"]),
            datetime.fromisoformat(task_dict["updatedAt"]) if task_dict.get("updatedAt") else None
        )
    
    def to_json(self) -> dict:
        json_dict = {
            "id" : self.id,
            "description" : self.description,
            "status" : self.status.value,
            "createdAt" : self.createdAt.isoformat(),
        }

        if self.updatedAt: json_dict["updatedAt"] = self.updatedAt.isoformat()

        return json_dict
    
    def __setattr__(self, name: str, value: Any) -> None:
        update_time = datetime.now()
        super().__setattr__("updatedAt", update_time)

        return super().__setattr__(name, value)
    
    def __str__(self) -> str:
        return f"""'{self.description}':
    ID: {self.id}
    status: {self.status.value}
    created at: {self.createdAt.strftime("%d/%m/%Y, %H:%M:%S")}
    {f"updated at: {self.updatedAt.strftime("%d/%m/%Y, %H:%M:%S") + '\n' if self.updatedAt else ''}"}"""

class Storage:
    def __init__(self, path: str = 'tasks.json') -> None:
        self.path = path
        self._tasks = None
        self._count = None
    
    def __enter__(self) -> Storage:
        if not os.path.exists(self.path):
            self._tasks = []
            self._count = count(1)
            return self

        with open(self.path) as file:
            data = json.load(file)
            self._tasks = [Task.from_json(task_dict=task) for task in data["tasks"]] # TODO: mb use get instead
            self._count = count(data["count"])

        return self
    
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[Exception]) -> bool:
        data = {
            "count" : next(self._count),
            "tasks" : [task.to_json() for task in self._tasks]
        }

        try:
            with open(self.path, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            return False

        return False
    
    def __getitem__(self, id: int) -> Task:
        for task in self._tasks:
            if task.id == id: return task
        else:
            raise KeyError(f"No task found by ID {id}")
        
    def get_task_by_id(self, id: int) -> Task:
        return self[id]
    
    def delete_by_id(self, id: int) -> str:
        task = self[id]
        self._tasks.remove(task)

        return task.description
    
    def add_task(self, description: str) -> int:
        task = Task(id=next(self._count), description=description, status=Status.TODO, 
                    createdAt=datetime.now())
        self._tasks.append(task)
        return task.id
    
    def get_tasks(self, filter: Optional[Callable[[Task], bool]] = None) -> list[Task]:
        if filter:
            return [task for task in self._tasks if filter(task)]
        
        return self._tasks