from crud import crear_autor, crear_libro, listar_libros_por_autor
from models import db_init


def main():
    db_init()

    # crear un autor
    datos_autor = {"nombre": "Julio", "apellido": "Cortazar", "pais": "arg"}
    autor = crear_autor(datos_autor)
    print(f"Autor creado: {autor.nombre} {autor.apellido} ({autor.pais})")

    # crear un libro asociado al autor
    datos_libro = {
        "titulo": "Rayuela",
        "autor": autor.id,
        "editorial": "Sudamericana",
        "fecha_publicacion": "1963-06-28",
    }
    libro = crear_libro(datos_libro)
    print(f"Libro creado: {libro.titulo} - {libro.editorial}")

    # listar los libros de ese autor
    libros = listar_libros_por_autor(autor.id)
    print(f"Libros de {autor.nombre} {autor.apellido}:")
    for l in libros:
        print(f"  - {l.titulo} ({l.fecha_publicacion})")


if __name__ == "__main__":
    main()
