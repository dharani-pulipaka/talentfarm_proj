/*
  # Create bills table for QuickDeliver app

  1. New Tables
    - `bills`
      - `id` (uuid, primary key)
      - `user_id` (uuid, foreign key to users)
      - `month` (text)
      - `amount` (decimal)
      - `status` (text)
      - `due_date` (date)
      - `created_at` (timestamp)
      - `updated_at` (timestamp)

  2. Security
    - Enable RLS on `bills` table
    - Add policy for users to read their own bills
    - Add policy for users to update their own bills

  3. Indexes
    - Index on user_id for fast user bill lookups
    - Index on status for filtering
    - Index on due_date for sorting
*/

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

-- Enable Row Level Security
ALTER TABLE bills ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY "Users can read own bills"
  ON bills
  FOR SELECT
  TO authenticated
  USING (user_id = auth.uid());

CREATE POLICY "Users can update own bills"
  ON bills
  FOR UPDATE
  TO authenticated
  USING (user_id = auth.uid());

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_bills_user_id ON bills(user_id);
CREATE INDEX IF NOT EXISTS idx_bills_status ON bills(status);
CREATE INDEX IF NOT EXISTS idx_bills_due_date ON bills(due_date);

-- Create trigger to update updated_at timestamp
CREATE TRIGGER update_bills_updated_at 
    BEFORE UPDATE ON bills 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();