"""Dashboard and related pages for the delivery app."""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
from utils.data import (
    SUBSCRIPTION_PLANS, RESTAURANT_RECOMMENDATIONS, 
    SPECIAL_OFFERS, TRENDING_ITEMS, get_all_orders
)


def dashboard_page():
    """Main dashboard page with metrics and charts."""
    st.markdown("""
    <div class="main-header">
        <h1>📊 Dashboard Overview</h1>
        <p>Welcome back! Here's your delivery service summary</p>
    </div>
    """, unsafe_allow_html=True)

    # Get user data
    user_data = st.session_state.get('user_data', {})
    orders = user_data.get('orders', [])
    
    # Calculate metrics
    total_orders = len(orders)
    total_spent = sum(order.get('total', 0) for order in orders)
    avg_order_value = total_spent / total_orders if total_orders > 0 else 0
    
    # Recent orders (last 7 days)
    recent_orders = [order for order in orders if order.get('status') in ['Delivered', 'In Transit', 'Preparing']]
    recent_count = len(recent_orders[:5])  # Last 5 orders

    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Orders</h3>
            <h2>{total_orders}</h2>
            <p>All time orders</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Spent</h3>
            <h2>₹{total_spent:,.0f}</h2>
            <p>Lifetime spending</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Average Order</h3>
            <h2>₹{avg_order_value:.0f}</h2>
            <p>Per order value</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Recent Activity</h3>
            <h2>{recent_count}</h2>
            <p>Recent orders</p>
        </div>
        """, unsafe_allow_html=True)

    # Charts section
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Recent Activity")
        
        # Recent Orders
        st.write("**Recent Orders**")
        if orders:
            for order in orders[:3]:  # Show last 3 orders
                status_color = {
                    'Delivered': '#28a745',
                    'In Transit': '#ffc107', 
                    'Preparing': '#17a2b8',
                    'Cancelled': '#dc3545'
                }.get(order.get('status', 'Pending'), '#6c757d')
                
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, {status_color}20 0%, {status_color}10 100%);
                    border-left: 4px solid {status_color};
                    padding: 1rem;
                    margin: 0.5rem 0;
                    border-radius: 8px;
                ">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong>{order.get('restaurant', 'Unknown')}</strong><br>
                            <small>{order.get('date', 'Unknown date')}</small>
                        </div>
                        <div style="text-align: right;">
                            <strong>₹{order.get('total', 0)}</strong><br>
                            <span style="color: {status_color}; font-weight: 500;">{order.get('status', 'Pending')}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No recent orders found")
    
    # with col2:
    #     st.subheader("💰 Billing Summary")
        
    #     # Billing information
    #     bills = user_data.get('bills', [])
    #     subscription = user_data.get('subscription', 'Basic')
        
    #     if bills:
    #         # Sort bills by due date (most recent first) and show last 3
    #         sorted_bills = sorted(bills, key=lambda x: x.get('due_date', ''), reverse=True)
    #         recent_bills = sorted_bills[:3]
            
    #         for bill in recent_bills:
    #             status_color = '#28a745' if bill.get('status') == 'Paid' else '#ffc107'
    #             amount = bill.get('amount', 0)
                
    #             # For Basic plan users, show a different message
    #             if subscription == 'Basic':
    #                 st.markdown("""
    #                 <div style="
    #                     background: linear-gradient(135deg, #e8f5e8 0%, #d4edda 100%);
    #                     border: 1px solid #28a745;
    #                     border-radius: 10px;
    #                     padding: 1.5rem;
    #                     text-align: center;
    #                     color: #155724;
    #                     margin: 1rem 0;
    #                 ">
    #                     <h4 style="margin: 0 0 0.5rem 0;">🎉 You're on the Basic Plan!</h4>
    #                     <p style="margin: 0;">No monthly subscription fees - you only pay delivery charges per order.</p>
    #                 </div>
    #                 """, unsafe_allow_html=True)
    #                 break
                
    #             # Skip bills with 0 amount
    #             if amount <= 0:
    #                 continue
                
    #             st.markdown(f"""
    #             <div style="
    #                 background: {'#f8f9fa' if bill.get('status') == 'Paid' else '#fff3cd'};
    #                 border-left: 4px solid {status_color};
    #                 padding: 1rem;
    #                 margin: 0.5rem 0;
    #                 border-radius: 8px;
    #                 box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    #             ">
    #                 <div style="display: flex; justify-content: space-between; align-items: center;">
    #                     <div>
    #                         <strong>{bill.get('month', 'Unknown')}</strong><br>
    #                         <small style="color: #666;">Due: {bill.get('due_date', 'Unknown')}</small>
    #                     </div>
    #                     <div style="text-align: right;">
    #                         <strong style="color: #333;">₹{amount}</strong><br>
    #                         <span style="color: {status_color}; font-weight: 500;">{bill.get('status', 'Pending')}</span>
    #                     </div>
    #                 </div>
    #             </div>
    #             """, unsafe_allow_html=True)
    #     else:
    #         if subscription == 'Basic':
    #             st.markdown("""
    #             <div style="
    #                 background: linear-gradient(135deg, #e8f5e8 0%, #d4edda 100%);
    #                 border: 1px solid #28a745;
    #                 border-radius: 10px;
    #                 padding: 1.5rem;
    #                 text-align: center;
    #                 color: #155724;
    #             ">
    #                 <h4 style="margin: 0 0 0.5rem 0;">🎉 You're on the Basic Plan!</h4>
    #                 <p style="margin: 0;">No monthly subscription fees - you only pay delivery charges per order.</p>
    #             </div>
    #             """, unsafe_allow_html=True)
    #         else:
    #             st.info("No billing information found")

    # Order trends chart
    if orders:
        st.subheader("📊 Order Trends")
        
        # Create a simple chart showing orders by restaurant
        restaurant_counts = {}
        restaurant_totals = {}
        
        for order in orders:
            restaurant = order.get('restaurant', 'Unknown')
            restaurant_counts[restaurant] = restaurant_counts.get(restaurant, 0) + 1
            restaurant_totals[restaurant] = restaurant_totals.get(restaurant, 0) + order.get('total', 0)
        
        if restaurant_counts:
            # Create DataFrame for plotting
            chart_data = pd.DataFrame({
                'Restaurant': list(restaurant_counts.keys()),
                'Orders': list(restaurant_counts.values()),
                'Total Spent (₹)': list(restaurant_totals.values())
            })
            
            # Create bar chart
            fig = px.bar(
                chart_data, 
                x='Restaurant', 
                y='Orders',
                title='Orders by Restaurant',
                color='Total Spent (₹)',
                color_continuous_scale='viridis'
            )
            fig.update_layout(
                xaxis_tickangle=-45,
                height=400,
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)

    # Quick actions
    # st.subheader("⚡ Quick Actions")
    # col1, col2, col3, col4 = st.columns(4)
    
    # with col1:
    #     if st.button("🛒 New Order", use_container_width=True):
    #         st.info("Redirecting to order placement...")
    
    # with col2:
    #     if st.button("📦 Track Order", use_container_width=True):
    #         st.session_state.current_page = "📦 Past Orders"
    #         st.rerun()
    
    # with col3:
    #     if st.button("💰 View Bills", use_container_width=True):
    #         st.session_state.current_page = "🧾 Bill Tracker"
    #         st.rerun()
    
    # with col4:
    #     if st.button("🎯 Get Recommendations", use_container_width=True):
    #         st.session_state.current_page = "🎯 Recommendations"
    #         st.rerun()


def bill_tracker_page(user_data):
    """Bill tracking and payment management page."""
    st.markdown("""
    <div class="main-header">
        <h1>🧾 Bill Tracker</h1>
        <p>Manage your subscription and payment history</p>
    </div>
    """, unsafe_allow_html=True)

    # Current subscription info
    subscription = user_data.get('subscription', 'Basic')
    plan_info = SUBSCRIPTION_PLANS.get(subscription, SUBSCRIPTION_PLANS['Basic'])
    
    st.subheader("📋 Current Subscription")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1rem;
        ">
            <h3 style="margin: 0 0 0.5rem 0;">{subscription} Plan</h3>
            <h2 style="margin: 0 0 1rem 0;">₹{plan_info['price']}/month</h2>
            <ul style="margin: 0; padding-left: 1.5rem;">
                {''.join([f'<li>{feature}</li>' for feature in plan_info['features']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("💎 Upgrade Plan", use_container_width=True):
            st.session_state.current_page = "💎 Subscription"
            st.rerun()

    # Bills history
    st.subheader("📊 Billing History")
    bills = user_data.get('bills', [])
    
    if bills:
        for bill in bills:
            status_color = '#28a745' if bill['status'] == 'Paid' else '#ffc107'
            status_bg = '#d4edda' if bill['status'] == 'Paid' else '#fff3cd'
            
            st.markdown(f"""
            <div style="
                background: {status_bg};
                border: 1px solid {status_color};
                border-radius: 10px;
                padding: 1rem;
                margin: 1rem 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <div>
                    <h4 style="margin: 0; color: #333;">{bill['month']}</h4>
                    <p style="margin: 0.5rem 0 0 0; color: #666;">Due: {bill['due_date']}</p>
                </div>
                <div style="text-align: right;">
                    <h3 style="margin: 0; color: #333;">₹{bill['amount']}</h3>
                    <span style="
                        background: {status_color};
                        color: white;
                        padding: 0.3rem 0.8rem;
                        border-radius: 15px;
                        font-size: 0.85rem;
                        font-weight: 500;
                    ">{bill['status']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No billing history available")

    # Payment methods
    st.subheader("💳 Payment Methods")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            border: 2px dashed #667eea;
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            color: #667eea;
        ">
            <h4>💳 Add Payment Method</h4>
            <p>Add a credit/debit card or UPI</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 10px;
            padding: 1.5rem;
        ">
            <h4>🏦 Current Method</h4>
            <p><strong>UPI:</strong> user@paytm</p>
            <p><strong>Card:</strong> **** **** **** 1234</p>
        </div>
        """, unsafe_allow_html=True)


def past_orders_page(user_data):
    """Past orders tracking page."""
    st.markdown("""
    <div class="main-header">
        <h1>📦 Past Orders</h1>
        <p>Track your order history and status</p>
    </div>
    """, unsafe_allow_html=True)

    orders = user_data.get('orders', [])
    
    if not orders:
        st.info("No orders found. Place your first order to see it here!")
        return

    # Filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        status_filter = st.selectbox(
            "Filter by Status",
            ["All", "Delivered", "In Transit", "Preparing", "Cancelled"]
        )
    
    with col2:
        # Get unique restaurants
        restaurants = list(set(order.get('restaurant', 'Unknown') for order in orders))
        restaurant_filter = st.selectbox(
            "Filter by Restaurant", 
            ["All"] + restaurants
        )
    
    with col3:
        sort_order = st.selectbox(
            "Sort by",
            ["Newest First", "Oldest First", "Amount High to Low", "Amount Low to High"]
        )

    # Apply filters
    filtered_orders = orders.copy()
    
    if status_filter != "All":
        filtered_orders = [order for order in filtered_orders if order.get('status') == status_filter]
    
    if restaurant_filter != "All":
        filtered_orders = [order for order in filtered_orders if order.get('restaurant') == restaurant_filter]
    
    # Apply sorting
    if sort_order == "Newest First":
        filtered_orders.sort(key=lambda x: x.get('date', ''), reverse=True)
    elif sort_order == "Oldest First":
        filtered_orders.sort(key=lambda x: x.get('date', ''))
    elif sort_order == "Amount High to Low":
        filtered_orders.sort(key=lambda x: x.get('total', 0), reverse=True)
    elif sort_order == "Amount Low to High":
        filtered_orders.sort(key=lambda x: x.get('total', 0))

    # Display orders
    st.subheader(f"📋 Orders ({len(filtered_orders)} found)")
    
    for order in filtered_orders:
        status_colors = {
            'Delivered': '#28a745',
            'In Transit': '#ffc107',
            'Preparing': '#17a2b8',
            'Cancelled': '#dc3545'
        }
        
        status_color = status_colors.get(order.get('status', 'Pending'), '#6c757d')
        
        with st.container():
            st.markdown(f"""
            <div class="order-card" style="
                border-left: 5px solid {status_color};
                background: white;
                margin: 1rem 0;
                padding: 1.5rem;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            ">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <div>
                        <h3 style="margin: 0; color: #333;">{order.get('restaurant', 'Unknown Restaurant')}</h3>
                        <p style="margin: 0.5rem 0; color: #666;">Order #{order.get('id', 'Unknown')} • {order.get('date', 'Unknown date')}</p>
                    </div>
                    <div style="text-align: right;">
                        <h3 style="margin: 0; color: #333;">₹{order.get('total', 0)}</h3>
                        <span style="
                            background: {status_color};
                            color: white;
                            padding: 0.3rem 0.8rem;
                            border-radius: 15px;
                            font-size: 0.85rem;
                            font-weight: 500;
                        ">{order.get('status', 'Pending')}</span>
                    </div>
                </div>
                
                <div style="margin-top: 1rem;">
                    <strong style="color: #333;">Items:</strong>
                    <div style="margin: 0.5rem 0; color: #666;">
                        {', '.join(order.get('items', []))}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Action buttons
            col1, col2, col3 = st.columns([1, 1, 2])
            
            with col1:
                if st.button(f"🔄 Reorder", key=f"reorder_{order.get('id')}"):
                    st.success(f"Added {order.get('restaurant')} items to cart!")
            
            with col2:
                if st.button(f"⭐ Rate", key=f"rate_{order.get('id')}"):
                    st.info("Rating feature coming soon!")


def subscription_page(user_data):
    """Subscription management page."""
    st.markdown("""
    <div class="main-header">
        <h1>💎 Subscription Plans</h1>
        <p>Choose the perfect plan for your food delivery needs</p>
    </div>
    """, unsafe_allow_html=True)

    current_plan = user_data.get('subscription', 'Basic')
    
    # Display current plan
    st.subheader("📋 Current Plan")
    current_plan_info = SUBSCRIPTION_PLANS.get(current_plan, SUBSCRIPTION_PLANS['Basic'])
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
    ">
        <h2 style="margin: 0 0 0.5rem 0;">You're on {current_plan} Plan</h2>
        <h3 style="margin: 0 0 1rem 0;">₹{current_plan_info['price']}/month</h3>
        <p style="margin: 0; opacity: 0.9;">
            {'Free plan with basic features' if current_plan == 'Basic' else 'Thank you for being a valued subscriber!'}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Available plans
    st.subheader("🎯 Available Plans")
    
    cols = st.columns(3)
    
    for i, (plan_name, plan_info) in enumerate(SUBSCRIPTION_PLANS.items()):
        with cols[i]:
            is_current = plan_name == current_plan
            border_color = "#28a745" if is_current else "#667eea"
            
            st.markdown(f"""
            <div style="
                border: 2px solid {border_color};
                border-radius: 15px;
                padding: 1.5rem;
                text-align: center;
                background: {'#f8fff8' if is_current else 'white'};
                height: 350px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            ">
                <div>
                    <h3 style="margin: 0 0 1rem 0; color: #333;">{plan_name}</h3>
                    <h2 style="margin: 0 0 1rem 0; color: {border_color};">₹{plan_info['price']}/month</h2>
                    <ul style="text-align: left; padding-left: 1rem; color: #666;">
                        {''.join([f'<li style="margin: 0.5rem 0;">{feature}</li>' for feature in plan_info['features']])}
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if is_current:
                st.success("✅ Current Plan")
            # else:
            #     if st.button(f"Choose {plan_name}", key=f"select_{plan_name}", use_container_width=True):
            #         st.success(f"Plan changed to {plan_name}!")
            #         # Here you would typically update the database
            #         st.info("Plan change will be effective from next billing cycle.")

    # Billing information
    st.subheader("💳 Billing Information")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            border: 1px solid #dee2e6;
        ">
            <h4 style="margin: 0 0 1rem 0; color: #333;">Next Billing Date</h4>
            <p style="margin: 0; color: #666; font-size: 1.1rem;">January 25, 2026</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            border: 1px solid #dee2e6;
        ">
            <h4 style="margin: 0 0 1rem 0; color: #333;">Next Charge</h4>
            <p style="margin: 0; color: #666; font-size: 1.1rem;">₹{current_plan_info['price']}</p>
        </div>
        """, unsafe_allow_html=True)


def recommendations_page(user_data):
    """Personalized recommendations page."""
    st.markdown("""
    <div class="main-header">
        <h1>🎯 Personalized Recommendations</h1>
        <p>Discover new restaurants and dishes based on your preferences</p>
    </div>
    """, unsafe_allow_html=True)

    # User's order history for personalization
    orders = user_data.get('orders', [])
    
    # Analyze user preferences
    if orders:
        # Get favorite restaurants
        restaurant_counts = {}
        for order in orders:
            restaurant = order.get('restaurant', 'Unknown')
            restaurant_counts[restaurant] = restaurant_counts.get(restaurant, 0) + 1
        
        favorite_restaurants = sorted(restaurant_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        
        st.subheader("⭐ Based on Your Order History")
        
        if favorite_restaurants:
            st.write("**Your Favorite Restaurants:**")
            for restaurant, count in favorite_restaurants:
                st.markdown(f"• **{restaurant}** - {count} orders")

    # Restaurant recommendations
    st.subheader("🍽️ Recommended Restaurants")
    
    cols = st.columns(2)
    
    for i, restaurant in enumerate(RESTAURANT_RECOMMENDATIONS[:6]):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="
                background: white;
                border: 1px solid #e0e0e0;
                border-radius: 10px;
                padding: 1rem;
                margin: 0.5rem 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <h4 style="margin: 0 0 0.5rem 0; color: #333;">{restaurant['name']}</h4>
                <p style="margin: 0 0 0.5rem 0; color: #666;">{restaurant['cuisine']} Cuisine</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #ffc107;">⭐ {restaurant['rating']}</span>
                    <span style="color: #28a745;">🕒 {restaurant['delivery_time']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Trending items
    st.subheader("🔥 Trending Items")
    
    cols = st.columns(3)
    
    for i, item in enumerate(TRENDING_ITEMS[:6]):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #fff5f5 0%, #fed7d7 100%);
                border-radius: 10px;
                padding: 1rem;
                margin: 0.5rem 0;
                text-align: center;
            ">
                <h4 style="margin: 0 0 0.5rem 0; color: #333;">{item['name']}</h4>
                <p style="margin: 0 0 0.5rem 0; color: #666; font-size: 0.9rem;">{item['restaurant']}</p>
                <p style="margin: 0 0 0.5rem 0; color: #e53e3e; font-weight: bold;">₹{item['price']}</p>
                <p style="margin: 0; color: #666; font-size: 0.8rem;">{item['orders']} orders</p>
            </div>
            """, unsafe_allow_html=True)

    # Special offers
    st.subheader("🎁 Special Offers")
    
    for offer in SPECIAL_OFFERS:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #e6fffa 0%, #b2f5ea 100%);
            border-left: 4px solid #38b2ac;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
        ">
            <h4 style="margin: 0 0 0.5rem 0; color: #234e52;">{offer['title']}</h4>
            <p style="margin: 0 0 0.5rem 0; color: #2d3748;">{offer['description']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <code style="background: #38b2ac; color: white; padding: 0.3rem 0.6rem; border-radius: 5px;">{offer['code']}</code>
                <small style="color: #4a5568;">Expires: {offer['expires']}</small>
            </div>
        </div>
        """, unsafe_allow_html=True)