#!/usr/bin/env python3

print("Enter the first number:")
First_num = int(input().strip())
print("Enter the second number:")
Second_num = int(input().strip())

result = First_num * Second_num

print(f"{First_num} x {Second_num} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")