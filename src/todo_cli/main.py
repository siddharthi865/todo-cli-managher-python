from pathlib import Path

from todo_cli.cli import build_parser, handle_command
from todo_cli.manager import TodoManager


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    storage_path = Path.cwd()  / "tasks.json"
    manager = TodoManager(storage_path)

    handle_command(args, manager)


if __name__ == "__main__":
    main()
