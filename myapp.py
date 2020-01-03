from flask import Flask,render_template
from flask import request
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pickle


app=Flask(__name__)
@app.route('/')
def hello_world():
	return render_template('Index.html')
    
@app.route('/predict',methods=['POST'])
def get_result():
    poly=pickle.load(open('poly.pkl','rb'))
    model=pickle.load(open('model.pkl','rb'))
    query=[[float(request.form['exp'])]]
    X_query=poly.transform(query)
    sal=model.predict(X_query)
    return 'Dear'+" "+request.form["nm"]+" "+'your salary for'+" "+request.form["exp"]+" "+'years experience is:'+" "+str(sal)

if __name__=='__main__':
    app.run(debug=True)
    
    