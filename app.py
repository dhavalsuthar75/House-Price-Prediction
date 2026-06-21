import pandas as pd
import pickle as pk
import streamlit as st

model=pk.load(open(r'C:\Users\SUTHAR DHAVALKUMAR\Documents\House Price Prediction\House_prediction_model.pk1','rb'))

st.header('Banglore House Prices Predictor')
data=pd.read_csv(r'C:\Users\SUTHAR DHAVALKUMAR\Documents\House Price Prediction\cleaned_data.csv')

loc=st.selectbox('choose the location',data['location'].unique())
sqft=st.number_input('Enter Total Sqft')
beds=st.number_input('Enter the No of Bedrooms')
bath=st.number_input('Enter the No of Bathroom')
balc=st.number_input('Enter the No of Balconies')

if st.button("Predict Price"):

    input = pd.DataFrame(
        [[loc, sqft, bath, balc, beds]],
        columns=['location', 'total_sqft', 'bath', 'balcony', 'badroom']
    )

    output = model.predict(input)

    st.success(f"Price of House is ₹{output[0]*100000:,.0f}")