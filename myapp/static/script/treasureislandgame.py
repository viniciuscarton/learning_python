print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
c1 = input("You are at a crossroad. Pick a direction! (L or R)")
if c1 == "L":
    c2 = input("There is a river ahead. The tide is hide, will you wait or swim (W or S)?")
    if c2 == "W":
        c3 = input("You found a big house (yes, in the middle of the island). In the hallway, there are three doors, red, blue and yellow. Which one would you try (R, B or Y)?")
        if c3 == "R":
            print("It is burning. You are in Hell. Literally. May Fire Walk With You.")
        elif c3 == "B":
            print("GLOOP GLOOP. You are drowning because you just stepped in Atlantis.. Unlucky you.")
        elif c3 == "Y":
            print("YASSSSSS you did it! You win!!!! Now get this gold and get out of this island.")
        else:
            print("Nothing. Just nothing. A white, endless, void. Game over, enjoy the eternity here, loser.")
    else:
        print("A SHARK! (???) swallowed you. Game over, I guess...")
else:
    print("Aaaahhaaa a tree just fell over you! Game Over.")

