import sqlite3


connection = sqlite3.connect("patients.db")

cursor = connection.cursor()


cursor.execute("""
INSERT INTO patients (name, age, city)
VALUES (?, ?, ?)
""", ("Rahul", 25, "Delhi"))


connection.commit()
connection.close()


print("Patient inserted successfully!")