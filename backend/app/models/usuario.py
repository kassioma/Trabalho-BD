from fastapi import UploadFile
from pydantic import BaseModel

class UsuarioModel(BaseModel):
    matricula: int
    email: str
    senha: str
    curso: str
    # imagem: UploadFile
    nome: str
    admin: int