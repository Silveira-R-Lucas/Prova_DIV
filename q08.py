from flask import Flask, request
import json

app = Flask(__name__)

count = 0

@app.route('/contador', methods=['POST'])
def new_value():
    if request.get_json(silent=True):
        params = request.get_json()
        get_value = list(params.values())

        if isinstance(get_value[0], int):
            count = get_value
            return {"numero": count}, 201

        return {'successful': False, 'status': 400, "error": "Somente números são aceitos na requisição"}, 400
    else:
        return {'successful': False, 'status': 400, "error": "JSON não encontrado."}, 400

@app.route('/contador', methods=['GET'])
def get_value():
    return {"numero": count}, 200

@app.route('/contador/incrementa',  methods=['PUT'])
def incrementa():
    count += 1
    return {"numero": count}, 202

@app.route('/contador', methods=['DELETE'])
def delete():
    count = 0
    return {"numero": count}, 202

if __name__ == '__main__':
    app.run(debug=True)