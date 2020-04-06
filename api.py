from total import main, predict_states, states
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/predict')
def predict():
    date = request.args.get('date')
    predict, true = main(date)
    return ('{ predict:' + str(predict) + ', true: ' + str(true) + '}')

@app.route('/api/predict-state')
def predict_state():
    date = request.args.get('date')
    uf = request.args.get('uf')
    predict, true = predict_states(date, uf)
    return ('{ predict:' + str(predict) + ', true: ' + str(true) + '}')

@app.route('/api/states')
def states_route():
    return str(states())

if __name__ == '__main__':
    app.run()