# Joshua Lemuel Z. Centina BS CPE 1-4
# Writing Multiple Line Contents

# Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output:
# Enter line: Beautiful is better than ugly.
# Are there more lines y/n? y
# Enter line: Explicit is better than implicit.
# Are there more lines y/n? y
# Enter line: Simple is better than complex.
# Are there more lines y/n? n 

# pseudocode
print("=" * 51)
print("\033[1;32mWelcome to Writing Multiple Lines of Text Contents!\033[0m")
print("=" * 51)
#define a function
def text():
# open mylife.txt (read) and write mode as text_input
    with open("mylife.txt", "w") as text_input:
# Welcome to this program
#"\033[1;xm\033[0m"
# use loop to execute the block of code repeatedly
        while True:
            line = input("Enter line: ")
            # write the input to mylife.txt
            text_input.write(line + "\n")
            add_line = input("Are there more lines y/n? ")
            if add_line.lower() != "y":
                break
# print the output
    print("=" * 51)
    print("\033[1;36mInputted lines: \033[0m")
    with open("mylife.txt") as text_input:
        #read each line by line
        for line in text_input:
            print(line.strip())
    print("=" * 51)
# close the file

text()