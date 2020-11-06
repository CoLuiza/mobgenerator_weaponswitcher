import json
from dataclasses import dataclass


@dataclass
class EnemyType:
    id: int
    arrow: float
    bullet: float
    special: float
    speed: float
    resource_path: str


@dataclass
class Enemy:
    enemy_type: EnemyType
    timestamp: float
    track: int

    def get_representation(self):
        return {
            "health":
                {
                    "arrow": self.enemy_type.arrow,
                    "bullet": self.enemy_type.bullet,
                    "special": self.enemy_type.special
                },
            "speed": self.enemy_type.speed, "track": self.track, "timestamp": self.timestamp,
            "resourcePath": self.enemy_type.resource_path
        }
