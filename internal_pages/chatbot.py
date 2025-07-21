"""AI Chatbot page for customer service."""
#chatbot.py
import streamlit as st
from utils.openrouter_client import call_openrouter_api, add_to_chat_history, clear_chat_history
from utils.auth import get_user_data


def chatbot_page():
    """AI Assistant chatbot page."""
    st.header("🤖 AI Customer Service Assistant")
    
    user_data = st.session_state.get('user_data', {})

    # Main layout with chat on left and actions on right
    col_chat, col_actions = st.columns([3, 1])

    with col_chat:
        # Chat container with better styling
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 15px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border: 1px solid #dee2e6;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            max-height: 500px;
            overflow-y: auto;
        ">
        """, unsafe_allow_html=True)

        # Display chat history
        chat_history = st.session_state.get('chat_history', [])
        
        if not chat_history:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
                padding: 1rem;
                border-radius: 10px;
                margin: 0.5rem 0;
                border-left: 4px solid #4caf50;
                color: #2e7d32;
            ">
                🤖 <strong>Assistant:</strong> Hello {user_data.get('name', 'there')}! I'm your QuickDeliver assistant. 
                How can I help you today? I can assist with orders, billing, recommendations, and more!
            </div>
            """, unsafe_allow_html=True)

        for message in chat_history:
            if message["role"] == "user":
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
                    padding: 1rem;
                    border-radius: 10px;
                    margin: 0.5rem 0;
                    border-left: 4px solid #2196f3;
                    color: #1565c0;
                    margin-left: 2rem;
                ">
                    👤 <strong>You:</strong> {message["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
                    padding: 1rem;
                    border-radius: 10px;
                    margin: 0.5rem 0;
                    border-left: 4px solid #9c27b0;
                    color: #6a1b9a;
                    margin-right: 2rem;
                ">
                    🤖 <strong>Assistant:</strong> {message["content"]}
                </div>
                """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Chat input at bottom
        st.markdown("### 💬 Type your message:")
        
        # Use form to handle input and clear after submission
        with st.form(key="chat_form", clear_on_submit=True):
            col_input, col_send = st.columns([4, 1])
            with col_input:
                user_input = st.text_input(
                    "", 
                    key="chat_input_form",
                    placeholder="Ask me anything about your orders, billing, or account...",
                    label_visibility="collapsed"
                )
            with col_send:
                send_button = st.form_submit_button("📤 Send", type="primary", use_container_width=True)

            # Handle form submission
            if send_button and user_input.strip():
                # Add user message to history
                add_to_chat_history("user", user_input)

                # Get AI response
                with st.spinner("🤖 Thinking..."):
                    response = call_openrouter_api(user_input)

                # Add AI response to history
                add_to_chat_history("assistant", response)

                # Rerun to show new messages and clear form
                st.rerun()

    with col_actions:
        # Quick Actions Section
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #fff3e0 0%, #ffcc02 100%);
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        ">
            <h4 style="color: #e65100; margin-bottom: 1rem;">⚡ Quick Actions</h4>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📦 Track Order", key="track_order_btn", use_container_width=True):
            add_to_chat_history("user", "I want to track my recent order")
            response = call_openrouter_api("I want to track my recent order status")
            add_to_chat_history("assistant", response)
            st.rerun()

        if st.button("💰 Billing Help", key="billing_help_btn", use_container_width=True):
            add_to_chat_history("user", "I have a question about my bill")
            response = call_openrouter_api("I have a question about my monthly bill")
            add_to_chat_history("assistant", response)
            st.rerun()

        if st.button("🍕 Restaurant Recs", key="restaurant_recs_btn", use_container_width=True):
            add_to_chat_history("user", "Can you recommend some restaurants?")
            response = call_openrouter_api("Can you recommend some restaurants based on my order history?")
            add_to_chat_history("assistant", response)
            st.rerun()

        if st.button("⚙️ Account Settings", key="account_settings_btn", use_container_width=True):
            add_to_chat_history("user", "Help me with my account settings")
            response = call_openrouter_api("Help me with my account settings and preferences")
            add_to_chat_history("assistant", response)
            st.rerun()

        # Clear chat button
        st.markdown("---")
        if st.button("🗑️ Clear Chat", key="clear_chat_btn", use_container_width=True):
            clear_chat_history()
            st.rerun()

        # Chat Tips in expandable section
        with st.expander("💡 Chat Tips"):
            st.markdown("""
            **What I can help you with:**
            - 📦 Track your orders and delivery status
            - 💰 Answer billing and payment questions
            - 🍕 Recommend restaurants based on your preferences
            - ⚙️ Help with account settings and subscription
            - 🎯 Find deals and special offers
            - 📞 General customer support
            
            **Tips for better responses:**
            - Be specific about your issue
            - Mention order IDs if you have them
            - Ask one question at a time for clarity
            
            **Powered by OpenRouter AI**
            - Using Claude 3.5 Sonnet for intelligent responses
            - Multiple model options available for different needs
            """)