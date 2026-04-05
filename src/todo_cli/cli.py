import argparse
from pathlib import Path

from todo_cli.manager import TodoManager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI To-Do Manager")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str)

    # Remove
    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("id", type=int)

    # List
    subparsers.add_parser("list", help="List all tasks")

    return parser


def handle_command(args: argparse.Namespace, manager: TodoManager) -> None:
    if args.command == "add":
        task = manager.add_task(args.description)
        print(f"Added task [{task.id}]: {task.description}")

    elif args.command == "remove":
        success = manager.remove_task(args.id)
        if success:
            print(f"Removed task {args.id}")
        else:
            print(f"Task {args.id} not found")

    elif args.command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            print(f"[{task.id}] {task.description}")
