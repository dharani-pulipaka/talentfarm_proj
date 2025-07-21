"""Authentication utilities for the delivery app."""
#auth.py
import bcrypt
import streamlit as st
from typing import Dict, Optional
from utils.database import db_manager
from utils.data import MOCK_USERS  # Keep for fallback


def hash_password(password: str) -> str:
    """Hash password using bcrypt for security."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')


def verify_password(password: str, hashed: str) -> bool:
    """Verify password against hash."""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except Exception:
        # Fallback for existing SHA-256 hashes (for demo users)
        import hashlib
        return hashed == hashlib.sha256(password.encode()).hexdigest()


def authenticate_user(username: str, password: str) -> bool:
    """Authenticate user credentials against database."""
    try:
        user_data = db_manager.authenticate_user(username, password)
        return user_data is not None
    except Exception:
        # Fallback to mock data for demo users
        if username in MOCK_USERS:
            return verify_password(password, MOCK_USERS[username]["password"])
        return False


def get_user_data(username: str) -> Dict:
    """Get user data from database."""
    try:
        user_data = db_manager.get_user_by_username(username)
        if user_data:
            # Get additional data (orders, bills)
            user_id = user_data['id']
            orders = db_manager.get_user_orders(user_id)
            bills = db_manager.get_user_bills(user_id)
            
            # Format data to match existing structure
            user_data['orders'] = [
                {
                    'id': order['order_number'],
                    'date': order['created_at'].strftime('%Y-%m-%d') if order['created_at'] else '',
                    'restaurant': order['restaurant'],
                    'items': order['items'] if isinstance(order['items'], list) else [],
                    'total': float(order['total']) if order['total'] else 0,
                    'status': order['status']
                }
                for order in orders
            ]
            
            user_data['bills'] = [
                {
                    'month': bill['month'],
                    'amount': float(bill['amount']) if bill['amount'] else 0,
                    'status': bill['status'],
                    'due_date': bill['due_date'].strftime('%Y-%m-%d') if bill['due_date'] else ''
                }
                for bill in bills
            ]
            
            return user_data
    except Exception as e:
        st.error(f"Error fetching user data: {e}")
    
    # Fallback to mock data
    return MOCK_USERS.get(username, {})


def is_authenticated() -> bool:
    """Check if user is authenticated."""
    return st.session_state.get('authenticated', False)


def login_user(username: str) -> None:
    """Login user and set session state."""
    st.session_state.authenticated = True
    st.session_state.username = username
    st.session_state.user_data = get_user_data(username)


def logout_user() -> None:
    """Logout user and clear session state."""
    for key in ['authenticated', 'username', 'user_data', 'chat_history']:
        if key in st.session_state:
            del st.session_state[key]


def create_user(username: str, email: str, password: str, name: str) -> bool:
    """Create new user account in database."""
    try:
        # Check if username or email already exists
        if db_manager.check_username_exists(username):
            return False
        
        if db_manager.check_email_exists(email):
            return False
        
        # Create user in database
        return db_manager.create_user(username, email, password, name)
        
    except Exception as e:
        st.error(f"Error creating user: {e}")
        return False


def init_session_state() -> None:
    """Initialize session state variables."""
    defaults = {
        'authenticated': False,
        'username': "",
        'chat_history': [],
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value