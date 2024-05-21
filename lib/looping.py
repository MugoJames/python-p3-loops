#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print( "Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared_list = [x**2 for x in int_list]
    return squared_list


def fizzbuzz():
    # code goes here!
    for number in range(1 , 101):
        if number % 3 == 0 and number % 5 == 0:
            print( "FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
