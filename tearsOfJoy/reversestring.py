"""
collect word
set reversed string to empty string
for each character in word
    add character to reversed string 
print reversed string
"""



words = input("Enter a word: ")
reversed_string = " "
for character in words:
    reversed_string = character + reversed_string
print(reversed_string)
