from flask import Flask, request, json
from apiMutants.mutants import *
from conexionDB.dbMutants import consultarEstadisticasDia
from conexionDB.dbMutants import guardarSecuenciaAdn

app = Flask(__name__)

#{secuenciaAdn : ['ATGCGA','CAGTGC',"TTATGT','AGAAGG','CCGCTA','TCACGC']}
@app.route('/mutant', methods=['POST'])
def mutant():
    esMutante = False
    request_data = request.get_json()
    dna = request_data['dna']
    if (esAdnValido(dna) == True):
        if (esMutante(dna) == True):
            esMutante = True
        guardarSecuenciaAdn(dna, esMutante)
        if esMutante == True:
            return "Es un Mutante"
        else:
            return "No es un Mutante", 403
    else:
        return {"codigoRespuesta": 999, "mensajeRepuesta": "El valor enviado no es una secuencia de AND Valida"}

@app.route('/stats', methods=['GET'])
def consultar():
    return json.dumps(consultarEstadisticasDia())

if __name__ == '__main__':
    app.run(debug=True, port=4000)
