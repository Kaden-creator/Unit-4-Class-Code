'''
Name:
Date: 10/22/24
Description: Unit 4 Lesson 1 - while loops

'''

# While loops run while a condition is true
# we usually don't know how many times, this
# scenario is when they are most often used

'''

some_condition

while some_condition is true:
    code to execute
    update variable (if forgotten -> infinite loop)
'''

start_number = 10
while start_number > 0:
    print(start_number)
    start_number = start_number - 1

if start_number == 0:
    print("0")
    print("BLASTOFF!!")
# Change the code so it prints 10 9 ... 0 Blastoff!

# making a loop run to get user input

while True:
    user_age = int(input("Enter age or -1 to quit: "))
    if user_age == -1:
        break # exit the loop
    else:
        continue # return to top of loop