import pymongo
import json
from datetime import datetime
clientMongo = pymongo.MongoClient("mongodb+srv://jandreshd:ValeIsa2405@clspython.klugh.mongodb.net/db1?retryWrites=true&w=majority")
db = clientMongo.db1


def consultarCollecionesBD():
    for i in db.list_collection_names():
        print (i)

def consultarEstadisticasDia():
    mutantes = db.mutants.find({"esMutante": True}).count()
    humanos = db.mutants.find({"esMutante": False}).count()
    proporcion = mutantes/humanos
    estadisticas = {'count_mutant_dna': mutantes,'count_human_dna':humanos, 'ratio': proporcion}
    return estadisticas

def existeDNA(dna):
    query = {"adn": str(dna)}
    resultado = db.mutants.find_one(query)
    return resultado

def guardarSecuenciaAdn(dna, esMutant):
    if existeDNA(dna) is None:
        fechaSistema = datetime.now().strftime('%Y-%m-%d') 
        cantidad = db.mutants.count_documents({})   
        dic={'_id':cantidad + 1,'fecha':fechaSistema, 'adn': str(dna), 'esMutante': esMutant}
        db.mutants.insert_one(dic)
        return {"codigoRespuesta": 0, "mensajeRepuesta": "Secuencia ADN Registrada Exitosamente"}