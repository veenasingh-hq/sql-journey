import sqlite3


connection = sqlite3.connect("constraints.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER CHECK(age >= 0 AND age <= 120),
    city TEXT NOT NULL,
    status TEXT DEFAULT 'active'
)
""")


cursor.execute("""
INSERT INTO patients (name, email, age, city)
VALUES (?, ?, ?, ?)
""", (
    "Rahul",
    "rahul@example.com",
    25,
    "Delhi"
))


connection.commit()


cursor.execute("SELECT * FROM patients")

patients = cursor.fetchall()


for patient in patients:
    print(patient)


connection.close()