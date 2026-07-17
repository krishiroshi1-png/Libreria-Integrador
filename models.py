from peewee import CharField, DateField, ForeignKeyField, Model, SqliteDatabase


DB_NAME = "libreria.db"

db = SqliteDatabase(DB_NAME)


class BaseModel(Model):
    class Meta:
        database = db


class Autor(BaseModel):
    nombre = CharField(max_length=20)
    apellido = CharField(max_length=20)
    pais = CharField(max_length=30)


class Libro(BaseModel):
    titulo = CharField(max_length=40)
    autor = ForeignKeyField(
        Autor,
        backref="libros",
        on_delete="CASCADE"
    )
    editorial = CharField(max_length=20)
    fecha_publicacion = DateField()


def db_init():
    with db:
        db.create_tables([Autor, Libro], safe=True)
