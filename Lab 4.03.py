'''
###########
Lab 4.03
###########

Instructions
In this lab we will be drawing images using nested for loops.

For each of the following problems, you will write a function that will draw the desired output. You may use an extra function if you find it helpful.

1.  Write a function, draw_7, to draw the 7x7 square (shown below)

    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
2.  Write a function stars_and_stripes, that will draw a 3 sets of rows. 1st a row of 7 stars followed by a row of 7 dashes (shown below)

    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
3.  Write a function, increasing_triangle that will print out the following:

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7

4. Write a function, vertical_stars_and_stripes that will print out the following:

    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -

5.  Use a function to create your own pattern or drawing. Some possible pattern ideas:

    Write a function that will print a border around a 7x7 square (shown below)

        * * * * * * * *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * * * * * * * *
    Write a function that will print the following balanced_triangle.

        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    Write a function that will print the following triangle.

        *
        ***
        *****
    
'''




# Draw Funtion
def draw():
    picture = ""
    for i in range(0, 6):
        picture += " *"

# 7x7 Square Function
def draw_7():
    for i in range(0, 7):
        drawing = ""
        for j in range (0, 7):
            drawing += " *"

        print(drawing)

# Stars And Stripes Function
def stars_and_stripes():
    for i in range(0, 3):
        drawing = ""
        for j in range (0, 6):
            drawing += " *"
        print(drawing)
        drawing = ""
        for k in range(0, 6):
            drawing += " -"
        print(drawing)


# Increasing Triangle Function
def increasing_triangle():
    for i in range(0, 1):
        number = ""
        for j in range (0, 1):
            number = " 1"
            print(number)
            for k in range(0, 1):
                number += " 2"
                print(number)
                for l in range(0, 1):
                    number += " 3"
                    print(number)
                    for m in range(0, 1):
                        number += " 4"
                        print(number)
                        for n in range(0, 1):
                            number += " 5"
                            print(number)
                            for o in range(0, 1):
                                number += " 6"
                                print(number)
                                for p in range(0, 1):
                                    number += " 7"
                                    print(number)

# Vertical Stars And Stripes Function
def vertical_stars_and_stripes():
    for i in range(0, 7):
        art = "-"
        for j in range(0, 3):
            art += " *"
            for k in range(0, 1):
                art += " -"
        print(art)


# My Design Fucntion
def my_design():
        number = ""
        for a in range(0, 1):
            number += " a"
            print(number)
        for b in range (0, 1):
            number += " b"
            print(number)
        for c in range(0, 1):
            number += " c"
            print(number)
        for d in range(0, 1):
            number += " d"
            print(number)
        for e in range(0, 1):
            number += " e"
            print(number)
        for f in range(0, 1):
            number += " f"
            print(number)
        for g in range(0, 1):
            number += " g"
            print(number)
        for h in range(0, 1):
            number += " h"
            print(number)
        for i in range(0, 1):
            number += " i"
            print(number)
        for j in range(0, 1):
            number += " j"
            print(number)
        for k in range(0, 1):
            number += " k"
            print(number)
        for l in range(0, 1):
            number += " l"
            print(number)
        for m in range(0, 1):
            number += " m"
            print(number)
        for n in range(0, 1):
            number += " n"
            print(number)
        for o in range(0, 1):
            number += " o"
            print(number)
        for p in range(0, 1):
            number += " p"
            print(number)
        for q in range (0, 1):
            number += " q"
            print(number)
        for r in range(0, 1):
            number += " r"
            print(number)
        for s in range(0, 1):
            number += " s"
            print(number)
        for t in range(0, 1):
            number += " t"
            print(number)
        for u in range(0, 1):
            number += " u"
            print(number)
        for v in range(0, 1):
            number += " v"
            print(number)
        for w in range(0, 1):
            number += " w"
            print(number)
        for x in range(0, 1):
            number += " x"
            print(number)
        for y in range (0, 1):
            number += " y"
            print(number)
        for z in range(0, 1):
            number += " z"
            print(number)

design = input("Which design would you like to see? (Enter a corresponding number) \n"
"1. Draw 7\n"
"2. Stars and Stripes \n"
"3. Increasing Triangle\n"
"4. Vertical Stars and Stripes\n"
"5. My Design \n ")
if design == "1":
    print()
    draw_7()
elif design == "2":
    print()
    stars_and_stripes()
elif design == '3':
    print()
    increasing_triangle()
elif design == '4':
    print()
    vertical_stars_and_stripes()
elif design == '5':
    print()
    my_design()
else:
    print("Please enter a single number!")


# stars_and_stripes()
# draw_7()
# increasing_triangle()
# vertical_stars_and_stripes()
# my_design()