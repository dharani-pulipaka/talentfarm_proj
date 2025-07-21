"""Configuration settings for the delivery app."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App Configuration
APP_NAME = "QuickDeliver"
APP_ICON = "🚚"
PAGE_TITLE = "QuickDeliver - Customer Service"

# Database Configuration
DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "quickdeliver"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "Dharani@05")
}

# OpenRouter API Configuration
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = "anthropic/claude-3.5-sonnet"  # You can change this to your preferred model
OPENROUTER_SITE_URL = "https://quickdeliver.app"  # Optional: Your site URL
OPENROUTER_APP_NAME = "QuickDeliver"  # Optional: Your app name

# Add your OpenRouter API key here - REPLACE WITH YOUR ACTUAL KEY
OPENROUTER_API_KEY = "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"  # Replace with your actual API key

# UI Configuration
THEME = {
    "primary_color": "#667eea",
    "secondary_color": "#764ba2",
    "background_color": "#f8f9fa",
    "text_color": "#333333"
}

# Session Configuration
SESSION_TIMEOUT = 3600  # 1 hour in seconds

# Mock Data Configuration
DEMO_USERNAME = "demo"
DEMO_PASSWORD = "password"