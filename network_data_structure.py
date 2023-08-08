"""CSC111 Final Report: The National Basketball Association’s Statistically Best Players Network Module

Description
===============================

This module contains the main network which stores all of the information about the data set including the awards, the
players and the achieved links. In this class, we use methods to add players, awards and achieved links from the data
sets that we found/created. As well, we pass in a networkx.Graph to each of these methods to create a networkx.Graph
which will be used for the visualization of the graph.

Copyright
===============================

This file is Copyright (c) 2023 Vincent Louie and Junwei Quan.
"""

import distutils.util as module
import doctest

import PIL

import networkx as nx

from PIL import Image
from node_edge_data_structure import BasketballPlayer, Award


class AwardNetwork:
    """A network similar to graphs where NBA players are linked using Achieved to the different awards
     that they have won in their career or so far.

    Instance Attributes:
    - _players: A mapping from the basketball player's name to the BasketballPlayer object
    - _awards: A mapping from the name of the award to the Award object
    """
    _players: dict[str, BasketballPlayer]
    _awards: dict[str, Award]

    def __init__(self) -> None:
        self._players = {}
        self._awards = {}

    def add_players(self, data: list[list[str | int]], network: nx.Graph) -> None:
        """Add all players to the players mapping given the data of all player.

        Preconditions:
        - The inner lists is in the form of [name, age, status, start year, end year, hall of fame, ...]
        (rest of the list are award numbers which will not be used in this function)
        """
        for player_data in data:
            # Image URLs for graph nodes
            icons = {player_data[0]: "icons/" + player_data[22]}

            # Load images
            images = {k: PIL.Image.open(fname) for k, fname in icons.items()}

            if player_data[4] == 'None':
                end_year = None
            else:
                end_year = int(player_data[4])
            player = BasketballPlayer(name=player_data[0], age=int(player_data[1]),
                                      status=bool(module.strtobool(player_data[2])),
                                      start_year=int(player_data[3]), end_year=end_year,
                                      hall_of_fame=bool(module.strtobool(player_data[5])))
            self._players[player_data[0]] = player
            network.add_node(player, image=images[player_data[0]])

    def add_awards(self, data: list[list[str | int]], network: nx.Graph) -> None:
        """Add all awards for the data to the award mapping given the data of all awards.

        Preconditions:
        - The inner lists is in the form of [name, points]
        """
        for award_data in data:
            # Image URLs for graph nodes
            icons = {award_data[0]: "icons/" + award_data[2]}

            # Load images
            images = {k: PIL.Image.open(fname) for k, fname in icons.items()}

            award = Award(name=award_data[0], points=int(award_data[1]))
            self._awards[award_data[0]] = award
            network.add_node(award, image=images[award_data[0]])

    def add_achieves(self, player_data: list[list[str | int]], award_data: list[list[str | int]],
                     network: nx.Graph) -> None:
        """Add all the achieve links between players and the awards that they have earned throughout their career

        Preconditions:
        - The inner lists is in the form of [name, age, status, start year, end year, hall of fame, ...]
        (rest of the list are award numbers which will not be used in this function)
        """
        for player in player_data:
            for i in range(0, 16):
                if int(player[i + 6]) != 0:
                    self._players[player[0]].achieve_award(self._awards[award_data[i][0]], int(player[i + 6]))
                    network.add_edge(self._players[player[0]], self._awards[award_data[i][0]])

    def players(self) -> dict:
        """Return the mapping of players' names and the BasketballPlayer object associated to that player"""
        return self._players

    def get_achieved_labels(self, graph: nx.Graph) -> dict[tuple, int]:
        """Returns a list of all edges and their respective number of awards won."""
        dict_so_far = {}
        for edge in graph.edges:
            for achieved in edge[1].awards.values():
                dict_so_far[(achieved.award, achieved.player)] = achieved.number

        return dict_so_far


if __name__ == '__main__':
    doctest.testmod()
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['PIL', 'distutils.util', 'networkx', 'node_edge_data_structure', 'Image'],
        'disable': ['unused-import'],
    })
