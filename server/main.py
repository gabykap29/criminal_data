from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.criminal_routes import criminal_routes

# instancio desde la clase FastApi
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True})

origins = [
    "*"
]

#Configurar cors
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(criminal_routes, tags=['criminal'])