import sqlite3


connection = sqlite3.connect("patients.db")

cursor = connection.cursor()


cursor.execute("SELECT * FROM patients")

patients = cursor.fetchall()


for patient in patients:
    print(patient)


connection.close()