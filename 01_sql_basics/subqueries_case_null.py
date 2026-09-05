import sqlite3

connection = sqlite3.connect("topic7.db")
cursor = connection.cursor()

# Create patients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    phone TEXT
)
""")

# Create appointments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    appointment_date TEXT,
    FOREIGN KEY (patient_id)
    REFERENCES patients(id)
)
""")

# Clean old data for practice
cursor.execute("DELETE FROM appointments")
cursor.execute("DELETE FROM patients")

# Insert patients
patients = [
    ("Rahul", 25, "9876543210"),
    ("Priya", 16, None),
    ("Amit", 65, "9123456780"),
    ("Neha", 35, None),
    ("Ravi", 50, "9988776655")
]

cursor.executemany("""
INSERT INTO patients (name, age, phone)
VALUES (?, ?, ?)
""", patients)

# Insert appointments
appointments = [
    (1, "2026-09-05"),
    (3, "2026-09-06"),
    (5, "2026-09-07")
]

cursor.executemany("""
INSERT INTO appointments (patient_id, appointment_date)
VALUES (?, ?)
""", appointments)

connection.commit()


# -------------------------
# NULL Handling
# -------------------------

print("Patients without phone:")

cursor.execute("""
SELECT name
FROM patients
WHERE phone IS NULL
""")

for row in cursor.fetchall():
    print(row)


# -------------------------
# COALESCE
# -------------------------

print("\nPhone information:")

cursor.execute("""
SELECT
    name,
    COALESCE(phone, 'Not Available')
FROM patients
""")

for row in cursor.fetchall():
    print(row)


# -------------------------
# CASE
# -------------------------

print("\nAge Categories:")

cursor.execute("""
SELECT
    name,
    age,
    CASE
        WHEN age < 18 THEN 'Minor'
        WHEN age < 60 THEN 'Adult'
        ELSE 'Senior'
    END AS age_category
FROM patients
""")

for row in cursor.fetchall():
    print(row)


# -------------------------
# Subquery
# -------------------------

print("\nPatients older than average age:")

cursor.execute("""
SELECT name, age
FROM patients
WHERE age > (
    SELECT AVG(age)
    FROM patients
)
""")

for row in cursor.fetchall():
    print(row)


# -------------------------
# Subquery with IN
# -------------------------

print("\nPatients who have appointments:")

cursor.execute("""
SELECT name
FROM patients
WHERE id IN (
    SELECT patient_id
    FROM appointments
)
""")

for row in cursor.fetchall():
    print(row)


# -------------------------
# Combined Query
# -------------------------

print("\nCombined Query:")

cursor.execute("""
SELECT
    name,
    age,
    COALESCE(phone, 'Not Available') AS phone,
    CASE
        WHEN age < 18 THEN 'Minor'
        WHEN age < 60 THEN 'Adult'
        ELSE 'Senior'
    END AS age_category
FROM patients
WHERE id IN (
    SELECT patient_id
    FROM appointments
)
""")

for row in cursor.fetchall():
    print(row)


connection.close()