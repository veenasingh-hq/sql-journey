from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import Base, SessionLocal, engine
from schemas import PatientCreate, PatientResponse
import crud


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Patient API - PostgreSQL"
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post(
    "/patients",
    response_model=PatientResponse
)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    return crud.create_patient(db, patient)


@app.get(
    "/patients",
    response_model=list[PatientResponse]
)
def read_patients(
    db: Session = Depends(get_db)
):
    return crud.get_patients(db)


@app.get(
    "/patients/{patient_id}",
    response_model=PatientResponse
)
def read_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = crud.get_patient(
        db,
        patient_id
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@app.put(
    "/patients/{patient_id}",
    response_model=PatientResponse
)
def update_patient(
    patient_id: int,
    patient_data: PatientCreate,
    db: Session = Depends(get_db)
):
    patient = crud.update_patient(
        db,
        patient_id,
        patient_data
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@app.delete("/patients/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = crud.delete_patient(
        db,
        patient_id
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {
        "message": "Patient deleted successfully"
    }