from sqlalchemy.orm import Session

from models import Patient
from schemas import PatientCreate


def create_patient(
    db: Session,
    patient_data: PatientCreate
):
    patient = Patient(
        name=patient_data.name,
        age=patient_data.age,
        phone=patient_data.phone
    )

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient


def get_patients(db: Session):
    return db.query(Patient).all()


def get_patient(
    db: Session,
    patient_id: int
):
    return (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )


def update_patient(
    db: Session,
    patient_id: int,
    patient_data: PatientCreate
):
    patient = get_patient(db, patient_id)

    if not patient:
        return None

    patient.name = patient_data.name
    patient.age = patient_data.age
    patient.phone = patient_data.phone

    db.commit()
    db.refresh(patient)

    return patient


def delete_patient(
    db: Session,
    patient_id: int
):
    patient = get_patient(db, patient_id)

    if not patient:
        return None

    db.delete(patient)
    db.commit()

    return patient