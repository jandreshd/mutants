from flask import Flask, request, json
from apiMutants.mutants import *
from conexionDB.dbMutants import consultarEstadisticas

app = Flask(__name__)

#{secuenciaAdn : ['ATGCGA','CAGTGC',"TTATGT','AGAAGG','CCGCTA','TCACGC']}
@app.route('/mutant', methods=['POST'])
def mutant():
    request_data = request.get_json()
    adn = request_data['adn']
    if (esAdnValido(adn) == True):
        if (esMutante(adn) == True):
            return "Es un Mutante"
        else:
            return "No es un Mutante", 403
    else:
        return {"respuesta": "El valor enviado no es una secuencia de AND Valida"}

@app.route('/stats', methods=['GET'])
def consultar():
    fechaSistema = datetime.now().strftime('%Y-%m-%d') 
    return json.dumps(consultarEstadisticas(fechaSistema))


if __name__ == '__main__':
    app.run(debug=True, port=4000)
