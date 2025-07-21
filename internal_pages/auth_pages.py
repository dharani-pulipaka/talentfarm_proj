"""Authentication pages for login and signup."""
#auth_pages.py
import streamlit as st
from utils.auth import authenticate_user, create_user, login_user
from config import APP_NAME


def load_css():
    """Load custom CSS styles."""
    try:
        with open('assets/styles.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("CSS file not found. Using default styling.")


def login_page():
    """Display login/signup page."""
    load_css()

    st.markdown(f"""
    <div class="main-header">
        <h1>🚚 {APP_NAME}</h1>
        <p>Your favorite food, delivered fast</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["Sign In", "Sign Up"])

        with tab1:
            signin_form()

        with tab2:
            signup_form()

        st.markdown('</div>', unsafe_allow_html=True)


def signin_form():
    """Display sign in form."""
    st.subheader("Welcome Back!")

    with st.form("signin_form"):
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        submit_button = st.form_submit_button("Sign In")

        if submit_button:
            if not username or not password:
                st.error("❌ Please fill in all fields")
            elif authenticate_user(username, password):
                login_user(username)
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")

    st.info("💡 Demo credentials: Username: `demo`, Password: `password`")


def signup_form():
    """Display sign up form."""
    st.subheader("Join QuickDeliver")

    with st.form("signup_form"):
        new_username = st.text_input("Choose Username", key="signup_username")
        new_name = st.text_input("Full Name", key="signup_name")
        new_email = st.text_input("Email Address", key="signup_email")
        new_password = st.text_input("Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

        submit_button = st.form_submit_button("Sign Up")

        if submit_button:
            if not all([new_username, new_name, new_email, new_password, confirm_password]):
                st.error("❌ Please fill in all fields")
            elif new_password != confirm_password:
                st.error("❌ Passwords don't match")
            elif len(new_password) < 6:
                st.error("❌ Password must be at least 6 characters")
            elif "@" not in new_email or "." not in new_email:
                st.error("❌ Please enter a valid email address")
            elif len(new_username) < 3:
                st.error("❌ Username must be at least 3 characters")
            elif len(new_name.strip()) < 2:
                st.error("❌ Please enter your full name")
            elif create_user(new_username, new_email, new_password, new_name):
                st.success("✅ Account created successfully! Please sign in with your new credentials.")
                st.balloons()
            else:
                st.error("❌ Username or email already exists. Please try different credentials.")