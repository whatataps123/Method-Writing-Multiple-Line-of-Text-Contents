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
#define a function
def text():
# open mylife.txt (read) and write mode as text_input
    with open("mylife.txt", "w") as text_input:
# use loop to execute the block of code repeatedly
        while True:
            line = input("Enter line: ")
            # write the input to mylife.txt
            text_input.write(line + "\n")
            add_line = input("Are there more lines y/n? ")
            if add_line.lower() != "y":
                break
# print the output
        print("Inputted lines: ")
        for line in line:  
            print(line)
# close the file

text()