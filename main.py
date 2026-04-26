import streamlit as st
from tools import pass_gen  # Naya tool import kiya

st.sidebar.title("Navigation")
menu = ["Home", "Password Generator"]
choice = st.sidebar.selectbox("Select Option", menu)

if choice == "Home":
    st.write("Welcome to your Factory!")
elif choice == "Password Generator":
    pass_gen.run() # Tool chala diya
