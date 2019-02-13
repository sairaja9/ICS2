# Fibonacci Sequence Code In Python
# Copyright © 2019, Sai K Raja, All Rights Reserved

nth_root = input("Are you looking for a specific iteration or root of the fibonacci sequence?...If not, type 0")

def fibonacci_sequence(n):  #Creating Fibonacci Sequence Function
    

    if n == 1:   #Starting value for Fibonacci Sequence
        return 1

    if n == 2:  #Second value in Fibonacci Sequence
        return 1

#The first two values in the Fibonacci Sequence are 1 and 1.

    return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

#This command builds on the new infinite values after 1 and 1 (the starting two values).

def print_sequence1():
    for i in range(1, int(nth_root)):
        print(fibonacci_sequence(i))
    print("The last number in this printed sequence is the " + str(nth_root) + "th root.")


for i in range(0):
    print(number)

number = fib_question



# This for loop specifies the number of iterations python will complete.  
# In other words, If you want the 15th number in the Fibonacci Sequence:
# make the maximum range 15 python will run the program and give you the 15th iteration or loop.

    #while number == fibonacci_sequence(i):
     #   print(number + "is in the fibonacci seqeunce")