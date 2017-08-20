#understandable
[![Build Status](https://travis-ci.org/VitorCapuano/understandable.svg?branch=master)](https://travis-ci.org/VitorCapuano/understandable)

Understandable api. Check out the project's [documentation](http://VitorCapuano.github.io/understandable/).

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

# Automated Deployment
Deployment is handled via Travis. When builds pass Travis will automatically deploy that branch to Heroku. Enable this with:
```bash
travis encrypt $(heroku auth:token) --add deploy.api_key
```
