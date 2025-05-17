# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: May 16, 2025
# This program uses and array list and generates a random number 10 times
# Then it adds it to the list, then it calculates the average

import random


def main():
    # Declare the constants
    MAX_ARRAY_SIZE = 10
    MIN_NUM = 0
    MAX_NUM = 100

    # Create the array list
    list_of_int = []
    # For loop, in range of 0 to 9, so it will do it 10 times starting from 0
    for counter in range(MAX_ARRAY_SIZE):
        # Generate a random number between 0 and 100
        random_num = random.randint(MIN_NUM, MAX_NUM)

        # Store the random number in the array
        list_of_int.append(random_num)
        # Print the current counter and the random number added
        print(f"{random_num} added to the list at position {counter}")

    # Initialise sum to cero
    sum = 0
    # For loop for each individual number from the list calculate the average
    for counter in range(0, 10):
        # Set the sum to add all the numbers from the array
        sum = sum + list_of_int[counter]

    # calculation for average
    total = sum / MAX_ARRAY_SIZE
    print(f"{total}")


if __name__ == "__main__":
    main()
