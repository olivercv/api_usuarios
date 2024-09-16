from ninja import Schema


class UsuarioSchema(Schema):
    id: int
    nombre: str
    apellidoPaterno: str
    apellidoMaterno: str
    edad: int
    nombreCuenta: str
    contrasena: str


class UsuarioCreateSchema(Schema):
    nombre: str
    apellidoPaterno: str
    apellidoMaterno: str
    edad: int
    nombreCuenta: str
    contrasena: str