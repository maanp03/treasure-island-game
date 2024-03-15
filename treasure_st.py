'''Python script for streamlit treasure island game'''

import streamlit as st

st.write("## Welcome to Treasure Island.\nYour mission is to find the treasure.")
st.write("##### Your missions is to find the treasure")

direction = st.radio(
    "You are at a cross road. Where do you want to go?",
    ["left", "right"])

if direction == "left":
    transport = st.text_input(
        "You've come to a lake. There is an island in the middle of the lake.\
            \n   Type 'wait' to wait for a boat. Type 'swim' to swim across."
    )

    if transport == "wait":
        door_colour = st.selectbox(
            "You arrive at the island unharmed. There is a house with 3 doors.\
                \n  One red, one yellow, and one blue. Which colour do you choose?",
                ("red", "yellow", "blue")
        )
        if door_colour == "red":
            st.write("It's a room full of fire! GAME OVER!")
        elif door_colour == "blue":
            st.write("You enter a room of beasts! GAME OVER!")
        else:
            st.write("You found the treasure! YOU WIN!")

    else:
        st.write("You get attacked by an angry trout. GAME OVER!")

else:
    st.write("You fall into a hole. GAME OVER!")
