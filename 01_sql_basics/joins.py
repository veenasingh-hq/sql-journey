import sqlite3


connection = sqlite3.connect("joins.db")

cursor = connection.cursor()


# Patients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")


# Appointments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    appointment_date TEXT,
    FOREIGN KEY (patient_id)
    REFERENCES patients(id)
)
""")


# Insert patients
cursor.execute("""
INSERT INTO patients (name)
VALUES (?)
""", ("Rahul",))

cursor.execute("""
INSERT INTO patients (name)
VALUES (?)
""", ("Priya",))

cursor.execute("""
INSERT INTO patients (name)
VALUES (?)
""", ("Amit",))


# Insert appointments
cursor.execute("""
INSERT INTO appointments (patient_id, appointment_date)
VALUES (?, ?)
""", (1, "2026-09-05"))

cursor.execute("""
INSERT INTO appointments (patient_id, appointment_date)
VALUES (?, ?)
""", (2, "2026-09-06"))


connection.commit()


# INNER JOIN
cursor.execute("""
SELECT patients.name, appointments.appointment_date
FROM patients
INNER JOIN appointments
ON patients.id = appointments.patient_id
""")

results = cursor.fetchall()

print("INNER JOIN:")

for result in results:
    print(result)


# LEFT JOIN
cursor.execute("""
SELECT patients.name, appointments.appointment_date
FROM patients
LEFT JOIN appointments
ON patients.id = appointments.patient_id
""")

results = cursor.fetchall()

print("\nLEFT JOIN:")

for result in results:
    print(result)


connection.close()