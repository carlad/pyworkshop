import sys

args = sys.argv

print(args)


name = input("Hello, what is your name? ")

birthday_string = input(f"Hello {name}. Please enter your birthday in MM/DD/YYYY format: ")

print(f"Hello {name}. Your birthday is on {birthday_string}.")
