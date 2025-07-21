# QuickDeliver - AI-Powered Food Delivery Customer Service

A modern Streamlit application for food delivery customer service with AI chatbot integration using OpenRouter API and PostgreSQL database.

## 🚀 Features

- 🤖 **AI Customer Service Assistant** powered by OpenRouter
- 📊 **Dashboard** with order metrics and analytics
- 📦 **Order Tracking** and history management
- 💰 **Bill Management** and payment tracking
- 💎 **Subscription Management** with different plans
- 🎯 **Personalized Recommendations** based on order history
- 🔐 **Secure Authentication** with bcrypt password hashing
- 🗄️ **PostgreSQL Database** for persistent data storage

## 🛠️ Setup Instructions

### 1. Database Setup
First, set up PostgreSQL database:
```bash
# Install PostgreSQL (Ubuntu/Debian)
sudo apt-get install postgresql postgresql-contrib

# Or using Docker
docker run --name quickdeliver-db -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

# Create database
createdb quickdeliver
```

### 2. Environment Configuration
Copy the example environment file and configure your settings:
```bash
cp .env.example .env
```

Edit `.env` file with your database credentials:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=quickdeliver
DB_USER=postgres
DB_PASSWORD=your_password_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
The application will automatically create the necessary tables when you first run it. The migration files are located in `supabase/migrations/`.

### 5. Configure OpenRouter API
1. Get your API key from [OpenRouter](https://openrouter.ai/)
2. Add your API key to the `.env` file:
   ```env
   OPENROUTER_API_KEY=sk-or-v1-your-actual-api-key-here
   ```

### 6. Available Models
You can change the AI model in `config.py`. Popular options include:
- `anthropic/claude-3.5-sonnet` (Default - Great for conversations)
- `openai/gpt-4o` (OpenAI's latest model)
- `google/gemini-pro-1.5` (Google's Gemini)
- `meta-llama/llama-3.1-8b-instruct` (Open source option)
- `mistralai/mixtral-8x7b-instruct` (Fast and efficient)

### 7. Run the Application
```bash
streamlit run app.py
```

## 🔑 Demo Credentials

- **Username:** `demo` (uses mock data)
- **Password:** `password`

Or create a new account using the signup form - all new accounts will be stored in the PostgreSQL database.

## 📁 Project Structure

```
├── app.py                    # Main application entry point
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── .env.example            # Environment variables template
├── assets/
│   └── styles.css          # Custom CSS styles
├── supabase/
│   └── migrations/         # Database migration files
├── pages/
│   ├── auth_pages.py       # Login/signup functionality
│   ├── chatbot.py          # AI assistant page
│   └── dashboard.py        # Dashboard and other pages
└── utils/
    ├── auth.py             # Authentication utilities
    ├── data.py             # Mock data and database functions
    ├── database.py         # PostgreSQL database manager
    └── openrouter_client.py # OpenRouter API client
```

## 🎯 Usage

1. **Setup Database** following the instructions above
2. **Login** with demo credentials or create a new account
3. **Navigate** through different sections using the sidebar
4. **Chat** with the AI assistant for customer service help
5. **Track orders**, manage bills, and explore recommendations
6. **Manage subscription** and account settings

## 🗄️ Database Features

- **User Management**: Secure user registration and authentication
- **Order Tracking**: Complete order history with status updates
- **Billing System**: Monthly billing and payment tracking
- **Data Persistence**: All user data stored securely in PostgreSQL
- **Migration System**: Easy database schema updates

## 🔧 Customization

### Database Configuration
Modify database settings in `.env`:
```env
DB_HOST=your_host
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
```

### Changing AI Models
Edit `OPENROUTER_MODEL` in `config.py`:
```python
OPENROUTER_MODEL = "anthropic/claude-3.5-sonnet"  # Change to your preferred model
```

### Adding New Features
- Add new pages in the `pages/` directory
- Extend the database schema with new migration files
- Modify the UI styling in `assets/styles.css`
- Add new database operations in `utils/database.py`

## 🌟 OpenRouter Benefits

- **Multiple AI Models**: Access to 100+ AI models from different providers
- **Cost Effective**: Pay only for what you use
- **High Availability**: Reliable API with fallback options
- **Easy Integration**: OpenAI-compatible API format

## 🔒 Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **SQL Injection Protection**: Parameterized queries
- **Row Level Security**: Database-level access control
- **Environment Variables**: Secure configuration management

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.