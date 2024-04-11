import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

# Set page configuration
st.set_page_config(layout="wide")

st.title("Carbon Footprint Prediction")
st.markdown("A machine learning model to predict carbon footprint usage")


# First Section
st.subheader("Personal Features")
expander1 = st.expander("Click to expand")
with expander1:
    col1, col2 = st.columns(2)
    with col1:
        body = st.radio('Body Type',('obese', 'overweight', 'underweight', 'normal') )
        gender = st.radio("Gender",("male","female"))
    with col2:
        shower = st.radio("Shower Frequency",('less frequently', 'twice a day', 'more frequently', 'daily'))
        new_clothes = st.slider("How many new clothes per Month", 0,100, step=1)
st.text('')

# Second Section
st.subheader("Travel")
expander = st.expander("Click to expand")
with expander:
    col3, col4 = st.columns(2)
    with col3:
        body = st.radio("Transportation", ('walk/bicycle', 'private', 'public' ))
        gender = st.radio("Vehicle Type", ('PMM', 'diesel', 'electric', 'petrol', 'lpg', 'hybrid', 'publicTransport'))
    with col4:
        shower = st.radio("Air Travel", ('rarely', 'very frequently', 'frequently', 'never'))
        social = st.slider("Distance Travelled Per Month ",1,10000,step=150)
st.text('')

st.subheader("Food Habits")
expander1 = st.expander("Click to expand")
with expander1:
    col7, col8 = st.columns(2)
    with col7:
        body = st.slider("Avg. Monthly Grocery bill", 1,600, step=10)
        gender = st.radio("Diet", ('vegetarian', 'omnivore', 'vegan', 'pescatarian'))
        waste_size = st.radio('Waste bag size',('extra large', 'medium', 'large', 'small'))
        waste_count = st.slider('Waste bag count Per Week', 1,8, step =1)
        social = st.radio("Social Activity", ('often', 'sometimes', 'never'))
    with col8:
        grill = st.radio("Cooking with Grill", ('yes', 'no'))
        oven = st.radio("Cooking with Oven", ('yes', 'no'))
        stove = st.radio("Cooking with Stove", ('yes', 'no'))
        microwave = st.radio("Cooking with Microwave", ('yes', 'no'))
        airfryer = st.radio("Cooking with Airfryer", ('yes', 'no'))
        social = st.slider("Distance Travelled Per Month ",0,10000,step=250)
st.text('')

st.subheader("Home and recycle")
container = st.expander('Click to expand')
with container:
    col5, col6 = st.columns(2)
    with col5:
        tv_pc = st.slider("TV/PC watch time Per Day", 0,24, step=1)
        internet = st.slider("Time spent on Internet Per Day", 0,24, step=1)
        heating = st.radio("Heating Source", ('natural gas', 'wood', 'coal', 'electricity'))
        energy_eff = st.radio('Energy Efficiency',('No', 'Sometimes', 'Yes'))
    with col6:
        paper = st.radio("Recycling Paper", ('yes', 'no'))
        plastic = st.radio("Recycling Plastic", ('yes', 'no'))
        glass = st.radio("Recycling Glass", ('yes', 'no'))
        metal = st.radio("Recycling Metal", ('yes', 'no'))

st.text('')
if st.button("Estimate Carbin Footprint"):
    result = predict()
    st.text(result[0])
st.text('')
