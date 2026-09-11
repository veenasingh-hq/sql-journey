from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from schemas import PatientCreate, PatientResponse
import crud


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Patient API"
)


# -------------------------
# Database Dependency
# -------------------------

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# -------------------------
# CREATE
# -------------------------

@app.post(
    "/patients",
    response_model=PatientResponse
)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):

    return crud.create_patient(
        db,
        patient
    )


# -------------------------
# GET ALL
# -------------------------

@app.get(
    "/patients",
    response_model=list[PatientResponse]
)
def read_patients(
    db: Session = Depends(get_db)
):

    return crud.get_patients(db)


# -------------------------
# GET ONE
# -------------------------

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


# -------------------------
# UPDATE
# -------------------------

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


# -------------------------
# DELETE
# -------------------------

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