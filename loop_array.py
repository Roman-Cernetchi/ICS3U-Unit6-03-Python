#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program prints 10 random integers and finds the smallest number

import random


def min_value(random_list):
    # This function finds the smallest number

    min_num = random_list[0]

    for loop_counter in random_list:
        if min_num <= loop_counter:
            continue
        elif min_num > loop_counter:
            min_num = loop_counter

    return min_num


def main():
    # This function prints 10 random integers and output

    random_list = []

    # process
    for loop_counter in range(0, 10):
        # random number
        random_number = random.randint(1, 100)
        random_list.append(random_number)
        print(random_number)

    # call function
    smallest_num = min_value(random_list)

    print("")
    print("The smallest number is: {0}".format(smallest_num))


if __name__ == "__main__":
    main()
