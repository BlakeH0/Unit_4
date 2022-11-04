'''
##########
Lab 4.02
##########

Part 1
----------
Write a function pluralize_words that takes in a list of words and updates the values of the list 
to make each one plural. It returns nothing.

Making plurals in English has a number of special cases, but for this lab we'll use a simple rule: 
if the word ends in a y remove the y and add ies; otherwise add an 's'.

We'll exercise the function on a list of words.

Create the function contract for pluralize_words.

Provide a few examples that confirm pluralize_words works as expected:

    Include examples with 'berry'

    What if the list is empty?

Example 1
----------
    # contract goes here
    def pluralize_words(word_list):
        # your code goes here
​
    word_list = ['apple', 'berry', 'melon']
    print(f"Singular words: {word_list}")
    pluralize_words(word_list)
    print(f"No longer singular words: {word_list}")
    # more examples go here

#######################################################
Here is what it should look like when you run your code:



singular_words = ["apple", "berry", "banana", "cherry", "plum"]
plural_words = []



def pluralize_word(list):
    for word in singular_words:
        last_letter = word[len(word) - 1]
        if last_letter == 'y':
            word = word[:-1] 
            plural_words.append(f"{word}ies")
        else:
            plural_words.append(f"{word}s")
    print(list)
    return plural_words

print(pluralize_word(singular_words))

#######################################################
Singular words: ['apple', 'berry', 'melon']
No longer singular words: ['apples', 'berries', 'melons']

Hint
-----
Remember that you can index into the string and get the length of a string. Use that to get the last letter of each word.

Part 2
------
Create a function my_reverse, which will return a reversed string.

Create the function contract for my_reverse.

Provide a few examples to confirm that my_reverse works:

    An empty string

    A string of even length

    A string of odd length greater than 1

    A string of length 1

Example 2
---------
    # contract goes here
    def my_reverse(string_to_reverse):
        # your code goes here

    reversed = my_reverse("apples")
    print(reversed)
    # examples go here

##############################################################


Here is what example 2 should look like when you run your code:



##############################################################
    selppa

Hint 2
------
To get the last element:(len(my_list) -1) - 0 
To get the second to last element: (len(my_list)-1 ) - 1 
To get the third to last element: (len(my_list)-1) - 2

Extension
---------
Create a function reverse_strings_in_list. This function will input a list of strings you want to reverse. 
The function will reverse the strings in the list by calling the my_reverse function in a loop.
'''

# BLAKE HARRINGTON 
def my_reverse(word):
    new_word = ""
    for letters in word:
        new_word = letters + new_word
    return new_word
    
reversed_word = my_reverse("apples")
print(reversed_word)
reversed_word = my_reverse("")
print(reversed_word)
reversed_word = my_reverse("sharp")
print(reversed_word)
reversed_word = my_reverse("a")
print(reversed_word)


word_list = ["Cat", "Millions", "", "I", "Whispering"]

def reverse_strings_in_list(list):
    reversed_list = []
    for words in word_list:
        reversed_list.append(my_reverse(words))
    return reversed_list

new_list = reverse_strings_in_list(word_list)
print(new_list)

