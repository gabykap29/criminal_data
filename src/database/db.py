from motor.motor_asyncio import AsyncIOMotorClient as AMC
import os

#Conexión a mongodb
mongo_details = os.getenv("MONGO_DETAILS", "mongodb://127.0.0.1:27017/")
client = AMC(mongo_details)
database = client["criminal_database"]

#Inicialización de colecciones

criminal_collection = database.get_collection("criminals")
criminal_relationships_collection = database.get_collection('criminal_relationships')
criminal_history_collection = database.get_collection("criminal_history")
crimen_type_collection = database.get_collection("crimen_type")
images_collection = database.get_collection('images')
users_collection = database.get_collection('users')
maps_cordenates = database.get_collection('maps_cordenates')