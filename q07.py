from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/soma', methods=['POST'])
def soma():
    if request.get_json(silent=True):
        params = request.get_json
        total = params['x'] + params['y']
        return {"Resultado": total}, 202
    else:
        return {'successful': False, 'status': 400, "error": "JSON não encontrado."}, 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)