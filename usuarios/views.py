from django.shortcuts import render

# Create your views here.
from ninja import Router
from usuarios.models import Usuario
from usuarios.schemas import UsuarioSchema, UsuarioCreateSchema
from django.shortcuts import get_object_or_404

router = Router()


@router.get("/usuarios", response=list[UsuarioSchema])
def list_usuarios(request):
    return list(Usuario.objects.all())


@router.get("/usuarios/{usuario_id}", response=UsuarioSchema)
def get_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return usuario


@router.post("/usuarios", response=UsuarioSchema)
def create_usuario(request, data: UsuarioCreateSchema):
    usuario = Usuario.objects.create(**data.dict())
    return usuario


@router.put("/usuarios/{usuario_id}", response=UsuarioSchema)
def update_usuario(request, usuario_id: int, data: UsuarioCreateSchema):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    for attr, value in data.dict().usuarios():
        setattr(usuario, attr, value)
    usuario.save()
    return usuario


@router.delete("/usuarios/{usuario_id}", response=dict)
def delete_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return {"success": True}
