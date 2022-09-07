#!/usr/bin/env python
# coding: utf-8

# In[1]:

# https://towardsdatascience.com/3-easy-ways-to-deploy-your-streamlit-web-app-online-7c88bb1024b1
import streamlit as st
st.title("Housing Prediction")
 
st.write("""
### Project description
We have trained the data to predict the n cheap house based on the following informations below""")
#  several models to predict the price of a house based on features such as the area of the house and the condition and quality of their different rooms.
 
# """)

import pandas as pd
data = pd.read_csv('housing-deployment-reg.csv')

# data = st.DataFrame(data)


  
# LotArea = st.number_input("Lot Area")
# TotalBsmtSF = st.number_input("Basement Square Feet")
BedroomAbvGr = st.number_input("Number of Bedrooms greater than or equal to ")
GarageCars = st.number_input("Car spaces in Garage greater than or equal to")
SalePrice = st.number_input("Sale price less than ")
# limit = st.number_input("find top n cheap houses")
limit = st.number_input(label="find top n cheap houses",step=1.,format="%f")

new_data=data[(data["BedroomAbvGr"]>= BedroomAbvGr ) &  ((data["GarageCars"]> GarageCars)) & (data["SalePrice"]< SalePrice)]

# new_house = pd.DataFrame({
#     'LotArea':[LotArea],
# #     'TotalBsmtSF':[TotalBsmtSF], 
# #     'BedroomAbvGr':[BedroomAbvGr], 
#     'GarageCars':[GarageCars]
# })

new_data=new_data.sort_values("SalePrice", ascending=True)
st.write(new_data.head(int(limit)))
 
# st.write("The price of the house is:", prediction)





