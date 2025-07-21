"""Main QuickDeliver Streamlit application."""

import streamlit as st
from internal_pages.auth_pages import login_page
from internal_pages.dashboard import (
    dashboard_page, bill_tracker_page, past_orders_page, 
    subscription_page, recommendations_page
)
from internal_pages.chatbot import chatbot_page
from utils.auth import init_session_state, logout_user, is_authenticated
from config import APP_NAME, APP_ICON, PAGE_TITLE


def configure_page():
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': None
        }
    )


def load_css():
    """Load custom CSS styles."""
    try:
        with open('assets/styles.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        # Fallback CSS if file not found
        st.markdown("""
        <style>
        .main-header {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
        }
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 0.5rem;
        }
        .order-card {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)


def sidebar_navigation():
    """Handle sidebar navigation."""
    with st.sidebar:
        # Enhanced Navigation Header
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        ">
            <h2 style="margin: 0; font-size: 1.5rem;">🚚 QuickDeliver</h2>
            <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Navigate with ease</p>
        </div>
        """, unsafe_allow_html=True)

        # Create navigation buttons
        if st.button("🤖 AI Assistant", key="nav_ai", use_container_width=True):
            st.session_state.current_page = "🤖 AI Assistant"

        if st.button("📊 Dashboard", key="nav_dashboard", use_container_width=True):
            st.session_state.current_page = "📊 Dashboard"

        if st.button("🧾 Bill Tracker", key="nav_bills", use_container_width=True):
            st.session_state.current_page = "🧾 Bill Tracker"

        if st.button("📦 Past Orders", key="nav_orders", use_container_width=True):
            st.session_state.current_page = "📦 Past Orders"

        if st.button("💎 Subscription", key="nav_subscription", use_container_width=True):
            st.session_state.current_page = "💎 Subscription"

        if st.button("🎯 Recommendations", key="nav_recommendations", use_container_width=True):
            st.session_state.current_page = "🎯 Recommendations"

        # Get current page from session state
        page = st.session_state.get('current_page', '🤖 AI Assistant')

        # Enhanced divider
        st.markdown("""
        <div style="
            height: 2px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            border-radius: 1px;
            margin: 2rem 0;
            opacity: 0.6;
        "></div>
        """, unsafe_allow_html=True)

        # Enhanced User info section
        user_data = st.session_state.get('user_data', {})
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1.5rem;
            border: 1px solid #dee2e6;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        ">
            <h4 style="color: #495057; margin-bottom: 1rem; display: flex; align-items: center;">
                👤 Account Details
            </h4>
            <div style="color: #6c757d; line-height: 1.6;">
                <p style="margin: 0.5rem 0;"><strong>Name:</strong> {user_data.get('name', 'N/A')}</p>
                <p style="margin: 0.5rem 0;"><strong>Email:</strong> {user_data.get('email', 'N/A')}</p>
                <p style="margin: 0.5rem 0;"><strong>Plan:</strong> 
                    <span style="
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                        padding: 0.2rem 0.8rem;
                        border-radius: 15px;
                        font-size: 0.85rem;
                        font-weight: 500;
                    ">{user_data.get('subscription', 'N/A')}</span>
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Another enhanced divider
        st.markdown("""
        <div style="
            height: 2px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            border-radius: 1px;
            margin: 1.5rem 0;
            opacity: 0.6;
        "></div>
        """, unsafe_allow_html=True)

        # Enhanced Logout button
        if st.button("🚪 Logout", key="logout_btn", type="primary", use_container_width=True):
            logout_user()
            st.rerun()
            
        return page


def main():
    """Main application logic."""
    configure_page()
    load_css()
    init_session_state()
    
    # Initialize current page if not set
    if 'current_page' not in st.session_state:
        st.session_state.current_page = '🤖 AI Assistant'

    if not is_authenticated():
        # Hide sidebar on login page
        st.markdown("""
        <style>
        .css-1d391kg {display: none}
        section[data-testid="stSidebar"] {display: none}
        </style>
        """, unsafe_allow_html=True)
        login_page()
    else:
        # Get selected page from sidebar
        selected_page = sidebar_navigation()
        
        # Display selected page content
        user_data = st.session_state.get('user_data', {})
        
        if selected_page == "🤖 AI Assistant":
            chatbot_page()
        elif selected_page == "📊 Dashboard":
            dashboard_page()
        elif selected_page == "🧾 Bill Tracker":
            bill_tracker_page(user_data)
        elif selected_page == "📦 Past Orders":
            past_orders_page(user_data)
        elif selected_page == "💎 Subscription":
            subscription_page(user_data)
        elif selected_page == "🎯 Recommendations":
            recommendations_page(user_data)


if __name__ == "__main__":
    main()