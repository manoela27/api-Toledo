from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI()

class Cliente(BaseModel):
    nome: str = Field(..., max_length=20)
    tipo_atendimento: str = Field(..., pattern="^(N|P)$") 
    data_chegada: datetime = datetime.now()
    posicao: int
    atendido: bool = False

fila = []

@app.get("/fila")
async def listar_fila():
    fila_nao_atendida = [cliente for cliente in fila if not cliente.atendido]
    return fila_nao_atendida or []

@app.get("/fila/{id}")
async def obter_cliente(id: int):
    if 0 <= id < len(fila):
        cliente = fila[id]
        return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado na posição especificada.")

@app.post("/fila")
async def adicionar_cliente(cliente: Cliente):
    cliente.posicao = len(fila) + 1 
    fila.append(cliente)
    return {"mensagem": "Cliente adicionado com sucesso.", "cliente": cliente}

@app.put("/fila")
async def atualizar_fila():
    for cliente in fila:
        if cliente.posicao == 1:
            cliente.posicao = 0
            cliente.atendido = True
        elif cliente.posicao > 1:
            cliente.posicao -= 1
    return {"mensagem": "Fila atualizada com sucesso.", "fila": fila}

@app.delete("/fila/{id}")
async def remover_cliente(id: int):
    if 0 <= id < len(fila):
        fila.pop(id)
        for i, cliente in enumerate(fila):
            cliente.posicao = i + 1
        return {"mensagem": "Cliente removido com sucesso."}
    raise HTTPException(status_code=404, detail="Cliente não encontrado na posição especificada.")
