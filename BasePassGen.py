import random
import string
import time
import pyperclip

import streamlit as st


funny_quotes = [

    "This password is so strong, it does push-ups!",
    "Even your mom can't guess this one!",
    "This password will outlive a cockroach!",
    "Guard this password like it's your last slice of pizza!",
    "Better write this one down—it's practically a masterpiece!"
    "Your password is more complicated than assembling IKEA furniture."
    "Your password is now as secretive as a magician’s tricks.",
    "This password is so good, even the NSA would be impressed.",
    "This password is so secure, even Sherlock Holmes couldn’t deduce it.",
    "This password is more complicated than your love life.",
    "This password is stronger than your morning coffee.",
    "This password is more mysterious than the Bermuda Triangle.",
    "This password is harder to guess than the plot twist in a thriller.",
    "This password is harder to figure out than the meaning of life.",
    "This password is more confusing than your partner.",
    "This password is more secure than your emotional walls.",
]

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title("Random Password Generator")

length = st.slider("Select password length", min_value=8, max_value=30, value=12)

if st.button("Generate Password"):
    password = generate_random_password(length)
    st.write("Generated password:")
    #st.write(password)

    #i want to make font bigger using HTML
    st.write(f"<p style='font-size: 28px;'>{password}</p>", unsafe_allow_html=True)


    pyperclip.copy(password)

    # Temporary pop-up message for success
    success_placeholder = st.empty()
    success_placeholder.success("Password copied to clipboard!")

    # Wait for a few seconds
    time.sleep(3)

    st.write(random.choice(funny_quotes))

    # Clear the success message
    success_placeholder.empty()

#CSS to put my tagline below page
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        font-size: 17px;
        color: gray;
    }
    </style>
    <div class="footer">
        ahmadafif.com
    </div>
    """, unsafe_allow_html=True)
