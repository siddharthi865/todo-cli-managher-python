from pathlib import Path
import tempfile

from todo_cli.manager import TodoManager


def test_add_and_list_tasks():
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = TodoManager(Path(tmpdir) / "tasks.json")

        manager.add_task("Test task")

        tasks = manager.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].description == "Test task"


def test_remove_task():
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = TodoManager(Path(tmpdir) / "tasks.json")

        task = manager.add_task("Task to remove")
        success = manager.remove_task(task.id)

        assert success
        assert len(manager.list_tasks()) == 0


def test_remove_nonexistent_task():
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = TodoManager(Path(tmpdir) / "tasks.json")

        success = manager.remove_task(999)
        assert not success
