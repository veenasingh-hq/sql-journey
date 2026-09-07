import sqlite3

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    balance REAL NOT NULL
)
""")

# Start clean for practice
cursor.execute("DELETE FROM accounts")

cursor.execute("""
INSERT INTO accounts (name, balance)
VALUES (?, ?)
""", ("Rahul", 5000))

cursor.execute("""
INSERT INTO accounts (name, balance)
VALUES (?, ?)
""", ("Priya", 3000))

connection.commit()


try:

    # Rahul se ₹500 minus
    cursor.execute("""
    UPDATE accounts
    SET balance = balance - 500
    WHERE name = ?
    """, ("Rahul",))

    # Priya ko ₹500 add
    cursor.execute("""
    UPDATE accounts
    SET balance = balance + 500
    WHERE name = ?
    """, ("Priya",))

    connection.commit()

    print("Transaction successful!")

except Exception as error:

    connection.rollback()

    print("Transaction failed!")
    print(error)


cursor.execute("""
SELECT * FROM accounts
""")

for row in cursor.fetchall():
    print(row)

connection.close()