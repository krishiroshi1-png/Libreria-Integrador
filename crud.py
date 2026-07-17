from models import Autor, Libro
from schemas import AutorSchema, LibroSchema


def crear_autor(datos_autor: dict) -> Autor:
    autor_schema = AutorSchema(**datos_autor)
    autor = Autor.create(**autor_schema.model_dump())
    return autor


def crear_libro(datos_libro: dict) -> Libro:
    libro_schema = LibroSchema(**datos_libro)
    datos = libro_schema.model_dump()
    autor_id = datos.pop("autor")
    libro = Libro.create(autor=autor_id, **datos)
    return libro


def listar_libros_por_autor(autor_id: int):
    autor = Autor.get_or_none(Autor.id == autor_id)
    if autor is None:
        return []
    return list(autor.libros)
