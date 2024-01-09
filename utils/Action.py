from dataclasses import dataclass, field


@dataclass
class Action:
    input: str
    key: str
    action: str
    params: dict = field(default_factory=dict)
