import sqlite3


connection = sqlite3.connect("patients.db")

cursor = connection.cursor()


# --------------------------------
# Total Patients
# --------------------------------

cursor.execute("""
SELECT COUNT(*)
FROM patients
""")

result = cursor.fetchone()

print("Total Patients:", result[0])


# --------------------------------
# Average Age
# --------------------------------

cursor.execute("""
SELECT AVG(age)
FROM patients
""")

result = cursor.fetchone()

print("Average Age:", result[0])


# --------------------------------
# Minimum Age
# --------------------------------

cursor.execute("""
SELECT MIN(age)
FROM patients
""")

result = cursor.fetchone()

print("Minimum Age:", result[0])


# --------------------------------
# Maximum Age
# --------------------------------

cursor.execute("""
SELECT MAX(age)
FROM patients
""")

result = cursor.fetchone()

print("Maximum Age:", result[0])


# --------------------------------
# Patients per City
# --------------------------------

cursor.execute("""
SELECT city, COUNT(*)
FROM patients
GROUP BY city
""")

results = cursor.fetchall()

print("\nPatients per city:")

for result in results:
    print(result)


# --------------------------------
# Average Age per City
# --------------------------------

cursor.execute("""
SELECT city, AVG(age)
FROM patients
GROUP BY city
""")

results = cursor.fetchall()

print("\nAverage age per city:")

for result in results:
    print(result)


# --------------------------------
# Cities with More Than 1 Patient
# --------------------------------

cursor.execute("""
SELECT city, COUNT(*)
FROM patients
GROUP BY city
HAVING COUNT(*) > 1
""")

results = cursor.fetchall()

print("\nCities with more than 1 patient:")

for result in results:
    print(result)


connection.close()