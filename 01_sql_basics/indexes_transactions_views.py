import sqlite3

connection = sqlite3.connect("hospital_topic9.db")
cursor = connection.cursor()

# -------------------------
# Tables
# -------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialization TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date TEXT,

    FOREIGN KEY (patient_id)
    REFERENCES patients(id),

    FOREIGN KEY (doctor_id)
    REFERENCES doctors(id)
)
""")


# Clean old data
cursor.execute("DELETE FROM appointments")
cursor.execute("DELETE FROM doctors")
cursor.execute("DELETE FROM patients")


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
# INDEX
# -------------------------

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_patient_name
ON patients(name)
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_appointment_patient
ON appointments(patient_id)
""")


print("Indexes created successfully!")


# -------------------------
# VIEW
# -------------------------

cursor.execute("""
DROP VIEW IF EXISTS appointment_details
""")

cursor.execute("""
CREATE VIEW appointment_details AS
SELECT
    patients.name AS patient_name,
    doctors.name AS doctor_name,
    doctors.specialization,
    appointments.appointment_date
FROM appointments
JOIN patients
ON appointments.patient_id = patients.id
JOIN doctors
ON appointments.doctor_id = doctors.id
""")


# -------------------------
# Use View
# -------------------------

print("\nAppointment Details:")

cursor.execute("""
SELECT * FROM appointment_details
""")

for row in cursor.fetchall():
    print(row)


# -------------------------
# TRANSACTION
# -------------------------

try:

    cursor.execute("""
    UPDATE patients
    SET age = age + 1
    WHERE id = ?
    """, (1,))

    cursor.execute("""
    UPDATE patients
    SET age = age + 1
    WHERE id = ?
    """, (2,))

    connection.commit()

    print("\nTransaction successful!")

except Exception as error:

    connection.rollback()

    print("\nTransaction failed!")
    print(error)


connection.close()