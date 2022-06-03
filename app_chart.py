import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')


def run_chart():
    st.subheader('데이터 컬럼별 차트와 통계')
    df = pd.read_csv('data/insurance.csv',encoding ='ISO-8859-1')
    col_list = df.columns
    selected_list =st.selectbox('차트를 보고싶은 컬럼 선택',col_list)
    if selected_list == col_list[0]  :
        fig = plt.figure()
        plt.hist(data= df ,  x = 'age', rwidth=0.8, bins =10)
        plt.xlabel('나이')
        st.pyplot(fig)

    elif selected_list == col_list[1]  :
        fig = plt.figure()
        plt.hist(data= df ,  x = 'sex', rwidth=0.8, bins =10)
        plt.xlabel('점수')
        st.pyplot(fig)

    elif selected_list == col_list[2]  :
        fig = plt.figure()
        plt.hist(data= df ,  x = 'bmi', rwidth=0.8, bins =10)
        plt.xlabel('bmi')
        st.pyplot(fig)

    elif selected_list == col_list[3]  :
        fig = plt.figure()
        plt.hist(data= df ,  x = 'children', rwidth=0.8, bins =10)
        plt.xlabel('자녀 수')
        st.pyplot(fig)
    
    elif selected_list == col_list[4]  :
        fig = plt.figure()
        plt.hist(data= df ,  x = 'smoker', rwidth=0.8, bins =10)
        plt.xlabel('흡연 유무')
        st.pyplot(fig)

    elif selected_list == col_list[5]  :
        fig = plt.figure()
        plt.hist(data= df ,  x = 'region', rwidth=0.8, bins =10)
        plt.xlabel('지역')
        st.pyplot(fig)
    elif selected_list == col_list[6]  :
        fig = plt.figure()
        plt.hist(data= df ,  x = 'charges', rwidth=0.8, bins =10)
        plt.xlabel('보혐료')
        st.pyplot(fig)

    st.subheader('데이터 컬럼별 상관계수')
    df = df.replace({'sex':'female'},0)
    df = df.replace({'sex':'male'},1)
    df = df.replace({'smoker':'no'},0)
    df = df.replace({'smoker':'yes'},1)
    df = df.replace({'region':'southwest'},0)
    df = df.replace({'region':'southeast'},1)
    df = df.replace({'region':'northwest'},2)
    df = df.replace({'region':'northeast'},3)

    selected_list1 =st.multiselect('컬럼들 선택 (2개이상) [여성: 0 남성:1] [금연: 0 흡연: 1]  [southwest: 0 southeast: 1 northwest: 2 northeast: 3] 으로 변환',col_list)
    if len(selected_list1) >= 2  :

        fig1 = sb.pairplot(data = df[selected_list1])
        st.pyplot(fig1)

        st.text('선택하신 컬럼끼리의 상관계수 입니다.')
        st.dataframe(df[selected_list1].corr())


        fig2 = plt.figure()
        sb.heatmap(data = df[selected_list1].corr(), annot =True, fmt = '.2f', vmin =-1 , vmax = 1, cmap='coolwarm',linewidths=0.5)
        st.pyplot(fig2)
