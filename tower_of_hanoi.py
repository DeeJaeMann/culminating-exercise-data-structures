#!/usr/bin/env python3
"""
Tower of Hanoi problem. This file must have a function named `tower_of_hanoi`, which the test code will import and run.
DO NOT MODIFY the function name, the arguments it takes, or the format of the data it returns

Feel free to add print statements and call your function here as needed so you can write/run code as you are developing
and debugging your solution to the problem.
"""

def tower_of_hanoi(n, source, destination, auxiliary, moves_list):
    """Solves the Tower of Hanoi problem and returns a list of moves.

        Each 'rod' is named "A", "B", "C".
        "A" is always the first rod on the left, "B" is the rod in the middle, "C" is the last rod on the right.
        There are always exactly 3 rods.

        A "move" is a string in the following format:

        "Move disk 1 from A to B"
        "Move disk 3 from C to B"
        ... and so on. See tests.py for examples

        :param int n: Number of disks to be moved. Valid ranges of n: 0 <= n <= 5, though a correct implementation should handle values larger than 5.
        :param str source: The rod we are moving the disks from. Valid inputs: "A", "B", "C".
        :param str destination: The rod we are moving the disks to. Valid inputs: "A", "B", "C".
        :param str auxiliary: The rod used as an auxiliary (intermediate) rod during the process. Valid inputs: "A", "B", "C".
        :param list moves_list: A list to store the moves made during the Tower of Hanoi process. This list is updated recursively.

        :type n: int
        :type source: str
        :type destination: str
        :type auxiliary: str
        :type moves_list: list
        :return: The list of moves made to solve the Tower of Hanoi problem.
        :rtype: list
    """

    # Exit case n == 0
    if n == 0:
        return moves_list
    

print(tower_of_hanoi(0, "A", "C", "B", []))
