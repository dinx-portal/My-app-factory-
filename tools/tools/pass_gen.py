import streamlit as st
import random
import string

def run():
    st.header("🔑 Password Generator")
    length = st.slider("Password Length", 8, 32, 12)
    if st.button("Generate Password"):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(length))
        st.success(f"Tera Password: `{password}`")
