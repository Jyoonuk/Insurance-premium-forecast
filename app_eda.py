from scipy.misc import ascent
import streamlit as st
import sklearn
import numpy as np
import joblib
import pandas as pd


def run_eda():
    df = pd.read_csv('data/insurance.csv',encoding ='ISO-8859-1')
    st.subheader('데이터 분석')
    if st.checkbox('데이터 전체 보기') :
       st.dataframe(df)
    radio_menu = ['데이터프레임','통계치']
    selected = st.radio('둘중 보고싶은 데이터를 선택하세요',radio_menu)
    df1 = df.replace({'sex':'female'},0)
    df1 = df1.replace({'sex':'male'},1)
    df1 = df1.replace({'smoker':'no'},0)
    df1 = df1.replace({'smoker':'yes'},1)
    df1 = df1.replace({'region':'southwest'},0)
    df1 = df1.replace({'region':'southeast'},1)
    df1 = df1.replace({'region':'northwest'},2)
    df1 = df1.replace({'region':'northeast'},3)

    if selected == radio_menu[0] :
        st.dataframe(df)
    elif selected == radio_menu[1] : 
        st.dataframe(df1.describe())

    col_list = df.columns[0],df.columns[2],df.columns[3],df.columns[6]

    selected_col = st.selectbox('최대 최소 원하는 컬럼 선택',col_list)

    df_max = df.loc[df[selected_col] == df[selected_col].max() , ]
    df_min = df.loc[df[selected_col] == df[selected_col].min() , ]

    st.subheader("{}컬럼의 최대값에 해당하는 데이터 .".format(selected_col))
    st.dataframe(df_max)
    st.subheader("{}컬럼의 최소값에 해당하는 데이터 .".format(selected_col))
    st.dataframe(df_min)

    st.subheader('나이별 보험료 평균금액')
    st.dataframe(df1.groupby('age')['charges'].mean().to_frame())

    st.subheader('나이별 흡연 유무 평균치')
    st.dataframe(df1.groupby('age')['smoker'].mean().to_frame())

    st.subheader('나이별 bmi 평균치')
    st.dataframe(df1.groupby('age')['bmi'].mean().to_frame())

    st.subheader('지역별 보혐료 평균금액')
    st.text('southwest : 0 , southeast : 1 , northwest : 2 , northeast : 3')
    st.dataframe(df1.groupby('region')['charges'].mean().to_frame())
 
    st.subheader('지역별 흡연 유무')
    st.dataframe(df1.groupby('region')['smoker'].mean().to_frame())

    st.subheader('지역별 bmi 평균치')
    st.dataframe(df1.groupby('region')['smoker'].mean().to_frame())

    
 
     