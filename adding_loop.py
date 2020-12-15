#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program lets user decide amount of number to be inputed and what numbers
# will be inputed and calculates the sum of the numbers entered


def main():
    # this program lets user decide amount of number to be inputed and what
    # numbers will be inputed and calculates the sum of the numbers entered
    total = 0

    # input, process & output
    while True:
        amount_of_numbers = input("How many numbers are you going to add: ")
        print("\n", end="")
        try:
            amount_of_numbers = int(amount_of_numbers)
            if amount_of_numbers > 0:
                while amount_of_numbers > 0:
                    try:
                        number_added = input("Enter an integer to add: ")
                        number_added = int(number_added)
                        if number_added > 0:
                            total = total + number_added
                            amount_of_numbers = amount_of_numbers - 1
                        else:
                            print("That was a negative integer and wont"
                                  " be added.")
                            amount_of_numbers = amount_of_numbers - 1
                            continue
                    except Exception:
                        print("That was not an integer.")
                break
            else:
                print("That was a negative integer."
                      " Please enter a positive integer")
                print("\n", end="")
        except Exception:
            print("That was not an integer. Try again.")
            print("\n", end="")
    print("The total is {0} ".format(total))


if __name__ == "__main__":
    main()
