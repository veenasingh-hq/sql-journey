from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    age = Column(Integer)

    appointments = relationship(
        "Appointment",
        back_populates="patient"
    )


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    appointment_date = Column(String, nullable=False)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id")
    )

    patient = relationship(
        "Patient",
        back_populates="appointments"
    )