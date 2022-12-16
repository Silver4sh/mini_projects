import pandas as pd

def create_bulk_data():
    import os, csv
    curr_dir = os.getcwd()
    with open(f'{curr_dir}\data.csv', 'w') as csv_file:
        fieldname = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
        writer = csv.writer(csv_file)
        writer.writerow(fieldname)
    print('--------------------------------------------------------')
    print('Isi Nilai Kuisioner di dalam file yang diberikan.')
    print('Directori File berada di:', curr_dir)
    print('!!! FILE HARUS BERFORMAT CSV !!!')
    print('--------------------------------------------------------')

def import_data():
    data = pd.read_csv('data.csv')
    data = data.dropna(how='all', axis=1)
    return data

## Uji
def test(data):
    n = data.shape[0]
    sumx = data.sum()
    sumy = data.sum(axis=1)
    sumxx = sumx ** 2
    sumyy = sumy ** 2

    def realibilitas():
        var_per_p = []
        for i in range(data.shape[1]):
            var_per_p.append((sumxx[i] - (sumx[i]**2/n))/n)
        var_p = (sumyy.sum() - (sumy.sum() / n)) / n
        try:
            result = (n / (n - 1)) * (1 - (sum(var_per_p) / var_p))
        except ZeroDivisionError:
            return 'Data yang diberikan salah'
        return result

    def validatas():
        import numpy as np
        sumxyxy = ((data ** 2) * sumx).sum()
        sumxy = sumx * sumy.sum()
        result = []
        try:
            for i in range(data.shape[1]):
                result.append(((n * sumxy[i]) - (sumx[i] * sumy.sum())) / np.sqrt(((n * sumxx[i]) - sumx[i] ** 2) * ((n * sumxyxy) - (sumy.sum() ** 2))))
        except ZeroDivisionError:
            return 'Data yang diberikan salah'
        return result
    
    result = [realibilitas(), validatas()]
    return result

def regresion(data):
    from sklearn import linear_model as lm
    def linier_regression():
        data = data
        data.insert(data.shape[1], 'y', list(data.sum(axis=1)), True)
        n = data.shape[1]
        x = data[data.columns[:n-1]].values
        y = data[data.columns[n-1]]
        reg = lm.LinerRegresion().fit(x, y)
        coef = reg.coef_
        return coef


############Running############
data = import_data()



datauji = test(data)
realibilitas = datauji[0]
validitas = datauji[1]
###############################