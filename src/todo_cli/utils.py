from functools import wraps
from typing import Callable, Any


def log_action(func: Callable) -> Callable:
    """Decorator to log actions."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[DEBUG] Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] Finished: {func.__name__}")
        return result

    return wrapper


def validate_description(description: str) -> str:
    description = description.strip()
    if not description:
        raise ValueError("Task description cannot be empty.")
    return description
