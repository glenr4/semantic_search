# Semantic Search
Note: this assumes you are running on Linux, if you are using Windows it may not work but you can always use: [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)

## Initialisation
- Download model: need to write a script
- Start Elastic Search: `docker compose up --detach`

## Indexing Pipeline
`python3 indexingPipeline.py`

## REST API
`uvicorn qandaApi:app --reload`  // qandaApi.py

Swagger: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
