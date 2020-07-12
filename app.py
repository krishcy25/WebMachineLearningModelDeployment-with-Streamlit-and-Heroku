#!/usr/bin/env python
# coding: utf-8

# In[14]:


from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('hp_pyc_deployment_07122020')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    from PIL import Image
    image = Image.open('logo1.PNG')
    image_hospital = Image.open('house.jpeg')

    st.image(image,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict the house loan using PyCaret Linear Regression by "Krishna Yarlagadda"')
    st.sidebar.success('https://www.pycaret.org')
    
    st.sidebar.image(image_hospital)

    st.title("House Prices Prediction Application")

    if add_selectbox == 'Online':

        LotArea = st.number_input('LotArea', min_value=1, max_value=100000, value=50)
        GarageArea = st.number_input('GarageArea', min_value=1, max_value=100000, value=50)
        FirstFloorSF = st.number_input('FirstFloorSF', min_value=1, max_value=100000, value=50)
        SecondFloorSF = st.number_input('SecondFloorSF', min_value=1, max_value=100000, value=50)
        
        PavedDrive = st.selectbox('PavedDrive', ['Y','N','P'])
        SaleCondition = st.selectbox('SaleCondition', ['Normal','Partial','Abnormal','Family','Alloca','AdjLand'])
      
        
        
        
        FullBath=st.selectbox('FullBath', [0,1,2,3])
        HalfBath = st.selectbox('HalfBath', [0,1,2,3])
        


        output=""

        input_dict = {'LotArea' : LotArea, 'GarageArea' : GarageArea, 'FirstFloorSF' : FirstFloorSF,
                      'SecondFloorSF' : SecondFloorSF
                      ,'PavedDrive' : PavedDrive, 'SaleCondition' : SaleCondition, 'FullBath' : FullBath,
                      'HalfBath': HalfBath}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)

        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()


# In[ ]:




