print("WELCOME TO THE TREASURE ISLAND GAME. YOUR MISSION IS TO FIND THE TREASURE")

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

middle = ""
door = ""

move = input(print("You are at a cross road. Where do you want to go? \n Type 'left' or 'right'"))

if move == "left":
  middle = input(print("You come to a lake. There is an island in the middle of the lake. Type 'swim' or 'wait' to proceed"))

  if middle == "wait":
    door = input(print("You arrive at the island unharmed.     There is a house with 3 doors. One red, one yellow and one   blue. Which colour do you choose?"))
  else:
    print("You were attacked by a trout. Game over")

  if door == "yellow":
    print("You win")
  elif door == "red":
    print("You were burned by fire. Game over")
  elif door == "blue":
    print("You were eaten by beasts. Game over")
  else:
    print("Game over")

else:
  print("You fell into a hole. Game over")
