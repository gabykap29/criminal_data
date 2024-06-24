from fastapi import APIRouter
from src.controllers.criminal_controllers import *
from httpx import Response
from fastapi.responses import JSONResponse


criminal_routes = APIRouter()

@criminal_routes.get('/', tags=['criminal'])
async def prueba_server():
    return 'Servidor funcionando!'

@criminal_routes.get('/criminals/{length}/{skip}', tags=['criminal'])
async def get_all_criminals(length: int, skip: int):
    criminals = await get_criminal_document(length, skip)
    if criminals is not None:
        response = JSONResponse(content=criminals, status_code=200)
        return response
    else:
        response = JSONResponse(content='No se encontraron delincuentes', status_code=404)
        return response

@criminal_routes.get('/criminals/{criminal_id}', tags=['criminal'])
async def get_criminal_by_id(criminal_id):
    criminal_id = str(criminal_id)
    criminal = await get_criminal_document_by_id(criminal_id)
    if criminal is not None:
        response = JSONResponse(content=criminal, status_code=200)
        return response
    else:
        response = JSONResponse(content='No se encontró el delincuente', status_code=404)
        return response

@criminal_routes.post('/criminals', tags=['criminal'])
async def insert_criminal(criminal_data: dict):
    criminal = await insert_criminal_document(criminal_data)
    if criminal is not None:
        response = JSONResponse(content="Agregado con exito!", status_code=201)
        return response
    else:
        response = JSONResponse(content='No se pudo agregar el delincuente', status_code=404)
        return response

@criminal_routes.get('/criminals/name/{name}/{lastname}/{skip}/{length}', tags=['criminal'])
async def get_criminal_by_name(name: str, lastname: str, skip: int, length: int):
    criminal = await get_criminal_document_by_name(name, lastname, skip, length)
    if criminal is not None:
        response = JSONResponse(content=criminal, status_code=200)
        return response
    else:
        response = JSONResponse(content='No se encontró el delincuente', status_code=404)
        return response
    
@criminal_routes.get('/criminals/dni/{dni}', tags=['criminal'])
async def get_criminal_by_dni(dni):
    dni = str(dni)
    criminal = await get_criminal_document_by_dni(dni)
    if criminal is not None:
        response =  JSONResponse(content=criminal, status_code=200)
        return response
    else:
        response = JSONResponse(content='No se encontró el delincuente', status_code=404)
        return response
    
@criminal_routes.put('/criminals/{criminal_id}', tags=['criminal'])
async def update_criminal(criminal_id: str, criminal_data: dict):
    criminal = update_criminal_document(criminal_id, criminal_data)
    if criminal is not None:
        response = JSONResponse(content='Actualizado con exito!', status_code=201)
        return response
    else:
        response = JSONResponse(content='No se pudo actualizar el delincuente', status_code=404)
        return response
    
@criminal_routes.put('/criminals/delete/{criminal_id}', tags=['criminal'])
async def delete_criminal(criminal_id: str):
    criminal =  await delete_criminal_document(criminal_id)
    if criminal is not None:
        response = JSONResponse(content='Eliminado con exito!', status_code=201)
        return response
    else:
        response = JSONResponse(content='No se pudo eliminar el delincuente', status_code=404)
        return response
    
@criminal_routes.put('/criminal/images/{criminal_id}', tags=['criminal'])
async def add_imagel(criminal_id: str, image: str):
    criminal = add_image_to_criminal(criminal_id, image)
    if criminal is not None:
        response = JSONResponse(content='Imagen agregada con exito!', status_code=201)
        return response
    else:
        response = JSONResponse(content='No se pudo agregar la imagen', status_code=404)
        return response