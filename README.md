# Minicurso IFC

Bot de notícias da Globo

## Requisitos

- Chave API de https://newsapi.org/s/globo-api
- Python 3.x
- Ngrok

## Setup

```sh
cp .example.env .env
touch .env
pip install -r --user requirements.txt
```

## Desenvolvimento

`python app.py`


## Botão 'GET STARTED'

```sh
curl -X POST -H "Content-Type: application/json" -d "{
  'get_started':{
    'payload':'FACEBOOK_WELCOME'
  }
}" "https://graph.facebook.com/v2.10/me/messenger_profile?access_token=<MESSENGER_PAGE_ACCESS_TOKEN>"
```
