'''
Ask the user a bunch of questions and every time they get it right,
add a number to their score
Give the player their score when they quit the game
'''
# greet the player
print("Welcome to my quiz game!")

# find out if they want to play
playing = input("Do you want to play the game? Y or N ")

# what do we do with their answer?
if playing.lower() != 'y':
    quit()

# what happens when they say yes
print("Okay, let's play! ")
score_tally = 0

# ask the first question
answer1 = input("What colour is the sky? ")
if answer1.lower() == "blue":
    score_tally += 1
    print('That is correct, you earn one point!')
else:
    print("incorrect")

answer2 = input("What does KFC stand for? ")
if answer2.lower() == "kentucky fried chicken":
    score_tally += 1
    print('Correct!')
else:
    print("incorrect")

answer3 = input("What is the opposite of left? ")
if answer3.lower() == "right":
    score_tally += 1
    print('Correct!')
else:
    print("incorrect")

print("You answered " + str(score_tally) + " questions correct! \nThis is equal to " + str(score_tally/3*100) + "%. ")