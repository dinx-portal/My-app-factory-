import streamlit as st
# Yahan apne tools import karo
from tools import subdomain_finder 

st.set_page_config(page_title="My AI Factory", layout="wide")

st.title("🚀 My AI Super-App")
st.sidebar.title("🛠️ Tools Factory")

# Sidebar mein tools ka menu
tool = st.sidebar.selectbox("Choose a Tool", ["Dashboard", "Subdomain Finder"])

if tool == "Dashboard":
    st.subheader("Welcome to your Factory!")
    st.write("Yahan se tum duniya ke har AI tool ko access kar sakte ho.")

elif tool == "Subdomain Finder":
    # Humne subdomain_finder.py ke andar 'run()' function banaya tha
    subdomain_finder.run()
