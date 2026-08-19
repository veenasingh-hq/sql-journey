import sqlite3


connection = sqlite3.connect("patients.db")

cursor = connection.cursor()


cursor.execute("""
DELETE FROM patients
WHERE id = ?
""", (3,))


connection.commit()

connection.close()


print("Patient deleted successfully!")