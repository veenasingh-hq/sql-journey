from sqlalchemy import select, or_, func

from database import engine, Base, SessionLocal
from models import Patient


Base.metadata.create_all(bind=engine)

db = SessionLocal()


# -------------------------
# Insert sample data
# -------------------------

existing = db.execute(
    select(Patient)
).scalars().all()

if not existing:

    patients = [
        Patient(name="Rahul", age=25, city="Delhi"),
        Patient(name="Priya", age=17, city="Lucknow"),
        Patient(name="Amit", age=45, city="Kanpur"),
        Patient(name="Neha", age=32, city="Lucknow"),
        Patient(name="Ravi", age=65, city="Delhi"),
        Patient(name="Anita", age=28, city="Kanpur"),
    ]

    db.add_all(patients)
    db.commit()


# -------------------------
# SELECT
# -------------------------

statement = select(Patient)

patients = (
    db.execute(statement)
    .scalars()
    .all()
)

print("All Patients:")

for patient in patients:
    print(patient.id, patient.name, patient.age)


# -------------------------
# WHERE
# -------------------------

statement = (
    select(Patient)
    .where(Patient.age > 30)
)

patients = (
    db.execute(statement)
    .scalars()
    .all()
)

print("\nAge > 30:")

for patient in patients:
    print(patient.name, patient.age)


# -------------------------
# OR
# -------------------------

statement = (
    select(Patient)
    .where(
        or_(
            Patient.city == "Delhi",
            Patient.city == "Lucknow"
        )
    )
)

patients = (
    db.execute(statement)
    .scalars()
    .all()
)

print("\nDelhi OR Lucknow:")

for patient in patients:
    print(patient.name, patient.city)


# -------------------------
# ORDER BY
# -------------------------

statement = (
    select(Patient)
    .order_by(Patient.age.desc())
)

patients = (
    db.execute(statement)
    .scalars()
    .all()
)

print("\nAge descending:")

for patient in patients:
    print(patient.name, patient.age)


# -------------------------
# LIMIT
# -------------------------

statement = (
    select(Patient)
    .order_by(Patient.id)
    .limit(3)
)

patients = (
    db.execute(statement)
    .scalars()
    .all()
)

print("\nFirst 3 patients:")

for patient in patients:
    print(patient.name)


# -------------------------
# PAGINATION
# -------------------------

page = 2
limit = 2

offset = (page - 1) * limit

statement = (
    select(Patient)
    .order_by(Patient.id)
    .offset(offset)
    .limit(limit)
)

patients = (
    db.execute(statement)
    .scalars()
    .all()
)

print("\nPage 2:")

for patient in patients:
    print(patient.name)


# -------------------------
# COUNT
# -------------------------

statement = select(
    func.count(Patient.id)
)

count = db.execute(statement).scalar()

print("\nTotal patients:", count)


db.close()