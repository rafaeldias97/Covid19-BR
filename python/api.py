from total import main, predict_states, states, calcular_medias
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/predict')
def predict():
    date = request.args.get('date')
    predict, true = main(date)
    # return  json.dumps(predict)
    return Response(json.dumps({'predict': predict, 'trueValue': true }),  mimetype='application/json')
    # return jsonify(result=predict)
    # return ('{ "predict":' + str(predict) + ', "trueObj": '+ str(true) + ' }')

@app.route('/api/predict-state')
def predict_state():
    date = request.args.get('date')
    uf = request.args.get('uf')
    predict, true = predict_states(date, uf)
    return ('{ "predict":' + str(predict) + ', "trueObj": '+ str(true) + ' }')

@app.route('/api/states')
def states_route():
    return str(states())

@app.route('/api/medias')
def medias():
    RegressaoLinear, UltimoValor, MediaMovel = calcular_medias()
    return Response(json.dumps({
        'regressaoLinear': RegressaoLinear,
        'ultimoValor': UltimoValor,
        'mediaMovel': MediaMovel 
    }),  mimetype='application/json')

if __name__ == '__main__':
    app.run()