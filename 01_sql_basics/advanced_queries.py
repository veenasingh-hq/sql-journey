import sqlite3


connection = sqlite3.connect("patients.db")

cursor = connection.cursor()


# 1. Sort by age
cursor.execute("""
SELECT * FROM patients
ORDER BY age DESC
""")

patients = cursor.fetchall()

print("Patients sorted by age:")

for patient in patients:
    print(patient)


# 2. Limit results
cursor.execute("""
SELECT * FROM patients
LIMIT 2
""")

patients = cursor.fetchall()

print("\nFirst 2 patients:")

for patient in patients:
    print(patient)


# 3. Search by name
cursor.execute("""
SELECT * FROM patients
WHERE name LIKE ?
""", ("A%",))

patients = cursor.fetchall()

print("\nNames starting with A:")

for patient in patients:
    print(patient)


# 4. Multiple cities
cursor.execute("""
SELECT * FROM patients
WHERE city IN (?, ?)
""", ("Delhi", "Lucknow"))

patients = cursor.fetchall()

print("\nPatients from Delhi or Lucknow:")

for patient in patients:
    print(patient)


# 5. Age range
cursor.execute("""
SELECT * FROM patients
WHERE age BETWEEN ? AND ?
""", (20, 30))

patients = cursor.fetchall()

print("\nPatients between age 20 and 30:")

for patient in patients:
    print(patient)


connection.close()