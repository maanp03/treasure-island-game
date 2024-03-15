'''The treasure island game
'''

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go?\n    Type 'left' or 'right'\n")

if direction == "left":
    transport = input("You've come to a lake. There is an island in the middle of the lake.\
                      \n   Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if transport == "wait":
        door_colour = input("You arrive at the island unharmed. There is a house with 3 doors.\
                            \n  One red, one yellow, and one blue. Which colour do you choose?\n")
        if door_colour == "red":
            print("It's a room full of fire! GAME OVER!")
        elif door_colour == "blue":
            print("You enter a room of beasts! GAME OVER!")
        else:
            print("You found the treasure! YOU WIN!")

    else:
        print("You get attacked by an angry trout. GAME OVER!")

else:
    print("You fall into a hole. GAME OVER!")