import streamlit as st
import numpy as np
from app_ml import run_ml
from app_eda import run_eda
from app_home import run_home
from app_chart import run_chart
from streamlit_option_menu import option_menu



def main () :


    menu = ['홈 화면','데이터 분석','데이터 차트','보험료 예측']
    with st.sidebar:
        st.image('data/다운로드.jpg')
        choice = option_menu('MENU',menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] : 
        run_eda()   
    elif choice == menu[2] :
        run_chart()
    elif choice == menu[3] :
        run_ml()
   

if __name__ == '__main__' : 
    main()
