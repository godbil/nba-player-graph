"""CSC111 Final Report: The National Basketball Association’s Statistically Best Players Node and Edge Module

Description
===============================

This module contains the two node data structures and the edge data structure which is the Award and BasketballPlayer
class and the Achieved class respectively. The Award class holds the name and the amount of points for each award from
our data set. The BasketballPlayer class holds lots of information about the player and finally the Achieved class
has an Award and a BasketballPlayer in it, plus the number of awards of that kind won by the player. Each class has
it's own methods which are used throughout the program. These three classes are used by the network data structure
to keep track of the entire graph.

Copyright
===============================

This file is Copyright (c) 2023 Vincent Louie and Junwei Quan.
"""

from __future__ import annotations

import doctest
from typing import Optional


class Award:
    """
    A class to represent the different awards that players can win

    Instance Attributes:
    - name: The name of the award
    - points: The amount of points that is awarded to a player for achieving this award
    """
    name: str
    points: int

    def __init__(self, name: str, points: int) -> None:
        self.name = name
        self.points = points


class BasketballPlayer:
    """
    A class to represent a basketball player with personal information.

    Instance Attributes:
    - name: The full name of the basketball player
    - age: The age of the basketball player (or age at death for players who passed away)
    - status: A boolean telling us whether the player is retired or still in league (True for active, false for retired)
    - start_year: The year that the NBA player started playing in the NBA
    - end_year: The year that the NBA player retired or None is the player is still active
    - hall_of_fame: A boolean telling us whether the player was inducted into the NBA Hall of Fame
    - awards: A mapping which maps the award name to the achieved class

    Representation Invariants:
    - status or end_year is not None
    """
    name: str
    age: int
    status: bool
    start_year: int
    end_year: Optional[int]
    hall_of_fame: bool
    awards: dict[str, Achieved]

    def __init__(self, name: str, age: int, status: bool, start_year: int, hall_of_fame: bool,
                 end_year: Optional[int] = None) -> None:
        self.name = name
        self.age = age
        self.status = status
        self.start_year = start_year
        self.end_year = end_year
        self.hall_of_fame = hall_of_fame
        self.awards = {}

    def achieve_award(self, award: Award, number: int) -> None:
        """
        Add a specific number of awards to the basketball player with an award node
        """
        achieved = Achieved(self, award, number)
        self.awards[award.name] = achieved

    def get_total_points(self) -> int:
        """
        Return the total points that player get from different awards.
        """
        total_points = 0
        for achieved in self.awards.values():
            total_points += achieved.award.points * achieved.number
        return total_points


class Achieved:
    """A link or "edge" that connects a player to the specific award that they have achieved.

    Instance Attributes:
    - player: The player that has won the award
    - award: The award that the player has achieved
    - number: The number of times that the player has won this award

    Representation Invariants:
    - number > 0
    """
    player: BasketballPlayer
    award: Award
    number: int

    def __init__(self, player: BasketballPlayer, award: Award, number: int) -> None:
        self.player = player
        self.award = award
        self.number = number


if __name__ == '__main__':
    doctest.testmod()
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['Optional'],
        'disable': ['unused-import'],
    })
