import sqlite3

connection = sqlite3.connect("hospital_design.db")
cursor = connection.cursor()

# -------------------------
# Patients
# -------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER CHECK(age > 0)
)
""")


# -------------------------
# Doctors
# -------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialization TEXT NOT NULL
)
""")


# -------------------------
# Appointments
# -------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    appointment_date TEXT NOT NULL,

    FOREIGN KEY (patient_id)
    REFERENCES patients(id),

    FOREIGN KEY (doctor_id)
    REFERENCES doctors(id)
)
""")


# -------------------------
# Insert Patients
# -------------------------

patients = [
    ("Rahul", 25),
    ("Priya", 30),
    ("Amit", 45)
]

cursor.executemany("""
INSERT INTO patients (name, age)
VALUES (?, ?)
""", patients)


# -------------------------
# Insert Doctors
# -------------------------

doctors = [
    ("Dr. Sharma", "Cardiology"),
    ("Dr. Verma", "Dermatology")
]

cursor.executemany("""
INSERT INTO doctors (name, specialization)
VALUES (?, ?)
""", doctors)


# -------------------------
# Insert Appointments
# -------------------------

appointments = [
    (1, 1, "2026-09-10"),
    (2, 2, "2026-09-11"),
    (3, 1, "2026-09-12")
]

cursor.executemany("""
INSERT INTO appointments
(patient_id, doctor_id, appointment_date)
VALUES (?, ?, ?)
""", appointments)


connection.commit()


# -------------------------
# Display Database
# -------------------------

print("Patients:")

cursor.execute("""
SELECT * FROM patients
""")

for row in cursor.fetchall():
    print(row)


print("\nDoctors:")

cursor.execute("""
SELECT * FROM doctors
""")

for row in cursor.fetchall():
    print(row)


print("\nAppointments:")

cursor.execute("""
SELECT * FROM appointments
""")

for row in cursor.fetchall():
    print(row)


connection.close()