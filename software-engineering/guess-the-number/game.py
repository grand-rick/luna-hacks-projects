import streamlit as st
import random

# Set up the game
st.title("Guess the Number")
st.write("Welcome to the game of Guess the Number! Player 1 will choose a number between 1 and 100, and Player 2 will have 10 tries to guess the number.")

number = st.number_input("Player 1: Choose a number between 1 and 100", min_value=1, max_value=100, step=1)
guesses_left = 10
st.write("Player 2: You have", guesses_left, "guesses left.")

# Play the game
while guesses_left > 0:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    guesses_left -= 1

    if guess < number:
        st.write("Too low! You have", guesses_left, "guesses left.")
    elif guess > number:
        st.write("Too high! You have", guesses_left, "guesses left.")
    else:
        st.write("Congratulations, you guessed the number!")
        break

if guesses_left == 0:
    st.write("Sorry, you ran out of guesses. The number was", number)

