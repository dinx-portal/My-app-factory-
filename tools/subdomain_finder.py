import streamlit as st

def run():
    st.header("🔍 Subdomain Finder")
    url = st.text_input("Enter domain (e.g., google.com)")
    if st.button("Find"):
        st.write(f"Searching subdomains for: {url}...")
        # Yahan tum apna actual script logic daloge
        st.success("Tool is working!")
