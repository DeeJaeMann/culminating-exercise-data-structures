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
    elif n == 1 :
        # Smallest disk
        # Check if there are any existing moves
        if moves_list == [] :
            # There are none, move the disk to the destination
            str_this_move = f"Move disk {n} from {source} to {destination}"
            moves_list.append(str_this_move)
            return tower_of_hanoi(n-1, source, destination, auxiliary, moves_list)
        else :
            # Disk 1 should be in auxillary
            str_this_move = f"Move disk {n} from {auxiliary} to {destination}"
            moves_list.append(str_this_move)
            return tower_of_hanoi(n-1, source, destination, auxiliary, moves_list)
    elif n == 2 :
        # Second smallest disk
        # Check if there are any existing moves
        if moves_list == [] :
            # There are none, move disk 1 to auxilary
            str_this_move = f"Move disk {n-1} from {source} to {auxiliary}"
            moves_list.append(str_this_move)
            # Don't reset N, we still have 2 moves to complete
            return tower_of_hanoi(n, source, destination, auxiliary, moves_list)
        else :
            # Disk 1 is in aux, move disk 2 to destination
            str_this_move = f"Move disk {n} from {source} to {destination}"
            moves_list.append(str_this_move)
            # Decriment N to move the final disk
            return tower_of_hanoi(n-1, source, destination, auxiliary, moves_list)
    

# print(f"Test 0: {tower_of_hanoi(0, 'A', 'C', 'B', [])}")
# print(f"Test 1: {tower_of_hanoi(1, 'A', 'C', 'B', [])}")
print(f"Test 2: {tower_of_hanoi(2, 'A', 'C', 'B', [])}")
