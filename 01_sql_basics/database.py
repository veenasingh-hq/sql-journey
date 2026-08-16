import sqlite3


# Connect to database
connection = sqlite3.connect("patients.db")

# Create cursor
cursor = connection.cursor()


# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT NOT NULL
)
""")


# Save changes
connection.commit()

# Close connection
connection.close()


print("Database and table created successfully!")