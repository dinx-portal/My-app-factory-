import streamlit as st

st.set_page_config(page_title="My App Factory", layout="wide")

st.title("🚀 My App Factory")
st.write("Welcome to your personal App Portal! Yahan se tum apni apps manage karoge.")

# Menu
menu = ["Home", "My Security Tools", "AI Lab"]
choice = st.sidebar.selectbox("Select a Tool", menu)

if choice == "Home":
    st.subheader("Dashboard")
    st.write("Abhi tumhara factory portal live ho chuka hai!")
    
elif choice == "My Security Tools":
    st.subheader("Security Suite")
    st.write("Yahan tum apne hacking/security tools manage karoge.")
    
elif choice == "AI Lab":
    st.subheader("AI Lab")
    st.write("Yahan tum AI agents aur generators run karoge.")
