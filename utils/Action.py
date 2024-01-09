from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Action:
    input: str
    key: str
    action: str | Callable
    params: dict = field(default_factory=dict)
