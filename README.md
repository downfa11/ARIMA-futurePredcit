# ARIMA-futurePredcit
Prediction Future of Time series dataset with ARIMA

전통적인 시계열 예측 모델인 ARIMA를 통해서 미래의 데이터를 예측하는 프로젝트입니다.

bitthumb에서 BTC의 현재 종가를 가져와서 데이터 전처리를 합니다.

 - 5일 뒤의 종가를 예측하는 모델이기 때문에 [..., 5일전의 종가]의 시계열로 현재 종가를 예측하고자 함.
 
 - statsmodels.tsa.arima_moel이 statsmodels.tsa.arima.model로 바뀐거... 다들 알고 계셨나요... 지원 이제 안하는거 전 몰랐어요...ㅠ
