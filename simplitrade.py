import streamlit as st
import math

st.title('Simplitrade Calculator')

# Constants
sl = 40
sl_per_lot = sl * 15

# User Inputs
risk = st.number_input("Enter risk amount:", min_value=0.0, step=100.0, format="%.2f")
premium = st.number_input("Enter premium price:", min_value=0.0, step=100.0, format="%.2f")
if risk > 0:
    lots = math.floor(risk / sl_per_lot)
    st.write("Total Lots you can trade:", lots)
    st.write(f"Premium price is {premium}")
    margin_needed = premium * lots * 15
    st.write(f"You need {margin_needed} margin in your account")
else:
    st.write("Please enter a valid risk amount to calculate.")
