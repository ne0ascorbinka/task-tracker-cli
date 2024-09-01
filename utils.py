from typing import Literal, Optional

Status = Literal['done', 'todo', 'in-progress']

class Args:
    command: str
    description: Optional[str]
    id: Optional[int]
    status: Optional[Literal['done', 'todo', 'in-progress']]