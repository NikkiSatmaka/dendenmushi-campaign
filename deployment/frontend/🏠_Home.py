#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image

TITLE = 'Den Den Mushi Campaign'
logo = Image.open('assets/dendenmushi.png')

st.set_page_config(
    page_title = f"Home - {TITLE}",
    page_icon='🐌',
    menu_items={
        'Get Help': 'https://github.com/NikkiSatmaka',
        'Report a bug': 'https://github.com/NikkiSatmaka',
        'About': '# Den Den Mushi Campaign'
    }
)

# credit for source image
img_source = "[deviantart](https://www.deviantart.com/drnachtschatten/art/Den-Den-Mushi-Transponder-Snail-355263223)"

# Title of the main page
col1, col2 = st.columns(2)
col1.image(logo, width=300)
col1.markdown('')
col1.markdown(f'image is rightfully owned by {img_source}', unsafe_allow_html=True)
col2.title(TITLE)

st.header('Introduction')

st.markdown(
    """
    Our new term deposit product is amazing.
    In this time of financial dread, this term deposit is a great product to invest in.

    Let's help our clients in this time of dire, by providing them with a better understanding of the term deposit product.

    The _**Den Den Mushi Campaign**_ is created to contact our clients and provide them this solution to their problems.

    However, we do know that you, as our highly valued telemarketers have a lot of clients to contact.
    We now provide you with a simple way to prioritize which clients that have a high chance of subscribing to our product.
    You can start by contacting these clients first.

    Simply go to the "Prediction" page and input the information regarding the client.
    Our state-of-the-art machine learning model will then predict whether your client have a high chance of subscribing to the term deposit product.

    So what are you waiting for?
    Go to the "Prediction" page and start predicting!
    Make those calls and get your clients to subscribe to our product!
    """
)

expander = st.expander('Show the informations you need to input to predict')
expander.markdown(
    """
    - Bank client data:
        1. Age
        2. Job
        3. Marital Status
        4. Education
        5. Credit Default Status
        6. Housing Loan Status
        7. Personal Loan Status

    - Related with the last contact of the current campaign:
        1. Communication Method
        2. Month of Last Contact
        3. Day of Week of Last Contact
        4. Duration of Last Contact (in seconds)

    - Other information:
        1. Contact Count during Campaign
        2. Days Passed since Last Contact
        3. Contact Count before Campaign
        4. Outcome of Previous Campaign

    - Social and economic indicators
        1. Employment Variation Rate - quarterly indicator
        2. Consumer Price Index - monthly indicator
        3. Consumer Confidence Index - monthly indicator
        4. Euribor 3 Month Rate - daily indicator
        5. Number of Employees - quarterly indicator
    """
)