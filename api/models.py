from sqlalchemy import Column, Integer, String
from database import Base

class Alumno(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    carrera = Column(String(100))
    semestre = Column(Integer)