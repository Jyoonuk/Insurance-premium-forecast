import streamlit as st
import sklearn
import numpy as np
import joblib


def run_ml():
    st.title('보험료 예측')

    print(sklearn.__version__)

    regressor = joblib.load('data/regressor1.pkl')
    scaler_X = joblib.load('data/scaler1_X.pkl')
    scaler_y = joblib.load('data/scaler_y1.pkl')


    age = st.number_input('나이 입력',0,120)


    radio_menu = ['남자','여자']
    gender = st.radio('선택하세요',radio_menu)
    if gender == '여자' :
        gender = 0
    else :
        gender = 1

    bmi = st.number_input('bmi 입력',0.0 ,)
    children = st.number_input('자녀 수 입력',0,)
    
    
    radio_menu1 = ['금연','흡연']
    smoker = st.radio('선택하세요',radio_menu1)
    if smoker == '금연' :
        smoker = 0
    else :
        smoker = 1 

    radio_menu2 = ['southwest','southeast','northwest','northeast']
    region = st.radio('선택하세요',radio_menu2)
    if region == 'southwest' :
        region = 0
    elif region == 'southeast' :
        region = 1 
    elif region == 'northwest' :
        region = 2 
    elif region == 'northeast' :
        region = 3 

    
    if st.button ('보험료 예측') :
        new_data = np.array([age,gender,bmi,children,smoker,region])

        new_data = new_data.reshape(1,6)
        new_data = scaler_X.transform(new_data)
        y_pred = regressor.predict(new_data)
        y_pred= scaler_y.inverse_transform(y_pred)
        y_pred = round(y_pred[0,0])
        st.write('이 사람의 보험료는 '+ str(y_pred) + '달러입니다.')
