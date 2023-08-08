"""CSC111 Final Report: The National Basketball Association’s Statistically Best Players Data Reader Module

Description
===============================

This module contains a function which is used to read the data set that will be used in our program. This will take the
csv file and read it, turning it into a list of lists of strings or integers which can be easily manipulated by the
other modules.

Copyright
===============================

This file is Copyright (c) 2023 Vincent Louie and Junwei Quan.
"""

import csv
import doctest


def read_csv_file(file: str) -> list[list[str | int]]:
    """Read the csv file of the NBA Top 75 Player Awards and store in a list to return.

    Preconditions:
        - file is a string which is the path to a csv file
    """
    data = []

    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            data.append(row)

    return data


if __name__ == '__main__':
    doctest.testmod()
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['csv'],
        'disable': ['unused-import'],
        'allowed-io': ['read_csv_file']
    })
