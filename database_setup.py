"""Database setup script to create tables and initial data."""

import os
import psycopg2
from psycopg2.extras import RealDictCursor
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

def create_tables():
    """Create all necessary tables."""
    
    # SQL to create users table
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
        username text UNIQUE NOT NULL,
        email text UNIQUE NOT NULL,
        name text NOT NULL,
        password_hash text NOT NULL,
        subscription text DEFAULT 'Basic',
        created_at timestamptz DEFAULT now(),
        updated_at timestamptz DEFAULT now()
    );
    
    -- Create indexes for performance
    CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
    CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
    """
    
    # SQL to create orders table
    create_orders_table = """
    CREATE TABLE IF NOT EXISTS orders (
        id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
        user_id uuid NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        order_number text UNIQUE NOT NULL,
        restaurant text NOT NULL,
        items jsonb NOT NULL DEFAULT '[]',
        total decimal(10,2) NOT NULL DEFAULT 0.00,
        status text NOT NULL DEFAULT 'Pending',
        created_at timestamptz DEFAULT now(),
        updated_at timestamptz DEFAULT now()
    );
    
    -- Create indexes for performance
    CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id);
    CREATE INDEX IF NOT EXISTS idx_orders_order_number ON orders(order_number);
    CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status);
    CREATE INDEX IF NOT EXISTS idx_orders_created_at ON orders(created_at);
    """
    
    # SQL to create bills table
    create_bills_table = """
    CREATE TABLE IF NOT EXISTS bills (
        id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
        user_id uuid NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        month text NOT NULL,
        amount decimal(10,2) NOT NULL DEFAULT 0.00,
        status text NOT NULL DEFAULT 'Pending',
        due_date date NOT NULL,
        created_at timestamptz DEFAULT now(),
        updated_at timestamptz DEFAULT now()
    );
    
    -- Create indexes for performance
    CREATE INDEX IF NOT EXISTS idx_bills_user_id ON bills(user_id);
    CREATE INDEX IF NOT EXISTS idx_bills_status ON bills(status);
    CREATE INDEX IF NOT EXISTS idx_bills_due_date ON bills(due_date);
    """
    
    # Create trigger function for updated_at
    create_trigger_function = """
    CREATE OR REPLACE FUNCTION update_updated_at_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """
    
    # Create triggers
    create_triggers = """
    DROP TRIGGER IF EXISTS update_users_updated_at ON users;
    CREATE TRIGGER update_users_updated_at 
        BEFORE UPDATE ON users 
        FOR EACH ROW 
        EXECUTE FUNCTION update_updated_at_column();
        
    DROP TRIGGER IF EXISTS update_orders_updated_at ON orders;
    CREATE TRIGGER update_orders_updated_at 
        BEFORE UPDATE ON orders 
        FOR EACH ROW 
        EXECUTE FUNCTION update_updated_at_column();
        
    DROP TRIGGER IF EXISTS update_bills_updated_at ON bills;
    CREATE TRIGGER update_bills_updated_at 
        BEFORE UPDATE ON bills 
        FOR EACH ROW 
        EXECUTE FUNCTION update_updated_at_column();
    """
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        print("Creating database tables...")
        
        # Execute all table creation scripts
        cursor.execute(create_users_table)
        print("✅ Users table created")
        
        cursor.execute(create_orders_table)
        print("✅ Orders table created")
        
        cursor.execute(create_bills_table)
        print("✅ Bills table created")
        
        cursor.execute(create_trigger_function)
        print("✅ Trigger function created")
        
        cursor.execute(create_triggers)
        print("✅ Triggers created")
        
        conn.commit()
        print("🎉 Database setup completed successfully!")
        
    except psycopg2.Error as e:
        print(f"❌ Database error: {e}")
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def check_database_connection():
    """Check if database connection is working."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Database connection successful!")
        print(f"PostgreSQL version: {version[0]}")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Setting up QuickDeliver database...")
    
    # Check connection first
    if check_database_connection():
        create_tables()
    else:
        print("❌ Please check your database configuration in .env file")
        print("Make sure PostgreSQL is running and credentials are correct")