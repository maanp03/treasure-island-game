'''Python script for streamlit treasure island game'''


import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.write("Click the button below to begin the treasure hunt game")
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    st.write("## Welcome to Treasure Island.")
    st.write("##### Your mission is to find the treasure.")
    direction = st.radio(
    "You are at a cross road. Where do you want to go?",
    ["left", "right"], index=None, on_change=set_state, args=[2])
    if direction is None:
        set_state(1)

if st.session_state.stage >= 2:
    if direction == "left":
        transport = st.text_input(
        "You've come to a lake. There is an island in the middle of the lake.\
            \n   Type 'wait' to wait for a boat. Type 'swim' to swim across.",
            on_change = set_state, args=[3])
        if st.session_state.stage >=3:
            if transport == "wait":
                door_colour = st.selectbox(
                    "You arrive at the island unharmed. There is a house with 3 doors.\
                        \n  One red, one yellow, and one blue. Which colour do you choose?",
                        ("red", "yellow", "blue"), on_change = set_state, args=[4],
                        index=None
                        )
                if st.session_state.stage >=4:
                    if door_colour == "red":
                        st.write("It's a room full of fire! GAME OVER!")
                        st.button("Start Over", on_click=set_state, args=[0])
                    elif door_colour == "blue":
                        st.write("You enter a room of beasts! GAME OVER!")
                        st.button("Start Over", on_click=set_state, args=[0])
                    else:
                        st.write("You found the treasure! YOU WIN!")
                        st.button("Start Over", on_click=set_state, args=[0])
            else:
                st.write("You get attacked by an angry trout. GAME OVER!")
                st.button("Start Over", on_click=set_state, args=[0])
        
    else:
        st.write("You fall into a hole. GAME OVER!")
        st.button("Start Over", on_click=set_state, args=[0])
