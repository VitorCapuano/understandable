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