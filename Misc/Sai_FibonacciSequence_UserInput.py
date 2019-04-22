# Fibonacci Sequence Code In Python
# Copyright © 2019, Sai K Raja, All Rights Reserved

x = input("What iteration/root in the fibonacci seqeunce do you want?")

print("0") #Starting Fibonacci Sequence with a zero (optional)

def fibonacci_sequence(a):  #Creating Fibonacci Sequence Function


    if a == 1:   #Starting value (after zero) for Fibonacci Sequence
        return 1

    if a == 2:  #Second value (after zero) in Fibonacci Sequence
        return 1

#The first two values in the Fibonacci Sequence are 1 and 1.

    return fibonacci_sequence(a-1) + fibonacci_sequence(a-2)

#This command builds on the new infinite values after 1 and 1 (the starting two values).

for i in range(1, int(x)):
    print(fibonacci_sequence(i))

#This prints the fibonacci sequence for the n-th value inputted by the user.

print("The last number shown is the " + str(x) + "th root of the fibonacci seqeunce.") #Answer message

input("Thank you for using my fibonacci seqeunce program.  if you would like to continue, press enter and run the program again.")

#Thanks and exit message