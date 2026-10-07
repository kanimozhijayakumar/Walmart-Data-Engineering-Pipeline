import psycopg2
import os

# Database connection string
conn_string = "dbname=walmart_db"

# CSV files mapping to tables
csv_files = {
    "customers.csv": "customers",
    "stores.csv": "stores",
    "products.csv": "products",
    "employees.csv": "employees",
    "orders.csv": "orders",
    "order_items.csv": "order_items",
}

data_dir = "data"

try:
    # Connect to the database
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    # Load each CSV file into its corresponding table
    for csv_file, table_name in csv_files.items():
        csv_path = os.path.join(data_dir, csv_file)
        
        if os.path.exists(csv_path):
            print(f"Loading {csv_file} into {table_name}...")
            
            with open(csv_path, 'r') as f:
                cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH (FORMAT CSV, HEADER TRUE)", f)
            
            conn.commit()
            print(f"✓ Successfully loaded {csv_file}")
        else:
            print(f"✗ File not found: {csv_path}")
    
    cursor.close()
    conn.close()
    print("\n✓ All data loaded successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    if conn:
        conn.rollback()
        conn.close()
