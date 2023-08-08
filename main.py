"""CSC111 Final Report: The National Basketball Association’s Statistically Best Players Main Module

Description
===============================

This module contains the main functions and variables which will be used throughout the program. This is also the
module which will be run. The module includes a runner function which will load the data sets, create the graphs and
also includes the button system which is used for our GUI. This includes the many button callbacks which are used to
call the other functions from other modules which will be executed when the specific button is pressed. Finally, the
main block is what runs the entire code and holds the main button system loop.

Copyright
===============================

This file is Copyright (c) 2023 Vincent Louie and Junwei Quan.
"""

from __future__ import annotations

import tkinter
import tkinter.messagebox
from typing import Any

import networkx as nx
import draw_graph

from data_reader import read_csv_file
from network_data_structure import AwardNetwork
from draw_graph import draw_network, filter_graph


def filter_200_callback() -> Any:
    """Filter graph for 200 points using this method for the button callback."""
    return filter_graph(state.current_graph, 200)


def filter_400_callback() -> Any:
    """Filter graph for 400 points using this method for the button callback."""
    return filter_graph(state.current_graph, 400)


def filter_600_callback() -> Any:
    """Filter graph for 600 points using this method for the button callback."""
    return filter_graph(state.current_graph, 600)


def filter_800_callback() -> Any:
    """Filter graph for 200 points using this method for the button callback."""
    return filter_graph(state.current_graph, 800)


def filter_mvp_callback() -> Any:
    """Filter graph for players who have won a Most Valuable Player award before."""
    return filter_graph(state.current_graph, filtered_award="Michael Jordan Most Valuable Player")


def filter_fmvp_callback() -> Any:
    """Filter graph for players who have won a Finals Most Valuable Player award before."""
    return filter_graph(state.current_graph, filtered_award="Bill Russell NBA Finals MVP")


def filter_dpoy_callback() -> Any:
    """Filter graph for players who have won a Defensive Player of the Year award before."""
    return filter_graph(state.current_graph, filtered_award="Hakeem Olajuwon Defensive Player Of The Year")


def filter_smoy_callback() -> Any:
    """Filter graph for players who have won a Sixth Man of the Year award before."""
    return filter_graph(state.current_graph, filtered_award="John Havlicek Sixth Man Of The Year")


def filter_mip_callback() -> Any:
    """Filter graph for players who have won a Most Improved Player award before."""
    return filter_graph(state.current_graph, filtered_award="George Mikan Most Improved Player")


def filter_roty_callback() -> Any:
    """Filter graph for players who have won a Rookie of the Year award before."""
    return filter_graph(state.current_graph, filtered_award="Wilt Chamberlain Rookie Of The Year")


def filter_1950_callback() -> Any:
    """Filter graph for players who were drafted in the 50's."""
    return filter_graph(state.current_graph, filtered_year=1950)


def filter_1960_callback() -> Any:
    """Filter graph for players who were drafted in the 60's."""
    return filter_graph(state.current_graph, filtered_year=1960)


def filter_1970_callback() -> Any:
    """Filter graph for players who were drafted in the 70's."""
    return filter_graph(state.current_graph, filtered_year=1970)


def filter_1980_callback() -> Any:
    """Filter graph for players who were drafted in the 80's."""
    return filter_graph(state.current_graph, filtered_year=1980)


def filter_1990_callback() -> Any:
    """Filter graph for players who were drafted in the 90's."""
    return filter_graph(state.current_graph, filtered_year=1990)


def filter_2000_callback() -> Any:
    """Filter graph for players who were drafted in the 2000's."""
    return filter_graph(state.current_graph, filtered_year=2000)


def filter_2010_callback() -> Any:
    """Filter graph for players who were drafted in the 2010's."""
    return filter_graph(state.current_graph, filtered_year=2010)


def draw_graphs_for_button() -> None:
    """Draws the graph when the button is clicked."""
    draw_network(state.current_graph)


def draw_graphs_label_for_button() -> None:
    """Draws the graph with label when the button is clicked."""
    draw_network(state.current_graph, network_graph.get_achieved_labels(state.current_graph))


def show_full_point_scoreboard(network: AwardNetwork) -> None:
    """Shows the full point total scoreboard with all 80 players."""
    all_points = []
    for player_name, player in network.players().items():
        total_points = player.get_total_points()
        all_points.append((total_points, player_name))

    all_points.sort(reverse=True)
    text = ""
    for player in all_points:
        text += f"{player[1]}: {player[0]} points\n"

    tkinter.messagebox.showinfo("Point Total Scoreboard for all players", text)


def scoreboard_callback() -> None:
    """Function for the button to call the show_full_point_scoreboard function."""
    show_full_point_scoreboard(network_graph)


def instruction_callback() -> None:
    """Pop up a new window which has the instructions for how to use the GUI."""
    tkinter.messagebox.showinfo("Instructions", "This is the Graphical User Interface for our graph visualization. "
                                                "There are three main types of filters for the graph, which are "
                                                "point filters that filter players who have more than a specific "
                                                "amount of points, award filter which filters to a specific type of "
                                                "award that can be won and finally, year filter which will filter the "
                                                "graph to players who were drafted in that specific decade (if the "
                                                "filter says 1990 then this means anyone drafted from 1990-1999). "
                                                "You are able to use ONE of the filter buttons for each type, meaning "
                                                "you can filter for one specific point minimum, one specific award "
                                                "and one specific time period. As well, you can do a combination of "
                                                "any of these three filters but only select ONE from each type. "
                                                "After this, you can use the Draw graph button to make the graph "
                                                "visualization. In order to do other filters after this, click the "
                                                "reset graph button and then refilter the graph. Another option is "
                                                "using the Draw graph with labels button which will add labels to the "
                                                "edges of the graph, representing the number of that specific award "
                                                "that the player has won. If the numbers are hard to see then you can "
                                                "zoom in to the graph using the controls on the top of the plot "
                                                "window. Enjoy!")


def runner() -> AwardNetwork:
    """Create a simulation of the AwardNetwork using the player_data.csv file for player data and award_data.csv
    for award data. Then we will return this AwardNetwork
    """
    players_data = read_csv_file("player_data.csv")
    awards_data = read_csv_file("award_data.csv")

    network = AwardNetwork()
    network.add_awards(awards_data, graph)
    network.add_players(players_data, graph)

    network.add_achieves(players_data, awards_data, graph)

    return network


if __name__ == '__main__':
    graph = nx.Graph()

    network_graph = runner()

    state = draw_graph.VisualizationState(graph)

    top = tkinter.Tk()
    top.title("NBA Player and Award Graph Filtering and Visualization Options")
    top.geometry('600x600')
    filter_info_button = tkinter.Button(top, text="Instructions", command=instruction_callback)
    filter_200_button = tkinter.Button(top, text="Filter to 200 points", command=filter_200_callback)
    filter_400_button = tkinter.Button(top, text="Filter to 400 points", command=filter_400_callback)
    filter_600_button = tkinter.Button(top, text="Filter to 600 points", command=filter_600_callback)
    filter_800_button = tkinter.Button(top, text="Filter to 800 points", command=filter_800_callback)
    filter_mvp_button = tkinter.Button(top, text="Filter to Most Valuable Player Award",
                                       command=filter_mvp_callback)
    filter_fmvp_button = tkinter.Button(top, text="Filter to Finals Most Valuable Player Award",
                                        command=filter_fmvp_callback)
    filter_dpoy_button = tkinter.Button(top, text="Filter to Defensive Player of the Year Award",
                                        command=filter_dpoy_callback)
    filter_smoy_button = tkinter.Button(top, text="Filter to Sixth Man of the Year Award",
                                        command=filter_smoy_callback)
    filter_mip_button = tkinter.Button(top, text="Filter to Most Improved Player Award",
                                       command=filter_mip_callback)
    filter_roty_button = tkinter.Button(top, text="Filter to Rookie of the Year Award",
                                        command=filter_roty_callback)
    filter_1950_button = tkinter.Button(top, text="Filter players who got drafted in 1950's",
                                        command=filter_1950_callback)
    filter_1960_button = tkinter.Button(top, text="Filter players who got drafted in 1960's",
                                        command=filter_1960_callback)
    filter_1970_button = tkinter.Button(top, text="Filter players who got drafted in 1970's",
                                        command=filter_1970_callback)
    filter_1980_button = tkinter.Button(top, text="Filter players who got drafted in 1980's",
                                        command=filter_1980_callback)
    filter_1990_button = tkinter.Button(top, text="Filter players who got drafted in 1990's",
                                        command=filter_1990_callback)
    filter_2000_button = tkinter.Button(top, text="Filter players who got drafted in 2000's",
                                        command=filter_2000_callback)
    filter_2010_button = tkinter.Button(top, text="Filter players who got drafted in 2010's",
                                        command=filter_2010_callback)
    scoreboard_button = tkinter.Button(top, text="Show Total Point Scoreboard", command=scoreboard_callback)
    draw_button = tkinter.Button(top, text="Draw graph", command=draw_graphs_for_button)
    draw_with_label_button = tkinter.Button(top, text="Draw graph with labels",
                                            command=draw_graphs_label_for_button)
    reset_button = tkinter.Button(top, text="Reset graph", command=state.reset_to_original_graph)
    filter_info_button.pack()
    filter_200_button.pack()
    filter_400_button.pack()
    filter_600_button.pack()
    filter_800_button.pack()
    filter_mvp_button.pack()
    filter_fmvp_button.pack()
    filter_dpoy_button.pack()
    filter_smoy_button.pack()
    filter_mip_button.pack()
    filter_roty_button.pack()
    filter_1950_button.pack()
    filter_1960_button.pack()
    filter_1970_button.pack()
    filter_1980_button.pack()
    filter_1990_button.pack()
    filter_2000_button.pack()
    filter_2010_button.pack()
    scoreboard_button.pack()
    draw_button.pack()
    draw_with_label_button.pack()
    reset_button.pack()
    top.mainloop()

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120,
    #     'extra-imports': ['networkx', 'draw_graph', 'tkinter', 'tkinter.messagebox', 'data_reader',
    #                       'network_data_structure', 'draw_graph'],
    #     'disable': ['unused-import'],
    #     'allowed-io': ['read_packet_csv', 'part3_runner_optional']
    # })
