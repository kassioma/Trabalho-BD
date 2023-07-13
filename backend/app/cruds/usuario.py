import json
from fastapi import APIRouter, File, HTTPException, UploadFile
import aiofiles
from app.models.usuario import UsuarioModel
import app.db.main as db

router = APIRouter(
    prefix="/Usuarios",
    tags=["Usuarios"],
    responses={404: {"description": "Not Found"}}
)

@router.post("/criar-usuario")
def criarUsuario(body: UsuarioModel):
    try:
        body
        listaKeys = []
        listaValues = []
        for campo in body:
            listaKeys.append(campo[0])
            listaValues.append(str(campo[1]) if type(campo[1]) == int else f'"{campo[1]}"')
        db.executeInsert(listaValues, listaKeys, "usuarios")
        return body
    except:
        body = json.loads(body.json())
        return HTTPException(
            status_code=409,
            detail=f'O usuário com a matrícula {body["matricula"]}'
        )

@router.post("/atualiza-foto/{matricula}")
async def atualizaFoto(matricula: int, file: UploadFile = File(...)):
    print(file, matricula)
    async with aiofiles.open(f"/home/{file.filename}", "wb") as fout:
        content = await file.read()
        await fout.write(content)
    db.executeInsertPhoto(f"/var/lib/mysql-files/{file.filename}", "usuarios", matricula)