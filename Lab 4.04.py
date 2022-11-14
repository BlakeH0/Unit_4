'''
############
Lab 4.04
############

Part 1
-----------
The goal of this lab is to practice using and accessing items from lists of lists.

You have a few errands to run and have created a few shopping lists to help you remember what to buy. 
You stored your notes in a nested list, shopping_cart. This program will allow the user to ask for a 
specific item by its index or update what items are in the cart. The user can request to view list to 
see the items in a specific shopping list.

Shopping Lists
    shopping_lists = [
        ['toothpaste', 'q-tips', 'milk'],
        ['milk', 'candy', 'apples'],
        ['planner', 'pencils', 'q-tips']
    ]
User Inputs
1 - Update

The program asks which shopping list the user wants to update, which position it should update, and the new value to update.

2 - View Item

The program asks which shopping list the item is on and which position it occupies, then prints the item's name.

3 - View List

The program asks which shopping list the user wants and prints all of the items associated with that shopping list.

Functions
update_list

Takes in an integer representing the index of the shopping list, an integer representing the index of the item to update, and a string representing the new value for that item. Does not alter the length of the list.

print_item

Takes an int representing the index of the shopping list followed by an int representing the index of the item to print.

print_list

Takes an int representing the index of the shopping list to print.

Feel free to add more functions as you see fit.

Example
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 1
    Which shopping list would you like to update? 1
    Which item would you like to change? 2
    New value for item #2? cheese
    toothpaste, cheese, milk
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 2
    Which shopping list do you want to choose? 2
    Which item on list #2 do you want to see? 3
    apples
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 3
    Which shopping list would you like to see? 3
    planner, pencils, q-tips

# Blake Harrington

# Shopping Lists
shopping_lists = [
    ['toothpaste', 'q-tips', 'milk'],
    ['milk', 'candy', 'apples'],
    ['planner', 'pencils', 'q-tips']
    ]

# Invalid Input Message
invalid = ("Please input a valid number!")

# Update List Function
def update_list():
    global shopping_lists
    list = int(input("Which list would you like to change? "))
    if list > 0 and list < 4:
        spot = int(input("What item would you like to change? "))
        if spot > 0 and spot < 4:
            new = input(f"What item would you like to update item #{spot} with? ")
            shopping_lists[list - 1][spot - 1] = new
            print()
            print("Updated shopping list: ")
            for lists in shopping_lists:
                print(lists)
        else:
            print(invalid)
    else:
        print(invalid)
    pass


# View Item
def print_item():
    global shopping_lists
    view = int(input("Which shopping list would you like to choose? "))
    for i in range(1, len(shopping_lists) + 1):
        if view == i:
            item = int(input("What item would you like to see? "))
            if item in range(0, len(shopping_lists)):
                print(shopping_lists[view - 1][item - 1])
            else:
                print(invalid)
                return invalid
        else:
            print(invalid)
            return invalid 


    pass


# View List Function
def print_list():
    global shopping_lists
    view_list = int(input("Which shopping list would you like to choose? "))
    if view_list in range(1, 4):
            print(shopping_lists[view_list - 1])
    else:
        print(invalid)
        return invalid
    pass




running = True

while running: 
    print()
    choice = input("What would you like to do? \n"
    "1. Update Item \n"
    "2. View Item \n"
    "3. View List \n" )
    if choice == "1":
        print()
        update_list()
        pass
    elif choice == "2":
        print()
        print_item()
        pass
    elif choice == "3":
        print()
        print_list()
        pass
    else:
        print()
        print("Please enter a corresponding number! ")



Part 2
------------
In this part of the lab you will go through your shopping list program and perform a few different calculations.

Create a function, all_in_one, that will put all the shopping lists into a single combined list using a for loop.

Create a function, count_q_tips, which will go through all items of the list and keep a count of how many times 
'q-tips' occurs.

In order to make the shopping lists more calcium rich, write a function, drink_more_milk, that adds 'milk' to each 
of the lists (unless it's already there).

You can't have milk without cookies. Write a function if_you_give_a_moose_a_cookie, that will go through every 
element of shopping_cart and update 'milk' to be 'milk and cookies'.

# Blake Harrington


# Shopping Lists
shopping_lists = [
    ['toothpaste', 'q-tips', 'milk'],
    ['milk', 'candy', 'apples'],
    ['planner', 'pencils', 'q-tips']
    ]

all_lists = []

# All In One Function
def all_in_one():
    global all_lists
    global shopping_lists
    for l in shopping_lists:
        for i in range(0, len(shopping_lists)):
            all_lists.append(l[i])
    print(all_lists)
    pass

# Count Q Tips Function
def count_q_tips():
    counter = 0
    for i in all_lists:
        if i == "q-tips":
            counter += 1
    print(counter)
    pass

# Drink More Milk Function
def drink_more_milk():
    for a in range(0, len(shopping_lists)):
        for b in range(0, len(shopping_lists[a])):
            if "milk" not in shopping_lists[a]:
                shopping_lists[a][b] = "milk"    
        print(shopping_lists[a]) 

# If You Give A Mouse A Cookie Function
def if_you_give_a_mouse_a_cookie():
    for i in range(0, len(shopping_lists)):
        for b in range(0, len(shopping_lists)):
            if shopping_lists[i][b] == "milk":
                shopping_lists[i][b] += " and cookies"
        print(shopping_lists[i])
    pass


all_in_one()
count_q_tips()
drink_more_milk()
if_you_give_a_mouse_a_cookie()

Extension
-------------
Write a function to reverse the order of the lists, and also reverse the order of the items in each list, in the shopping_cart nested list.

The new reversed list should look like the following when printed (newlines and spacing added for clarity):

    shopping_cart = [
        ['q-tips', 'pencils', 'planner'],
        ['apples', 'candy', 'milk'],
        ['milk', 'q-tips', 'tooth paste']
    ]
Tip
Last item can be gotten by my_list[-1]

Second to last element: my_list[-2]

Third to last element: my_list[-3]

# Blake Harrington

# Shopping Lists
shopping_lists = [
    ['toothpaste', 'q-tips', 'milk'],
    ['milk', 'candy', 'apples'],
    ['planner', 'pencils', 'q-tips']
    ]

# print(shopping_lists[-1][-1])

# Reversed List Function
def reversed_list():
    shopping_lists.reverse()
    for a in range(0, len(shopping_lists)):
        shopping_lists[a].reverse()
        print(shopping_lists[a])
    

reversed_list()


'''

