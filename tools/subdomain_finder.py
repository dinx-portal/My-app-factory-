import streamlit as st

def run():
    st.header("🔍 Subdomain Finder Tool")
    domain = st.text_input("Enter domain:")
    if st.button("Find Subdomains"):
        # Yahan apna logic dalna
        st.info(f"Scanning {domain}... (Logic yahan aayega)")
        st.success("Result mil gaya!")
