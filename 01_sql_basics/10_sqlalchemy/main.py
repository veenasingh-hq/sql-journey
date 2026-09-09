from database import engine, Base, SessionLocal
from models import Patient, Appointment


Base.metadata.create_all(bind=engine)

db = SessionLocal()


# Create patient
patient = Patient(
    name="Rahul",
    age=25
)

db.add(patient)
db.commit()
db.refresh(patient)


# Create appointments
appointment1 = Appointment(
    appointment_date="2026-09-10",
    patient=patient
)

appointment2 = Appointment(
    appointment_date="2026-09-15",
    patient=patient
)

db.add_all([
    appointment1,
    appointment2
])

db.commit()


# Patient → Appointments

print("Patient:", patient.name)

for appointment in patient.appointments:
    print(
        appointment.id,
        appointment.appointment_date
    )


# Appointment → Patient

print("\nAppointment Patient:")

appointment = db.query(Appointment).first()

print(
    appointment.appointment_date,
    appointment.patient.name
)


db.close()