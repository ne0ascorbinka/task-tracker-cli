from __future__ import annotations
from typing import Optional, Type
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
            datetime.fromisoformat(task_dict["updated_at"]) if task_dict.get("updated_at") else None
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

class Storage:
    def __init__(self, path: str = 'tasks.json') -> None:
        self.path = path
        self._tasks = None
        self._count = None
    
    def __enter__(self) -> Storage:
        if not os.path.exists(self.path):
            self._tasks = []
            self._count = count(0)
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

        return True
    
    def add_task(self, description: str) -> int:
        task = Task(id=next(self._count), description=description, status=Status.TODO, 
                    createdAt=datetime.now())
        self._tasks.append(task)
        return task.id