'''The treasure island game
'''

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go?\n    Type 'left' or 'right'\n")

if direction == "left":
    transport = input("You've come to a lake. There is an island in the middle of the lake.\n   Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
else:
    print("You fell into a hole. Game over!")

if transport == "swim":
    print("You get attacked by an angry trout. Game over!")
else:
    colour = input("You arive at the island unharmed. There is a house with 3 doors.\n   One red, one yellow, and one blue.\n Which colour do you chose?\n")

if colour == "red":
    print("It's a room full of fire. Game over!")
elif colour == "blue":
    print("You enter a room full of beasts. Game over!")
else:
    print("You found the treasure! You win!")