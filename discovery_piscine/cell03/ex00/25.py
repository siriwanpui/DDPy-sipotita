#!/usr/bin/env python3

print("Enter a number less than 25")
num_input=int(input())

if num_input>25:
    print("Error")

else:
    while num_input <=25:
        print(f"Inside the loop, my variable is {num_input}")
        num_input+=1

