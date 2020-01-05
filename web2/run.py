import pandas as pd
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

def get_data(path):
    datas = []
    try:
        df = pd.read_csv(path, encoding='gbk')
    except:
        df = pd.read_csv(path, encoding='utf-8')
    df.fillna(0)
    for index, row in df.iterrows():
        datas.append(list(row))
    return datas

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('table', type='1'))

@app.route('/show/<string:type>/', methods=['GET'])
def table(type):
    x = type
    print(x)
    if x == '1':
        data = get_data('住宅.csv')
        return render_template('table1.html', datas=data)
    elif x == '2':
        data = get_data('2.csv')
        return render_template('table2.html', datas=data)
    elif x == '3':
        data = get_data('3.csv')
        return render_template('table3.html', datas=data)
    elif x == '4':
        data = get_data('4.csv')
        return render_template('table4.html', datas=data)
    elif x == '5':
        data = get_data('5.csv')
        return render_template('table5.html', datas=data)
    elif x == '6':
        data = get_data('6.csv')
        return render_template('table6.html', datas=data)
    elif x == '7':
        data = get_data('7.csv')
        return render_template('table7.html', datas=data)



if __name__ == '__main__':
    app.run()