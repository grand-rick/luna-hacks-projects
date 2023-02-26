import streamlit as st
import random

st.set_page_config(page_title="Guess the Number", page_icon="🔢")

st.title("Guess the Number")

# Define the game logic
def play_game():
    secret_number = random.randint(1, 100)
    num_guesses = 0
    st.write("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while True:
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100)
        num_guesses += 1

        if guess < secret_number:
            st.write("Too low! Guess again.")
        elif guess > secret_number:
            st.write("Too high! Guess again.")
        else:
            st.write(f"Congratulations, you guessed the number in {num_guesses} guesses!")
            break

# Define the user interface
player_name = st.text_input("Enter your name:")
st.write(f"Hello, {player_name}!")
st.write("Let's play Guess the Number.")

if st.button("Start Game"):
    play_game()

st.write("Thanks for playing!")
