import textwrap

first_input = input("Enter the first chapter : ")
first_pages_number = input("Enter the number of pages : ")

secont_input = input("Enter the second chapter : ")
second_pages_number = input("Enter the number of pages : ")

third_input = input("Enter the third chapter : ")
third_pages_number = input("Enter the number of pages : ")

width = 30

print("\n Table of contents ...")
print(first_input.ljust(width), first_pages_number.rjust(width))
print(secont_input.ljust(width), second_pages_number.rjust(width))
print(third_input.ljust(width), third_pages_number.rjust(width))
