'''
Users can create different versions of a story choosing between given options
that results in different scenarios for their named character. Each decision will send the character on a 
adventurous path that may end in either victory or their demise.
'''
character_name = input("Give your adventurer a name: ")

print("Welcome to " + str(character_name) + "'s story!" )

q1 = input(str(character_name) + " is stuck on a cold mountain top, some friends came to the rescue.  One by boat and one by helicopter, choose: 'boat' or 'heli'.")
if q1.lower() == 'boat':
    print(str(character_name) + " is on the boat safely and travelling downstream toward the base of the mountain.")
    print(str(character_name) + " notices a waterfall up ahead and has to make a decision fast! Grab onto a nearby tree root or ride it out?")
    q2 = input("Help " + str(character_name) + " choose fast by entering 'g' for grab root  or 'r' to ride it out. ")
    if q2.lower() == "g":
        print(str(character_name) + " managed to get to safety on the riverbank, but got a nasty cut on the right palm.  Better get that bandaged! ")
        q3 = input("Will " + str(character_name) + " make use of a soft piece of branch or an ivy leaf to patch up the cut? Enter 'b' for branch or 'i' for ivy.")
        if q3.lower() == 'b':
            print("Great job! Now let's get down this mountain!")
        elif q3.lower() == 'i':
            print("The Ivy was magical and healed the cut instantly.")
            print("Find a safe spot to get down to the river at the bottom of the waterfall.")
        else:
            print("The cut luckily formed a scab and the adventure continues on another day.")
            quit()
    elif q2.lower() == 'r':
        print("This is going to be a wild ride, hang on!")
        print(str(character_name) + " is plummeting down the waterfall and considers whether it is safer in the boat or to abandon it going down the waterfall.")  
        q4 = input("Choose 's' to stay in the boat or 'j' to jump out. ")
        if q4.lower() == 's':
            print("The boat cushions your fall and traps some air while the waterfall pushes you deep below.")
            print("Your attempts to swim downstream to get from under the waterfall is successful and your wash up on the river bank. /n Your friend is beside you. ")
            print("You walk together downstream and reach the safety of a nearby town.  What an adventure!")
            quit()
        elif q4.lower() == 'j':
            print("Jumping off the boat while going down the fall, gave the opportunity to get away from the base of the waterfall and land in the river below.")
            print("You reach the riverbank and after finding your friend and catching your breath, walk downstream to a nearby town.")
            quit()
    else:
        print(str(character_name) + " wakes up in sweat.  What a wild dream!")
        quit()
elif q1.lower() == 'heli':
    print("The helicopter flies to the nearest town and lands on the helipad.  This could have been a wild one, lucky for you!")
else:
    print('Looks like you are waiting for a miracle.  Wishing you all the best! /n the end ')
    quit()

