"""Database population script to add sample users with orders and bills."""

import os
import psycopg2
from psycopg2.extras import RealDictCursor
import bcrypt
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_connection():
    """Get database connection."""
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'),
        database=os.getenv('DB_NAME', 'quickdeliver'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'Dharani@05')
    )

def hash_password(password: str) -> str:
    """Hash password using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def populate_users():
    """Populate database with sample users."""
    users_data = [
        {
            'username': 'priya_sharma',
            'email': 'priya.sharma@gmail.com',
            'name': 'Priya Sharma',
            'password': 'password123',
            'subscription': 'Premium'
        },
        {
            'username': 'rahul_kumar',
            'email': 'rahul.kumar@yahoo.com',
            'name': 'Rahul Kumar',
            'password': 'password123',
            'subscription': 'Basic'
        },
        {
            'username': 'sneha',
            'email': 'sneha@hotmail.com',
            'name': 'Sneha',
            'password': 'password123',
            'subscription': 'Standard'
        },
        {
            'username': 'amit',
            'email': 'amit.singh@gmail.com',
            'name': 'Amit Singh',
            'password': 'password123',
            'subscription': 'Premium'
        },
        {
            'username': 'dharani',
            'email': 'dharani@gmail.com',
            'name': 'Dharani',
            'password': 'password123',
            'subscription': 'Basic'
        }
    ]
    
    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        print("Adding users to database...")
        
        for user in users_data:
            # Check if user already exists
            cursor.execute("SELECT id FROM users WHERE username = %s", (user['username'],))
            if cursor.fetchone():
                print(f"⚠️  User {user['username']} already exists, skipping...")
                continue
            
            # Hash password
            password_hash = hash_password(user['password'])
            
            # Insert user
            cursor.execute("""
                INSERT INTO users (username, email, name, password_hash, subscription)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
            """, (user['username'], user['email'], user['name'], password_hash, user['subscription']))
            
            user_id = cursor.fetchone()['id']
            user['id'] = user_id
            
            print(f"✅ Added user: {user['name']} ({user['username']})")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return users_data
        
    except Exception as e:
        print(f"❌ Error adding users: {e}")
        return []

def populate_orders(users_data):
    """Populate database with sample orders for users."""
    
    # Sample order data
    restaurants = [
        "Pizza Palace", "Spice Garden", "Burger Junction", "Thai Express",
        "Chinese Dragon", "South Indian Corner", "Italian Bistro", "Mexican Fiesta",
        "BBQ Nation", "Sushi World", "Street Food Hub", "Continental Cafe",
        "Healthy Bites", "Dessert Paradise"
    ]
    
    sample_items = {
        "Pizza Palace": ["Margherita Pizza", "Pepperoni Pizza", "Garlic Bread", "Pepsi"],
        "Spice Garden": ["Butter Chicken", "Naan", "Basmati Rice", "Dal Makhani"],
        "Burger Junction": ["Classic Burger", "Cheese Burger", "Fries", "Onion Rings", "Milkshake"],
        "Thai Express": ["Pad Thai", "Spring Rolls", "Thai Tea", "Green Curry"],
        "Chinese Dragon": ["Chicken Fried Rice", "Manchurian", "Hot & Sour Soup", "Noodles"],
        "South Indian Corner": ["Masala Dosa", "Sambar", "Coconut Chutney", "Filter Coffee"],
        "Italian Bistro": ["Pasta Alfredo", "Caesar Salad", "Garlic Bread", "Tiramisu"],
        "Mexican Fiesta": ["Chicken Burrito", "Nachos", "Guacamole", "Quesadilla"]
    }
    
    statuses = ["Delivered", "Delivered", "Delivered", "In Transit", "Preparing", "Cancelled"]
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        print("Adding orders to database...")
        
        order_counter = 1
        
        for user in users_data:
            if not user.get('id'):
                continue
                
            # Generate 3-6 orders per user
            import random
            num_orders = random.randint(3, 6)
            
            for i in range(num_orders):
                # Random restaurant
                restaurant = random.choice(restaurants)
                
                # Random items from that restaurant
                available_items = sample_items.get(restaurant, ["Item 1", "Item 2"])
                num_items = random.randint(1, 3)
                items = random.sample(available_items, min(num_items, len(available_items)))
                
                # Random total (₹400 to ₹2500)
                total = random.randint(200, 999)
                
                # Random status
                status = random.choice(statuses)
                
                # Random date in last 30 days
                days_ago = random.randint(1, 30)
                order_date = datetime.now() - timedelta(days=days_ago)
                
                # Generate order number
                order_number = f"ORD-2024-{order_counter:03d}"
                order_counter += 1
                
                # Insert order
                cursor.execute("""
                    INSERT INTO orders (user_id, order_number, restaurant, items, total, status, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (user['id'], order_number, restaurant, json.dumps(items), total, status, order_date))
                
                print(f"  📦 Added order {order_number} for {user['name']}")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✅ Orders added successfully!")
        
    except Exception as e:
        print(f"❌ Error adding orders: {e}")

def populate_bills(users_data):
    """Populate database with sample bills for users."""
    
    # Subscription prices
    subscription_prices = {
        'Basic': 0,
        'Standard': 499,
        'Premium': 799
    }
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        print("Adding bills to database...")
        
        for user in users_data:
            if not user.get('id'):
                continue
                
            subscription = user.get('subscription', 'Basic')
            monthly_amount = subscription_prices.get(subscription, 0)
            
            # Generate bills for last 6 months
            for month_offset in range(6):
                bill_date = datetime.now() - timedelta(days=30 * month_offset)
                month_name = bill_date.strftime("%B %Y")
                
                # Due date is usually 25th of the month
                due_date = bill_date.replace(day=25)
                
                # Random status (mostly paid for older bills)
                if month_offset > 1:
                    status = "Paid"
                elif month_offset == 1:
                    status = "Paid" if user['username'] != 'amit_singh' else "Pending"
                else:
                    status = "Pending"
                
                # Insert bill
                cursor.execute("""
                    INSERT INTO bills (user_id, month, amount, status, due_date, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (user['id'], month_name, monthly_amount, status, due_date, bill_date))
                
                print(f"  💰 Added {month_name} bill for {user['name']} - ₹{monthly_amount} ({status})")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✅ Bills added successfully!")
        
    except Exception as e:
        print(f"❌ Error adding bills: {e}")

def main():
    """Main function to populate database."""
    print("🚀 Starting database population...")
    print("=" * 50)
    
    # Add users
    users_data = populate_users()
    
    if users_data:
        print("\n" + "=" * 50)
        # Add orders
        populate_orders(users_data)
        
        print("\n" + "=" * 50)
        # Add bills
        populate_bills(users_data)
        
        print("\n" + "=" * 50)
        print("🎉 Database population completed successfully!")
        print("\nYou can now login with any of these users:")
        print("Username: priya_sharma | Password: password123")
        print("Username: rahul_kumar | Password: password123") 
        print("Username: sneha_patel | Password: password123")
        print("Username: amit_singh | Password: password123")
        print("Username: dharani | Password: password123")
    else:
        print("❌ Failed to populate database")

if __name__ == "__main__":
    main()