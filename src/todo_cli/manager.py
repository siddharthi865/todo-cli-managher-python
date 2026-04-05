from pathlib import Path
from typing import List

from todo_cli.models import Task
from todo_cli.storage import FileStorage
from todo_cli.utils import log_action, validate_description


class TodoManager:
    def __init__(self, storage_path: Path) -> None:
        self.storage = FileStorage(storage_path)
        self.tasks: List[Task] = self.storage.load_tasks()

    def _get_next_id(self) -> int:
        return max((task.id for task in self.tasks), default=0) + 1

    @log_action
    def add_task(self, description: str) -> Task:
        description = validate_description(description)
        task = Task(id=self._get_next_id(), description=description)
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        return task

    @log_action
    def remove_task(self, task_id: int) -> bool:
        original_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]

        if len(self.tasks) == original_len:
            return False

        self.storage.save_tasks(self.tasks)
        return True

    def list_tasks(self) -> List[Task]:
        return self.tasks
