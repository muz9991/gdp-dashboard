import streamlit as st
import pandas as pd
import plotly.express as px
import time
import bcrypt

# Authentication
st.set_page_config(page_title="Login Page", layout="centered")

# Function to hash passwords with bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

# Pre-hashed passwords (stored securely in a real application)
USER_CREDENTIALS = {
    "user@example.com": bcrypt.hashpw("password123".encode(), bcrypt.gensalt())
}

# Session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.title("Monitoring and Anomoly detection Platform")
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email in USER_CREDENTIALS and bcrypt.checkpw(password.encode(), USER_CREDENTIALS[email]):
            st.session_state.authenticated = True
            st.session_state.email = email
            st.success("Login successful! Redirecting...")
            time.sleep(2)
            st.switch_page("pages/Dashboard.py")
        else:
            st.error("Invalid email or password. Please try again.")

login()

# Explanation of Encryption:
# - The passwords are hashed using bcrypt, which includes a salt for security.
# - When a user logs in, the entered password is encoded and checked against the stored hashed password using bcrypt.checkpw().
# - This prevents storing plain-text passwords and enhances security by making it computationally infeasible to reverse the hash.
