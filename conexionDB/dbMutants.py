import pymongo
from datetime import datetime
clientMongo = pymongo.MongoClient("mongodb+srv://jandreshd:ValeIsa2405@clspython.klugh.mongodb.net/db1?retryWrites=true&w=majority")
db = clientMongo.db1


def consultarCollecionesBD():
    for i in db.list_collection_names():
        print (i)

def consultarEstadisticas(fecha):
    
    query = {"dateCount": fecha}
    resultado = format(f"[{db.mutants.find_one(query)}]")
    return resultado

def guardarEstadistica(fecha):
    
    numDocFrases = db.collectionFrases.count_documents({})   
    request_data = request.get_json()  
    frase = request_data['frase']
    dic={'_id':numDocFrases+1,'frase':frase}
    db.collectionFrases.insert_one(dic)
    numDocFrases = db.collectionFrases.count_documents({})   
    return {"Respuesta":"A new phrase has been inserted successfully"}