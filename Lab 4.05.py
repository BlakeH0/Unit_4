'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])
​
    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program

After printing 6, it will print an error due to it being out of range of the list.

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program

The function is not being called, so nothing is going to be printed.

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.



'''

def print_numbers(list):
    for i in range(0, len(list)):
        print(list[i])

num_list = [1, 2, 3, 4, 5, 6]

def swapping_stars():
    line_str = ""
    for line in range(0, 6):
        for char in range(0,6):
            if line % 2 == char % 2:
                line_str += "*"
            else:
                line_str += "-"
    print(line_str)


choice = input("Which function would you like to run? \n"
"1. Print Numbers \n"
"2. Swapping Stars \n")

if choice == "1":
    print_numbers(num_list)
elif choice == "2":
    print()
    swapping_stars()
else:
    print("Please enter a valid number choice! ")