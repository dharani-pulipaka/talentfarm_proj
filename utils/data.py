"""Mock data and database functions for the delivery app."""
#data.py
# Mock user database with realistic data
MOCK_USERS = {
    "demo": {
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
        "email": "demo@quickdeliver.com",
        "name": "Demo User",
        "subscription": "Standard",
        "orders": [
            {
                "id": "ORD-2024-156",
                "date": "2024-12-28",
                "restaurant": "Pizza Palace",
                "items": ["Margherita Pizza", "Garlic Bread", "Pepsi"],
                "total": 545,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-155",
                "date": "2024-12-26",
                "restaurant": "Burger Junction",
                "items": ["Classic Burger", "French Fries", "Chocolate Milkshake"],
                "total": 425,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-154",
                "date": "2024-12-24",
                "restaurant": "Spice Garden",
                "items": ["Butter Chicken", "Garlic Naan", "Basmati Rice", "Lassi"],
                "total": 520,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-153",
                "date": "2024-12-22",
                "restaurant": "Thai Express",
                "items": ["Pad Thai", "Spring Rolls", "Thai Green Curry"],
                "total": 480,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-152",
                "date": "2024-12-20",
                "restaurant": "Chinese Dragon",
                "items": ["Chicken Fried Rice", "Veg Manchurian", "Hot & Sour Soup"],
                "total": 395,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-151",
                "date": "2024-12-18",
                "restaurant": "South Indian Corner",
                "items": ["Masala Dosa", "Sambar", "Coconut Chutney", "Filter Coffee"],
                "total": 285,
                "status": "Delivered"
            }
        ],
        "bills": [
            {"month": "December 2024", "amount": 499, "status": "Pending", "due_date": "2024-12-25"},
            {"month": "November 2024", "amount": 499, "status": "Paid", "due_date": "2024-11-25"},
            {"month": "October 2024", "amount": 499, "status": "Paid", "due_date": "2024-10-25"},
            {"month": "September 2024", "amount": 499, "status": "Paid", "due_date": "2024-09-25"}
        ]
    },
    "priya_sharma": {
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
        "email": "priya.sharma@gmail.com",
        "name": "Priya Sharma",
        "subscription": "Premium",
        "orders": [
            {
                "id": "ORD-2024-003",
                "date": "2024-01-10",
                "restaurant": "Spice Garden",
                "items": ["Butter Chicken", "Naan", "Basmati Rice"],
                "total": 622,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-004",
                "date": "2024-01-12",
                "restaurant": "Pizza Palace",
                "items": ["Pepperoni Pizza", "Garlic Bread", "Pepsi"],
                "total": 830,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-005",
                "date": "2024-01-18",
                "restaurant": "Thai Express",
                "items": ["Pad Thai", "Spring Rolls", "Thai Tea"],
                "total": 685,
                "status": "In Transit"
            },
            {
                "id": "ORD-2024-006",
                "date": "2024-01-22",
                "restaurant": "Burger Junction",
                "items": ["Cheese Burger", "Onion Rings", "Milkshake"],
                "total": 601,
                "status": "Preparing"
            }
        ],
        "bills": [
            {"month": "July 2024", "amount": 799, "status": "Paid", "due_date": "2024-07-15"},
            {"month": "June 2024", "amount": 799, "status": "Paid", "due_date": "2024-06-15"},
            {"month": "May 2024", "amount": 799, "status": "Paid", "due_date": "2024-05-15"}
        ]
    },
    "rahul_kumar": {
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
        "email": "rahul.kumar@yahoo.com",
        "name": "Rahul Kumar",
        "subscription": "Basic",
        "orders": [
            {
                "id": "ORD-2024-007",
                "date": "2024-01-08",
                "restaurant": "South Indian Corner",
                "items": ["Masala Dosa", "Sambar", "Coconut Chutney"],
                "total": 415,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-008",
                "date": "2024-01-14",
                "restaurant": "Chinese Dragon",
                "items": ["Chicken Fried Rice", "Manchurian", "Hot & Sour Soup"],
                "total": 497,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-009",
                "date": "2024-01-21",
                "restaurant": "Healthy Bites",
                "items": ["Quinoa Salad", "Green Smoothie"],
                "total": 372,
                "status": "Cancelled"
            }
        ],
        "bills": [
            {"month": "July 2024", "amount": 0, "status": "No Charge", "due_date": "2024-07-31"},
            {"month": "June 2024", "amount": 0, "status": "No Charge", "due_date": "2024-06-30"},
            {"month": "May 2024", "amount": 0, "status": "No Charge", "due_date": "2024-05-31"}
        ]
    },
    "sneha_patel": {
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
        "email": "sneha.patel@hotmail.com",
        "name": "Sneha Patel",
        "subscription": "Standard",
        "orders": [
            {
                "id": "ORD-2024-010",
                "date": "2024-01-05",
                "restaurant": "Italian Bistro",
                "items": ["Pasta Alfredo", "Caesar Salad", "Garlic Bread"],
                "total": 725,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-011",
                "date": "2024-01-11",
                "restaurant": "Mexican Fiesta",
                "items": ["Chicken Burrito", "Nachos", "Guacamole"],
                "total": 560,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-012",
                "date": "2024-01-19",
                "restaurant": "Dessert Paradise",
                "items": ["Chocolate Cake", "Ice Cream", "Coffee"],
                "total": 445,
                "status": "Delivered"
            }
        ],
        "bills": [
            {"month": "July 2024", "amount": 499, "status": "Paid", "due_date": "2024-07-20"},
            {"month": "June 2024", "amount": 499, "status": "Paid", "due_date": "2024-06-20"},
            {"month": "May 2024", "amount": 499, "status": "Paid", "due_date": "2024-05-20"}
        ]
    },
    "amit_singh": {
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
        "email": "amit.singh@gmail.com",
        "name": "Amit Singh",
        "subscription": "Premium",
        "orders": [
            {
                "id": "ORD-2024-013",
                "date": "2024-01-03",
                "restaurant": "BBQ Nation",
                "items": ["Grilled Chicken", "Tandoori Roti", "Dal Makhani"],
                "total": 945,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-014",
                "date": "2024-01-09",
                "restaurant": "Sushi World",
                "items": ["California Roll", "Miso Soup", "Green Tea"],
                "total": 999,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-015",
                "date": "2024-01-16",
                "restaurant": "Street Food Hub",
                "items": ["Pani Puri", "Bhel Puri", "Masala Chai"],
                "total": 225,
                "status": "Delivered"
            },
            {
                "id": "ORD-2024-016",
                "date": "2024-01-23",
                "restaurant": "Continental Cafe",
                "items": ["Grilled Sandwich", "French Fries", "Cold Coffee"],
                "total": 390,
                "status": "Preparing"
            }
        ],
        "bills": [
            {"month": "July 2024", "amount": 799, "status": "Pending", "due_date": "2024-07-28"},
            {"month": "June 2024", "amount": 799, "status": "Paid", "due_date": "2024-06-28"},
            {"month": "May 2024", "amount": 799, "status": "Paid", "due_date": "2024-05-28"}
        ]
    }
}

# Subscription plans
SUBSCRIPTION_PLANS = {
    "Premium": {
        "price": 799,
        "features": ["Free delivery", "Priority support", "Exclusive deals", "No surge pricing"]
    },
    "Standard": {
        "price": 499,
        "features": ["Reduced delivery fees", "Basic support", "Some deals"]
    },
    "Basic": {
        "price": 0,
        "features": ["Standard delivery fees", "Email support"]
    }
}

# Restaurant recommendations
RESTAURANT_RECOMMENDATIONS = [
    {"name": "Pizza Palace", "cuisine": "Italian", "rating": 4.5, "delivery_time": "25-35 min"},
    {"name": "Spice Garden", "cuisine": "Indian", "rating": 4.7, "delivery_time": "30-40 min"},
    {"name": "Burger Junction", "cuisine": "American", "rating": 4.2, "delivery_time": "20-30 min"},
    {"name": "Thai Express", "cuisine": "Thai", "rating": 4.6, "delivery_time": "25-35 min"},
    {"name": "Chinese Dragon", "cuisine": "Chinese", "rating": 4.4, "delivery_time": "35-45 min"},
    {"name": "South Indian Corner", "cuisine": "South Indian", "rating": 4.8, "delivery_time": "20-30 min"},
    {"name": "Italian Bistro", "cuisine": "Italian", "rating": 4.3, "delivery_time": "30-40 min"},
    {"name": "Mexican Fiesta", "cuisine": "Mexican", "rating": 4.1, "delivery_time": "25-35 min"}
]

# Special offers
SPECIAL_OFFERS = [
    {
        "title": "Free Delivery Weekend",
        "description": "Get free delivery on orders over ₹500",
        "code": "FREEDEL",
        "expires": "January 31, 2024"
    },
    {
        "title": "20% Off Pizza",
        "description": "20% off all pizza orders",
        "code": "PIZZA20",
        "expires": "February 5, 2024"
    },
    {
        "title": "New User Bonus",
        "description": "₹200 off your next order",
        "code": "WELCOME200",
        "expires": "February 15, 2024"
    }
]

# Trending items based on actual orders
TRENDING_ITEMS = [
    {"name": "Margherita Pizza", "restaurant": "Pizza Palace", "price": 539, "orders": 1250},
    {"name": "Butter Chicken", "restaurant": "Spice Garden", "price": 445, "orders": 980},
    {"name": "Pad Thai", "restaurant": "Thai Express", "price": 477, "orders": 875},
    {"name": "Classic Burger", "restaurant": "Burger Junction", "price": 310, "orders": 720},
    {"name": "Masala Dosa", "restaurant": "South Indian Corner", "price": 450, "orders": 650},
    {"name": "Chicken Fried Rice", "restaurant": "Chinese Dragon", "price": 290, "orders": 590}
]

def get_user_orders(username: str) -> list:
    """Get user's order history."""
    user_data = MOCK_USERS.get(username, {})
    return user_data.get('orders', [])

def get_user_bills(username: str) -> list:
    """Get user's billing history."""
    user_data = MOCK_USERS.get(username, {})
    return user_data.get('bills', [])

def get_user_subscription(username: str) -> str:
    """Get user's subscription plan."""
    user_data = MOCK_USERS.get(username, {})
    return user_data.get('subscription', 'Basic')

def add_order(username: str, order: dict) -> bool:
    """Add new order for user."""
    if username in MOCK_USERS:
        MOCK_USERS[username]['orders'].append(order)
        return True
    return False

def update_subscription(username: str, new_plan: str) -> bool:
    """Update user's subscription plan."""
    if username in MOCK_USERS and new_plan in SUBSCRIPTION_PLANS:
        MOCK_USERS[username]['subscription'] = new_plan
        return True
    return False

def get_all_orders() -> list:
    """Get all orders from all users for analytics."""
    all_orders = []
    for username, user_data in MOCK_USERS.items():
        for order in user_data.get('orders', []):
            order_copy = order.copy()
            order_copy['username'] = username
            order_copy['user_name'] = user_data.get('name', username)
            all_orders.append(order_copy)
    return sorted(all_orders, key=lambda x: x.get('date', ''), reverse=True)

def get_restaurant_orders(restaurant_name: str) -> list:
    """Get all orders for a specific restaurant."""
    all_orders = get_all_orders()
    return [order for order in all_orders if order.get('restaurant') == restaurant_name]