import random
import string
import streamlit as st

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for i in range(length):
        random_character = random.choice(characters)
        password += random_character

    return password

#print(generate_random_password())#

st.title("Random Password Generator")

length = st.slider("select password length", min_value=5, max_value=128, value= 12)

if st.button("Generate Password"):
    password = generate_random_password(length)
    st.write("generated password:", password)