API de Fila de Atendimento
Esta é uma API desenvolvida com FastAPI para gerenciar uma fila de atendimento de clientes. Ela oferece endpoints para listar, adicionar, atualizar e remover clientes da fila.

Funcionalidades
A API permite realizar as seguintes operações:

Listar todos os clientes não atendidos: Retorna todos os clientes na fila que ainda não foram atendidos.
Obter cliente específico: Retorna as informações de um cliente baseado na posição da fila.
Adicionar cliente à fila: Permite adicionar um novo cliente à fila.
Atualizar a fila: Atualiza a posição dos clientes após o atendimento do primeiro cliente da fila.
Remover cliente da fila: Remove um cliente da fila e ajusta as posições dos demais.
Endpoints
1. GET /fila
Lista todos os clientes não atendidos na fila.

Resposta (200 OK):

json
Copiar código
[
  {
    "nome": "João",
    "tipo_atendimento": "P",
    "data_chegada": "2024-11-24T13:45:00",
    "posicao": 1,
    "atendido": false
  },
  {
    "nome": "Maria",
    "tipo_atendimento": "N",
    "data_chegada": "2024-11-24T13:50:00",
    "posicao": 2,
    "atendido": false
  }
]
2. GET /fila/{id}
Obtém um cliente específico na fila pelo ID (posição).

Exemplo de requisição:

bash
Copiar código
GET /fila/1
Resposta (200 OK):

json
Copiar código
{
  "nome": "João",
  "tipo_atendimento": "P",
  "data_chegada": "2024-11-24T13:45:00",
  "posicao": 1,
  "atendido": false
}
Resposta (404 Not Found): Caso o ID não seja válido.

3. POST /fila
Adiciona um novo cliente à fila.

Exemplo de requisição:

bash
Copiar código
POST /fila
Content-Type: application/json

{
  "nome": "Carlos",
  "tipo_atendimento": "N",
  "data_chegada": "2024-11-24T14:00:00",
  "posicao": 3,
  "atendido": false
}
Resposta (201 Created):

json
Copiar código
{
  "mensagem": "Cliente adicionado com sucesso.",
  "cliente": {
    "nome": "Carlos",
    "tipo_atendimento": "N",
    "data_chegada": "2024-11-24T14:00:00",
    "posicao": 3,
    "atendido": false
  }
}
4. PUT /fila
Atualiza a fila, promovendo o primeiro cliente para atendido e ajustando as posições dos demais.

Exemplo de requisição:

bash
Copiar código
PUT /fila
Resposta (200 OK):

json
Copiar código
{
  "mensagem": "Fila atualizada com sucesso.",
  "fila": [
    {
      "nome": "Carlos",
      "tipo_atendimento": "N",
      "data_chegada": "2024-11-24T14:00:00",
      "posicao": 1,
      "atendido": false
    },
    {
      "nome": "Maria",
      "tipo_atendimento": "N",
      "data_chegada": "2024-11-24T13:50:00",
      "posicao": 2,
      "atendido": false
    }
  ]
}
5. DELETE /fila/{id}
Remove um cliente específico da fila e ajusta as posições dos demais.

Exemplo de requisição:

bash
Copiar código
DELETE /fila/1
Resposta (200 OK):

json
Copiar código
{
  "mensagem": "Cliente removido com sucesso."
}
Resposta (404 Not Found): Caso o ID não seja válido.

Instalação
Clone o repositório:

bash
Copiar código
git clone <url_do_repositorio>
Navegue até o diretório do projeto:

bash
Copiar código
cd <diretorio_do_projeto>
Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

Windows:
bash
Copiar código
.\venv\Scripts\activate
Linux/MacOS:
bash
Copiar código
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Inicie o servidor:

bash
Copiar código
uvicorn main:app --reload
Testando a API
Após iniciar o servidor, você pode acessar a API em http://127.0.0.1:8000 e testar os endpoints descritos acima. O Swagger UI estará disponível em http://127.0.0.1:8000/docs, onde você pode interagir com a API de forma visual.

Dependências
FastAPI: Framework para criação da API.
Pydantic: Para validação de dados.
Uvicorn: Servidor ASGI para rodar a aplicação.
