#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import requests
from PIL import Image
from packages.options import job_options, marital_options, education_options
from packages.options import default_options, housing_options, loan_options
from packages.options import contact_options, month_options, day_of_week_options
from packages.options import poutcome_options

TITLE = "Prospective Client Prediction"

sub1 = "Bank client data"
sub2 = "Related with the last contact of the current campaign"
sub3 = "Other information"
sub4 = "Social and economic indicator"

msg_0_res = "It's highly likely that this client will not subscribe."
msg_0_act = "Look for another more potential clients!"
msg_0_add = "Here's a four-leaf clover for you"
msg_1_res = "There's a huge chance that this client will subscribe."
msg_1_act = "Call him immediately!"
msg_1_add = "Fingers crossed for you"
msg_goodluck = "Good Luck!"

img_crystal = Image.open('assets/crystal-ball.jpg')
img_res_0 = Image.open('assets/four-leaf-clover.jpg')
img_res_1 = Image.open('assets/fingers-crossed.jpg')


st.set_page_config(
    page_title = f"{TITLE}",
    page_icon='🐌',
    menu_items={
        'Get Help': 'https://github.com/NikkiSatmaka',
        'Report a bug': 'https://github.com/NikkiSatmaka',
        'About': '# Den Den Mushi Campaign'
    }
)

# URL = "http://127.0.0.1:5000/prediction/predict"  # for testing
URL = "https://bank-marketing-backend.herokuapp.com/prediction/predict"  # for deployment

col1, col2 = st.columns(2)
with col1:
    st.title(TITLE)
with col2:
    st.image(img_crystal, width=300)

st.subheader(sub1)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        'Age',
        min_value=17,
        max_value=100,
        value=40,
        help="Client's Age. Default is 40"
    )

    job = st.selectbox(
        'Job',
        job_options,
        index=0,
        help="Client's Job. Default is admin."
    )

    marital = st.selectbox(
        'Marital Status',
        marital_options,
        index=0,
        help="Client's Marital Status. Default is single."
    )

with col2:
    education = st.selectbox(
        'Education',
        education_options,
        index=6,
        help="Client's Education. Default is university degree."
    )

    default = st.radio(
        'Credit Default',
        default_options,
        index=0,
        help="Does the client have a credit in default? Default is no.",
        horizontal=True
    )

    housing = st.radio(
        'Housing Loan',
        housing_options,
        index=0,
        help="Does the client have a housing loan? Default is no.",
        horizontal=True
    )

    loan = st.radio(
        'Personal Loan',
        loan_options,
        index=0,
        help="Does the client have a personal loan? Default is no.",
        horizontal=True
    )

st.subheader(sub2)

col1, col2 = st.columns(2)

with col1:
    contact = st.selectbox(
        'Communication Method',
        contact_options,
        index=0,
        help="Method of Communication. Default is cellular."
    )

    month = st.selectbox(
        'Month of Last Contact',
        month_options,
        index=0,
        help="When was the last contact made with the client? Default is January."
    )

with col2:
    day_of_week = st.selectbox(
        'Day of Week of Last Contact',
        day_of_week_options,
        index=0,
        help="What day of the week was the last contact made with the client? Default is Monday."
    )

    duration = st.number_input(
        'Duration of Last Contact (in seconds)',
        min_value=0,
        max_value=10800,
        value=60,
        help="Duration of last contact in seconds. Default is 60."
    )

st.subheader(sub3)
col1, col2 = st.columns(2)

with col1:
    campaign = st.number_input(
        'Contact Count during Campaign',
        min_value=0,
        max_value=100,
        value=3,
        help="How many times has the client been contacted during this campaign. Default is 3."
    )

    pdays = st.number_input(
        'Days Passed since Last Contact',
        min_value=0,
        max_value=999,
        value=30,
        help="Days passed since the last contact. Default is 30. Input 999 if client has not been previously contacted."
    )

with col2:
    previous = st.number_input(
        'Contact Count before Campaign',
        min_value=0,
        max_value=100,
        help="How many times has the client been contacted before this campaign. Default is 3."
    )

    poutcome = st.selectbox(
        'Outcome of Previous Campaign',
        poutcome_options,
        index=0,
        help="What was the result of the previous campaign? Default is Failure."
    )

st.subheader(sub4)
col1, col2 = st.columns(2)
with col1:
    emp_var_rate = st.slider(
        'Employment Variation Rate - Quarterly Indicator',
        min_value=-10.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
        help="Employment variation rate. Default is 1.0."
    )

    cons_price_idx = st.slider(
        'Consumer Price Index - Monthly Indicator',
        min_value=0.0,
        max_value=999.0,
        value=90.0,
        step=0.1,
        help="Consumer Price Index. Default is 90.0."
    )

    cons_conf_idx = st.slider(
        'Consumer Confidence Index - Monthly Indicator',
        min_value=-100.0,
        max_value=999.0,
        value=-40.0,
        step=1.0,
        help="Consumer Confidence Index. Default is -40.0."
    )

with col2:
    euribor3m = st.slider(
        'Euribor 3 Month Rate - Daily Indicator',
        min_value=-10.0,
        max_value=50.0,
        value=4.5,
        step=1.0,
        help="Euribor 3 Month Rate. Default is 4.5."
    )

    nr_employed = st.slider(
        'Number of Employees - Quarterly Indicator',
        min_value=0.0,
        max_value=10000.0,
        value=5191.0,
        step=0.1,
        help="Number of Employees. Default is 5191"
    )

# store user input in a dictionary
data = {
    "age": age,
    "job": job,
    "marital": marital,
    "education": education.replace(' ', '.'),
    "default": default,
    "housing": housing,
    "loan": loan,
    "contact": contact,
    "month": month[:3],
    "day_of_week": day_of_week[:3],
    "duration": duration,
    "campaign": campaign,
    "pdays": pdays,
    "previous": previous,
    "poutcome": poutcome,
    "emp_var_rate": emp_var_rate,
    "cons_price_idx": cons_price_idx,
    "cons_conf_idx": cons_conf_idx,
    "euribor3m": euribor3m,
    "nr_employed": nr_employed
}

col1, col2, col3 = st.columns(3)
with col2:
    predict = st.button("Predict")

with st.spinner('Predicting...'):
    # inferencing
    if predict:
        # communicate
        r = requests.post(URL, json=data)
        res = r.json()

        if r.status_code == 200:
            result = res['result']['class_name']
            if result == 'Not Subscribe':
                st.warning(msg_0_res)
                st.subheader(msg_0_act)
                st.subheader(msg_goodluck)
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.write(msg_0_add)
                    st.image(img_res_0, width=300)
            else:
                st.success(msg_1_res)
                st.subheader(msg_1_act)
                st.subheader(msg_goodluck)
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.write(msg_1_add)
                    st.image(img_res_1, width=300)

        elif r.status_code == 400:
            st.title("There's an error in the input data!")
            st.write(res['message'])