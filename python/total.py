# -*- coding: utf-8 -*-
from datetime import date
from datetime import timedelta
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pandas as pd
import numpy as np

# df = pd.read_csv('corona.csv')
df = pd.read_csv('covid19.csv')

def MinMaxDate():
    data = []
    for dat in df['date']:
        data.append(date.fromisoformat(dat))
    return min(data), max(data), timedelta(days=1)

def totalDate(start_date, end_date, delta) :
    total = []
    while start_date <= end_date:
        # print(np.where(df['date'] == start_date.isoformat(), df['cases'], 0).sum())
        result = np.where(df['date'] == start_date.isoformat(), df['cases'], 0).sum()

        total.append([start_date.isoformat(), result])
        start_date += delta
    total = np.array(total) 
    return pd.DataFrame({'Date': total[:, 0], 'Value': total[:, 1]})
    # return np.array(total)

def totalState(start_date, end_date, delta, sigla) :
    total = []
    while start_date <= end_date:
        result = np.where(df['uf'] == sigla, np.where(df['date'] == start_date.isoformat(), df['cases'], 0), 0).sum()
        total.append([start_date.isoformat(), result])
        start_date += delta
    total = np.array(total) 
    return pd.DataFrame({'Date': total[:, 0], 'Value': total[:, 1]})

def formatObject (data):
    x_data = []
    y_data = []
    for d in range(1,data.shape[0]):
        x = [int(data.iloc[d-1:d].values.ravel()[1])]
        y = int(data.iloc[d].values[1])

        x_data.append(x)
        y_data.append(y)
    return np.array(x_data), np.array(y_data)

def predict(x_data, y_data):
    #Listas para armazenar as previsões de cada modelo
    y_pred = []
    y_pred_last = []
    y_pred_ma = []
    y_true = []
    #Itera pela série temporal treinando um novo modelo a cada mês
    end = y_data.shape[0]
    for i in range(1,end):
        x_train = x_data[:i,:]
        y_train = y_data[:i]
        
        x_test = x_data[i,:]
        y_test = y_data[i]

        model = LinearRegression(normalize=True)
        model.fit(x_train,y_train)

        y_pred.append(int(model.predict(x_test.reshape(1, -1))[0]))
        y_pred_last.append(int(x_test[-1]))
        y_pred_ma.append(int(x_test.mean()))
        y_true.append(int(y_test))

    return y_pred, y_pred_last, y_pred_ma, y_true, model

def predictByDate (model, start_date, y_pred, data):
    aux = []
    index = 0
    while start_date <= date.fromisoformat(data):
        result = np.where(df['date'] == start_date.isoformat(), df['date'], 0)
        # if result.any(0) != 0:
        if len(y_pred) >= index:
            if index-1 == -1:
                aux.append(
                    {
                        'index': str(index), 
                        'date': (start_date + timedelta(days=1)).isoformat(),
                        'valor': str(0)
                    })
            else:
                aux.append(
                    {
                        'index': str(index),
                        'date': (start_date + timedelta(days=1)).isoformat(),
                        'valor': str(y_pred[index-1])
                    })
        else:
            pred = int(model.predict([[int(aux[index-1]['valor'])]]))
            # print(aux[])
            # pred = int(model.predict([[aux[index-1][2]]]))
            aux.append(
                {
                    'index': str(index),
                    'date': (start_date + timedelta(days=1)).isoformat(),
                    'valor': str(pred)
                })
        index += 1
        start_date += timedelta(days=1)
    return aux

def main (date_p):
    start_date, end_date, delta = MinMaxDate()
    total = totalDate(start_date, end_date, delta)
    x_data, y_data = formatObject(total)
    y_pred, y_pred_last, y_pred_ma, y_true, model = predict(x_data, y_data)

    y_pred = np.array(y_pred)
    y_pred_last = np.array(y_pred_last)
    y_pred_ma = np.array(y_pred_ma)
    y_true = np.array(y_true)
    return (predictByDate(model, start_date, y_pred, date_p), 
            predictByDate(model, start_date, y_true, end_date.isoformat()))
    # print ('\nMean Absolute Error')
    # print ('MAE Regressão Linear', mean_absolute_error(y_pred,y_true))
    # print ('MAE Último Valor', mean_absolute_error(y_pred_last,y_true))
    # print ('MAE Média Móvel', mean_absolute_error(y_pred_ma,y_true))
    # #Imprime os erros na tela

def predict_states (date_p, sigla) :
    start_date, end_date, delta = MinMaxDate()
    total = totalState(start_date, end_date, delta, sigla) 
    x_data, y_data = formatObject(total)
    y_pred, y_pred_last, y_pred_ma, y_true, model = predict(x_data, y_data)

    y_pred = np.array(y_pred)
    y_pred_last = np.array(y_pred_last)
    y_pred_ma = np.array(y_pred_ma)
    y_true = np.array(y_true)
    return (predictByDate(model, start_date, y_pred, date_p), 
            predictByDate(model, start_date, y_true, end_date.isoformat()))
    # #Imprime os erros na tela
    # print ('\nMean Absolute Error')
    # print ('MAE Regressão Linear', mean_absolute_error(y_pred,y_true))
    # print ('MAE Último Valor', mean_absolute_error(y_pred_last,y_true))
    # print ('MAE Média Móvel', mean_absolute_error(y_pred_ma,y_true))
def mape(y_pred,y_true):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def calcular_medias():
    start_date, end_date, delta = MinMaxDate()
    total = totalDate(start_date, end_date, delta) 
    x_data, y_data = formatObject(total)
    y_pred, y_pred_last, y_pred_ma, y_true, model = predict(x_data, y_data)
    y_pred = np.array(y_pred)
    y_pred_last = np.array(y_pred_last)
    y_pred_ma = np.array(y_pred_ma)
    y_true = np.array(y_true)

    # #Imprime os erros na tela
    # print ('\nMean Absolute Percentage Error')
    # print ('MAPE Regressão Linear', mape(y_pred,y_true))
    # print ('MAPE Último Valor', mape(y_pred_last,y_true))
    # print ('MAPE Média Móvel', mape(y_pred_ma,y_true))

    # print ('\nMean Absolute Error')
    # print ('MAE Regressão Linear', mean_absolute_error(y_pred,y_true))
    # print ('MAE Último Valor', mean_absolute_error(y_pred_last,y_true))
    # print ('MAE Média Móvel', mean_absolute_error(y_pred_ma,y_true))
    return mean_absolute_error(y_pred,y_true), mean_absolute_error(y_pred_last,y_true), mean_absolute_error(y_pred_ma,y_true)

def states():
    return np.unique(df['uf'])

# main('2020-04-07')

# states()
# main('2020-04-03')
# states('2020-04-03', 'PA')