import streamlit as st

# Page setup
st.set_page_config(page_title="My App Factory", layout="wide")

# Title and welcome
st.title("🚀 My App Factory")
st.write("Welcome to your personal app portal!")

# Sidebar menu
st.sidebar.title("Navigation")
menu = ["Home", "Tools"]
choice = st.sidebar.selectbox("Select Option", menu)

if choice == "Home":
    st.subheader("Dashboard")
    st.write("Aapki factory live hai! Yahan se tum apni apps manage kar sakte ho.")

elif choice == "Tools":
    st.subheader("My Tools")
    st.write("Yahan tumhare tools list honge.")
