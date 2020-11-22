from __future__ import annotations

import random

from typing import Optional, TYPE_CHECKING
from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item


class Resurrectable(BaseComponent):
    parent: Actor

    def __init__(self, number_of_turns: int, max_lives: int):
        self.number_of_turns = number_of_turns
        self.number_of_lives = random.randint(1, max_lives)


