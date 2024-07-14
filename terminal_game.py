import random
import sys

#PRESENTATION
print("Hello, you are on the mars space station and you will try to survive a breach!")
print("You can chose Normal mode or Hardcore mode.")
print("In Normal mode, you start at 100HP, 100 FOOD and 100 WATER.")
print("In Hardcore mode, you start at 30HP, 10 FOOD and 10 WATER.")
print("Some actions will require food and/or water, while you have a chance to get back some of it after each action you make.")
print("While at or under 0 food and/or water, you will lose HP each round.")
print("You die at 0HP and lose the game, GLHF !")
print("IMPORTANT NOTE : Please only use integers, escape mars space station is still in beta!")

#VARIABLES START
codetoguess = random.randint(0,9)
codetoguess2 = random.randint(10,99)
hp = 0
food = 0
water = 0

#GAMEMODE CHOICE
gamemode = int(input("Type 1 for Normal mode, 2 for Hardcore mode : "))
if gamemode == 1:
    hp = 100
    food = 100
    water = 100
elif gamemode == 2:
    hp = 30
    food = 10
    water = 10
else:
    print("Wrong input!")
#LUCK FUNCTION RANDOMLY GETS U EXTRA HP OR FOOD AND WATER
def luck():
    global food, water, hp
    if gamemode ==1:
        luck = random.randint(1,10)
        luck2 = random.randint(1,10)
        if luck == 1:
            food +=50
            water +=50
            print("You got lucky! +50 food and water")
            if luck2 == 1:
                hp +=30
                print("You got lucky! +30hp")
            if luck != 1 and luck2 != 1:
                print("You didn't have luck this time :(")
                print("You have", food, "food and", water, "water!")

#CHECK FUNCTION IF U DIED OR NOT
def check():
    global food, water, hp
    if food<0 or water<0: #STATS UPDATE
        hp -=20
    if hp>0: #ANNOUNCE
        print("You have",food, "food!")
        print("You have", water, "water!")
        print("You have ", hp, "hp!")
    else:
        print("You died! Try again!")
        sys.exit() #TO STOP THE PROGRAM ONCE YOU DIED
    
#STEP 1
print("You are on the mars space station, there is a breach in sector a, you need to go back to earth ASAP !")
print("You have 2 paths to the emergency space shuttle!")
print("Option 1 : Follow the safe but long path.")
print("Option 2 : Follow the short but tricky path.")
path1 = int(input('What will you chose? (1-2): '))
#PATH 1 1ST CHOICE
if path1 == 1: 
    luck()
    print("You walk a long corridor, losing 50 food and water!")
    print("Reminder : while at or below 0 food or water, you lose hp!")
    food -= 50
    water -= 50
    check()
    print("You now can try to guess the code to the final door (0 to 10) or climb a long ladder that takes a lot of energy but avoids the code guessing!")
    path2 = int(input("Do you chose option 1 or 2 ? "))
    if path2 == 1: #PATH 1 2ND CHOICE
        guess = int(input("Which number do you try ? "))
        while guess != codetoguess:
            luck()
            print("Wrong code! You lose 30 food and 30 water!")
            food -=30
            water -=30
            check()
            guess = int(input("Which number do you try ? "))
        else :
            print("You escaped! Well done!")
    elif path2 == 2: #PATH 1 2ND CHOICE 2
        luck()
        print("After climbing the ladder, you lost 50 food and water!")
        food -=50
        water -=50
        check()
        print("You can try to guess the code to another final door (0 to 10) or climb another ladder that takes a lot of energy and a random number of hp but avois the code guessing and gets you in the shuttle!")
        path3 = int(input("Do you chose option 1 or 2 ?"))
        if path3 ==1: #PATH 1 3RD CHOICE
            guess = int(input("Which integer do you try ? "))
            while guess != codetoguess:
                luck()
                print("Wrong code! You lose 30 food and 30 water!")
                food -=30
                water -=30
                check()
                guess = int(input("Which number do you try ? "))
            else :
                print("You escaped! Well done!")
        elif path3 == 2: #PATH 1 3RD CHOICE 2
            luck()
            die = random.randint(0,100)
            hp -= die
            print("After climbing the ladder, you lost 50 food and water")
            print("You also lost", hp, "hp!")
            food -=50
            water -=50
            check()
            print("You escaped! Well done!")
        else:
            print("Wrong input!")
    else: #ERROR PREVISION, I THINK IF U PUT IN SMTH ELSE THAN AN INTEGER IT GETS AN ERROR BUT I GUESS ITS FINE FOR NOW
         print("Wrong input!")
#PATH 2
elif path1 == 2 : 
    print("There is a code lock a door with a 2 digit number.")
    guess2 = int(input("Which integer do you try ? "))
    while guess2 != codetoguess2: #CONTINUE UNTIL GOOD CODE
        luck()
        print("Wrong code! You lose 30 food and 30 water!")
        food -=30
        water -=30
        check()
        guess2 = int(input("Which integer do you try ? "))
    else: #2ND STEP : LITTLE MATH QUESTION
        print("You now have to answer a math question to enter the shuttle!")
        print("What is the integral of 1/x on [1;3] ? ")
        print("1) ln 2")
        print("2) ln 3")
        print("3) 1/3") 
        guess3 = int(input("Which answer do you chose ? "))
        if guess3 == 2:
            print("You escaped! well done! Nice math!")
        else:
            print("Wrong answer! You don't know simple math, you deserve to die for that! Try again the whole game!") #FUN ANSWER
            sys.exit()
else:
    print("Wrong input!")
    