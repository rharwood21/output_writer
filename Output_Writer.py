"""
Author: Riley Harwood
Last Edit: 12 September 2023
This module will be used as a helpful tool for making input test files in 605.621
"""
import random
from typing import TextIO

def process_files(outputFile: TextIO) -> None:
    """

    :param inputFile:
    :param outputFile:
    :return:
    """

    for i in range(1000):
        x = random.randrange(-100, 100)
        y = random.randrange(-100, 100)
        outputFile.write(f"{x},{y}\n")

