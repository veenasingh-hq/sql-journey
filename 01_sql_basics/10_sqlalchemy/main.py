from database import engine, Base, SessionLocal
from models import Patient


# Create tables
Base.metadata.create_all(bind=engine)


# Create session
db = SessionLocal()


# -------------------------
# CREATE
# -------------------------

patient = Patient(
    name="Rahul",
    age=25,
    phone="9876543210"
)

db.add(patient)
db.commit()
db.refresh(patient)

print("Created:")
print(patient.id, patient.name)


# -------------------------
# READ
# -------------------------

patients = db.query(Patient).all()

print("\nAll Patients:")

for patient in patients:
    print(
        patient.id,
        patient.name,
        patient.age,
        patient.phone
    )


# -------------------------
# FILTER
# -------------------------

patients = (
    db.query(Patient)
    .filter(Patient.age > 20)
    .all()
)

print("\nPatients older than 20:")

for patient in patients:
    print(patient.name)


# -------------------------
# UPDATE
# -------------------------

patient = (
    db.query(Patient)
    .filter(Patient.name == "Rahul")
    .first()
)

if patient:
    patient.age = 26
    db.commit()

    print("\nUpdated:")
    print(patient.name, patient.age)


# -------------------------
# DELETE
# -------------------------

patient = (
    db.query(Patient)
    .filter(Patient.name == "Rahul")
    .first()
)

if patient:
    db.delete(patient)
    db.commit()

    print("\nPatient deleted")


# Close session
db.close()