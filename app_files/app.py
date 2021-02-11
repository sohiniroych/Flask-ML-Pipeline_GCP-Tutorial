#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:32:03 2021

@author: sohini
"""


# Importing the libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

app=Flask(__name__)#create instance on flask
model=pickle.load(open('treemodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    output=round(prediction[0],2)
    return render_template('index.html', prediction_text='Profit should be ${}'.format(output))

@app.route('/predict_api', methods=["POST"])
def predict_api():
    data=request.get_json(force=True)
    prediction=model.predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)
    
    
if __name__=='__main__':
    app.run( debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)) )
