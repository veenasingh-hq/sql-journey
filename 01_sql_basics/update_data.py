import sqlite3


connection = sqlite3.connect("patients.db")

cursor = connection.cursor()


cursor.execute("""
UPDATE patients
SET city = ?
WHERE id = ?
""", ("Lucknow", 1))


connection.commit()

connection.close()


print("Patient updated successfully!")