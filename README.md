#understandable
[![Build Status](https://travis-ci.org/VitorCapuano/understandable.svg?branch=master)](https://travis-ci.org/VitorCapuano/understandable)

Understandable api. [Documentação](http://VitorCapuano.github.io/understandable/).

# Setar projeto
Criar e ativar virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Instalar dependências:

```bash
pip install -r requirements/local.txt
```

Migrar banco de dados e criar superusuário:
```bash
python understand/manage.py migrate
python understand/manage.py createsuperuser
```

Iniciar em desenvolvimento a aplicação:
```bash
python understand/manage.py runserver
```

# Understand API GUIDE

# Autenticação
Para os clientes se autenticarem, o token deve ser incluido como Authorization HTTP header. Deve ser informado `Token` e depois o uuid do client. Exemplo:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

Quando o usuário enviar um token errado, receberá como resposta `401 Unauthorized` com `WWW-Authenticate` no header. Exemplo:

```
WWW-Authenticate: Token
```

Exemplo de request:

```bash
curl -X GET http://127.0.0.1:8000/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

## Recuperando seu token
O token terá retorno, caso o usuário esteja registado e envie na request o username e o password. Exemplo:

**Requisição**:

`POST` `api-token-auth/`

Parametros:

Nome | Tipo | Descrição
---|---|---
username | string | username
password | string | password

**Resposta**:
```
json
{
    "token" : "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```
