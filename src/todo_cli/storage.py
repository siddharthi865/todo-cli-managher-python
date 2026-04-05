import json
from pathlib import Path
from typing import List

from todo_cli.models import Task


class StorageError(Exception):
    pass


class FileStorage:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def load_tasks(self) -> List[Task]:
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, OSError) as e:
            raise StorageError(f"Failed to load tasks: {e}")

    def save_tasks(self, tasks: List[Task]) -> None:
        try:
            with self.file_path.open("w", encoding="utf-8") as f:
                json.dump([task.to_dict() for task in tasks], f, indent=2)
        except OSError as e:
            raise StorageError(f"Failed to save tasks: {e}")
