# Desafio Framework

API desenvolvida em Django como parte do desafio técnico para a Framework

## Como inicializar a aplicação

### Requisitos

- Python 3
- pip
- Docker (Para utilizar o modo 2)
### Modo 1
- Inicie um terminal na raíz do projeto
> pip install virtualenv  
> virtualenv venv  
> Windows: venv\Scripts\activate || unix: source venv/bin/activate  
> pip install -r requirements.txt  
> python manage.py runserver

### Modo 2 - Docker
- Inicie um terminal no diretório docker
> docker-compose up
## Endpoints
### Auth  
Para gerar o token de autenticação  
`localhost:8000/api/auth`
#### Parametros
- username: admin
- password: admin
  
### Desafio
Retorno dos dados solicitados  
`localhost:8000/api/desafio`
#### Parametros
- Authorization: Token 5c3e17aa5e680f101b47cd7da5fc5d73135bd1ca

