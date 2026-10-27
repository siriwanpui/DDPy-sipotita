#!/usr/bin/env python3
first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))

print(first_number, "x", second_number, "=", first_number * second_number)

result=first_number * second_number
if result>0:
    print("The result is positive")
elif result<0:
    print("The result is negative")
else:
    print("The result is postive and negative")
