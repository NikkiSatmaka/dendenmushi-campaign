#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from pathlib import Path
import joblib
import pandas as pd

from packages.imputation_handling import prepare_imputation


app = Flask(__name__)

# initiate model & columns
LABEL = ["Not Subscribe", "Subscribe"]

# initiate list of columns to be imputed
COLUMNS_TO_IMPUTE = ["job", "marital", "education", "housing", "loan"]

# model location
model_dir = "models"
scaler_name = "imputer_scaler_pipe.pkl"
model_name = "final_rf_pipe.pkl"

# create path object
scaler_path = Path(model_dir, scaler_name)
model_path = Path(model_dir, model_name)

# load model
scaler = joblib.load(scaler_path)
model = joblib.load(model_path)

@app.route("/")
def welcome():
    return "<h3>This is the Backend for My Modeling Program</h3>"

@app.route("/prediction/predict", methods=["GET", "POST"])
def predict_campaign():
    if request.method == "POST":
        content = request.json
        try:
            # create dictionary to store input data
            new_data = {
                "age": content["age"],
                "job": content["job"].lower(),
                "marital": content["marital"].lower(),
                "education": content["education"].lower(),
                "default": content["default"].lower(),
                "housing": content["housing"].lower(),
                "loan": content["loan"].lower(),
                "contact": content["contact"].lower(),
                "month": content["month"].lower(),
                "day_of_week": content["day_of_week"].lower(),
                "duration": content["duration"],
                "campaign": content["campaign"],
                "pdays": content["pdays"],
                "previous": content["previous"],
                "poutcome": content["poutcome"].lower(),
                "emp_var_rate": content["emp_var_rate"],
                "cons_price_idx": content["cons_price_idx"],
                "cons_conf_idx": content["cons_conf_idx"],
                "euribor3m": content["euribor3m"],
                "nr_employed": content["nr_employed"]
            }

            # convert to dataframe
            new_data = pd.DataFrame([new_data])

            # prepare data for imputation
            prepared_data = prepare_imputation(new_data, COLUMNS_TO_IMPUTE)
            
            # scale data
            scaled_data = scaler.transform(prepared_data)

            # predict and store result
            res = model.predict(scaled_data)

            # convert result to dictionary
            result = {
                "class": str(res[0]),
                "class_name": LABEL[res[0]]
            }

            # jsonify result
            response = jsonify(
                success=True,
                result=result
            )

            # return response
            return response, 200

        except Exception as e:
            response = jsonify(
                success=False,
                message=str(e)
            )

            # return response
            return response, 400

    # return dari get method
    return "<p>Please use the POST method to predict <em>inference model</em></p>"

# app.run(debug=True)
