from dataclasses import dataclass


@dataclass
class Task:
    id: int
    description: str

    def to_dict(self) -> dict:
        return {"id": self.id, "description": self.description}

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(id=data["id"], description=data["description"])
