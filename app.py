from flask import Flask,render_template,request
import pickle
import numpy as numpy
import pandas as pd
app = Flask(__name__)
with open('model1.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method=="GET":
        return render_template('index.html')
    if request.method=="POST":
        PM_25=request.form['PM_25']
        PM10=request.form['PM10']
        NH3=request.form['NH3']
        CO=request.form['CO']
        SO2=request.form['SO2']
        O3=request.form['O3']
        Nitro=request.form['Nitro']
        print(PM10,PM_25)
        input_variables = pd.DataFrame([[PM_25,PM10,NH3,CO,SO2,O3,Nitro]],
                                       columns=['PM2.5', 'PM10', 'NH3', 'CO', 'SO2', 'O3', 'Nitro'],
                                       dtype=float)
        print(input_variables)
        prediction = model.predict(input_variables)[0]    
        return render_template('main.html',
                                     original_input={'PM':PM_25,
                                                     'PM10':PM10,
                                                     'Nitro':Nitro,
                                                     'NH3':NH3,
                                                     'O3':O3,
                                                     'CO':CO,
                                                     'SO2':SO2,},
                                     result=round(prediction,2),
                                     )

    

if __name__ == '__main__':
    app.run(debug=True)