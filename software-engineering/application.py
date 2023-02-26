import pandas as pd
import streamlit as st

st.title("Budget Application")

income = st.number_input("Enter your income:", min_value=0.0, step=0.01)

expenses_df = pd.DataFrame(columns=["Expense", "Amount"])
num_expenses = st.number_input("Enter the number of expenses:", min_value=0, step=1)

for i in range(num_expenses):
    expense = st.text_input(f"Enter expense name #{i + 1}:", key=f"expense_{i}")
    amount = st.number_input(f"Enter expense amount #{i + 1}:", min_value=0.0, step=0.01, key=f"amount_{i}")
    expenses_df.loc[i] = [expense, amount]

st.write("Here is your budget:")
st.write("Income:", income)
st.write(expenses_df)

total_expenses = expenses_df["Amount"].sum()
remaining_balance = income - total_expenses

if remaining_balance > 0:
    st.write("Congratulations, you have a remaining balance of", remaining_balance)
elif remaining_balance == 0:
    st.write("You have no remaining balance.")
else:
    st.write("Warning: you have exceeded your income by", abs(remaining_balance))
