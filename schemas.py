from datetime import date

from pydantic import BaseModel, Field


class AutorSchema(BaseModel):
    nombre: str = Field(min_length=2, max_length=20)
    apellido: str = Field(min_length=2, max_length=20)
    pais: str = Field(min_length=2, max_length=30)


class LibroSchema(BaseModel):
    titulo: str = Field(min_length=2, max_length=40)
    autor: int
    editorial: str = Field(min_length=2, max_length=20)
    fecha_publicacion: date
