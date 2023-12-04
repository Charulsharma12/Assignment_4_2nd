#Write a Python program to triple all numbers of a given list of integers. Use Python map.

numbers = list(map(int, input('Enter numbers in a list:')))

tripled_numbers = list(map(lambda x: x*3, numbers))

print(tripled_numbers)