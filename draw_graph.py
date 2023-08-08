"""CSC111 Final Report: The National Basketball Association’s Statistically Best Players Visualization Module

Description
===============================

This module is the module which does the visualizations for the graphs using the networkx and matplotlib packages. This
module also does the filtering for the graphs which allows the user to filter the graph to their preference and see
specific things about the graph in more detail. We also have a visualization state which helps the program know which
graph it should plot right now as the class holds the original graph and the current graph. The original graph is used
for resetting the graph for when the user wants to refilter or see the original graph again.

Copyright
===============================

This file is Copyright (c) 2023 Vincent Louie and Junwei Quan.
"""

import copy
import doctest
from typing import Optional
import networkx as nx
import matplotlib.pyplot as plt

from node_edge_data_structure import BasketballPlayer


class VisualizationState:
    """A class which stores the current graph and the original graph which includes all awards and players.
    This will allow us to create other graphs to filter and reset the graph.

    Instance Attributes:
        - original_graph: The original graph which includes all the awards and players and achieved edges
        - current_graph: The current graph which is used for drawing
    """
    original_graph: nx.Graph
    current_graph: nx.Graph

    def __init__(self, original_graph: nx.Graph) -> None:
        self.original_graph = original_graph
        self.current_graph = copy.deepcopy(original_graph)

    def reset_to_original_graph(self) -> None:
        """Resets the graph to the original graph with all players and awards."""
        self.current_graph = copy.deepcopy(self.original_graph)


def draw_network(network: nx.Graph, edge_labels: Optional[dict[tuple, int]] = None) -> None:
    """Draws the award network using images assigned to each node with an optional parameter which decides whether
    to draw the graph with edge labels or not."""
    pos = nx.spring_layout(network, seed=123456789, k=1.5)

    fig = plt.figure(figsize=(50, 30))
    ax = plt.subplot()

    nx.draw_networkx_edges(
        network,
        pos=pos,
        ax=ax
    )

    if edge_labels is not None:
        edge_list = list(edge_labels.keys())
        for edge in edge_list:
            if edge not in network.edges:
                edge_labels.pop(edge)

        nx.draw_networkx_edge_labels(
            network, pos,
            edge_labels=edge_labels,
            font_color='red',
            font_size=20
        )

    # Transform from data coordinates (scaled between xlim and ylim) to display coordinates
    tr_figure = ax.transData.transform
    # Transform from display to figure coordinates
    tr_axes = fig.transFigure.inverted().transform

    # Select the size of the image (relative to the X axis)
    icon_size = 0.05764957126405579
    icon_center = icon_size / 2.0

    # Add the respective image to each node
    for n in network.nodes:
        xf, yf = tr_figure(pos[n])
        xa, ya = tr_axes((xf, yf))
        # get overlapped axes and plot icon
        a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
        a.imshow(network.nodes[n]["image"])
        a.axis("off")

    plt.show()


def filter_graph(network: nx.Graph, points: Optional[int] = -1, filtered_award: Optional[str] = '',
                 filtered_year: Optional[int] = 0) -> nx.Graph:
    """Filters a networkx graph to the specific parameters given. The graph can either be filtered to a specific amount
    of points, filtered to a specific award or filtered to a speicific start year. The filter can either be one of the
    three given parameters or can be multiple, for example, filtering the graph to include players who got drafted in
    the 1990's who have won the MVP award and more than 600 points.

    Preconditions:
        - filtered_year must be the start of a decade year, i.e. 1950, 1960, 1970, etc.
        - filtered_award must be a valid award
    """
    node_list = list(network.nodes)
    for node in node_list:
        if isinstance(node, BasketballPlayer):
            if node in network.nodes:
                if node.get_total_points() < points:
                    network.remove_node(node)
                if filtered_year != 0 and node.start_year not in range(filtered_year, filtered_year + 10):
                    network.remove_node(node)
        else:
            if filtered_award not in {'', node.name}:
                network.remove_node(node)
    return network


if __name__ == '__main__':
    doctest.testmod()
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['copy', 'matplotlib.pyplot', 'networkx', 'Optional', 'node_edge_data_structure'],
        'disable': ['unused-import'],
    })
