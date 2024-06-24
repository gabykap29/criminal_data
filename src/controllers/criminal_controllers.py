from src.database.db import criminal_collection
from src.utils.convert_objectid import convert_object_ids
from bson import ObjectId

async def get_criminal_document(length: int = 10, skip: int = 0):
    # Obtener los delincuentes con estado True, aplicando paginación
    criminals_cursor = criminal_collection.find({"state": {'$eq': True}}).skip(skip).limit(length)
    
    criminals = await criminals_cursor.to_list(length)
    if criminals:
        criminals = convert_object_ids(criminals)
        return criminals
    else:
        return None

#funcion para obtener un delincuente por su id
async def get_criminal_document_by_id(criminal_id):
    try:
        criminal_id = ObjectId(criminal_id)
    except:
        return None
    criminal = await criminal_collection.find_one({"_id":criminal_id})
    if criminal:
        criminal = convert_object_ids(criminal)
        return criminal
    else:
        return None
    
#funcion para obtener un delincuente por su nombre
async def get_criminal_document_by_name(name, lastname, skip=0, length=10):
    criminal = criminal_collection.find({"names":name, "lastname":lastname}).skip(skip).limit(length)
    criminal = await criminal.to_list(length)
    if criminal:
        criminal = convert_object_ids(criminal)
        return criminal
    else:
        return None

#funcion para obtener un delincuente por su dni
async def get_criminal_document_by_dni(dni:str):
    criminal = await criminal_collection.find_one({"dni":dni})
    if criminal:
        criminal = convert_object_ids(criminal)
        return criminal
    else:
        return None
    

#funcion para agregar un delincuente
async def insert_criminal_document(criminal_data):
    criminal_data.update({"state":True})
    criminal = await criminal_collection.insert_one(criminal_data)
    if criminal:
        return criminal
    else:
        return None
    
#funcion para actualizar un delincuente
def update_criminal_document(criminal_id, criminal_data):
    criminal = criminal_collection.update_one({"_id":criminal_id}, {"$set":criminal_data})
    if criminal:
        return criminal
    else:
        return None
    
#funcion para eliminar un delincuente
async def delete_criminal_document(criminal_id):
    criminal = await criminal_collection.update_one({"_id":criminal_id}, {"$set":{"state":False}})
    if criminal:
        return criminal
    else:
        return None
    
#funcion para agregar una imagen a un delincuente
def add_image_to_criminal(criminal_id, image):
    criminal = criminal_collection.update_one({"_id":criminal_id}, {"$push":{"images":image}})
    if criminal:
        return criminal
    else:
        return None