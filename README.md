# Insurance-premium-forecast( 보험료에 대한 데이터 분석과 보험료 예측 ) 
+ 보험료에 대해서 데이터를 분석하고
+ 인공지능으로 학습을 시켜서
+ 보험료를 예측하는 웹 입니다. 
+ 사용한 언어 : python 
+ 데이터 출처 : https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction
+ 웹 주소 : http://15.164.229.97:8503/

# 데이터 컬럼 설명 
+ age : 나이 
+ sex : 성별 
+ children : 자녀 수
+ smoker : 흠연 유무 
+ region : 사는 지역 
+ charge : 보험료

분석 
+ 컬럼에 따라 데이터를 분석하고 시각화 했다 .

예측
+ MinMax Scaler를 이용해 데이터를 스케일링하고 train_test_split을 하고 머신러닝 linearregression을 통해 charge 컬름을 예측했다. 
