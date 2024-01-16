import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

# 가상의 데이터 생성을 위한 날짜 범위 설정
dates = pd.date_range(start="2020-01-01", end="2020-12-31", freq='D')

# 가상의 데이터 생성 (데이터A와 데이터B)
np.random.seed(0)
dataA = pd.DataFrame({
    'date': dates,
    'volume': np.random.randint(100, 1000000, len(dates))
})
dataB = pd.DataFrame({
    'date': dates,
    'volume': np.random.randint(100, 1000000, len(dates))
})

# 날짜 데이터를 pandas의 datetime 형식으로 변환
dataA['date'] = pd.to_datetime(dataA['date'])
dataB['date'] = pd.to_datetime(dataB['date'])

# 선형 회귀 모델을 사용하여 추세선 계산
modelA = LinearRegression()
modelB = LinearRegression()

# 날짜 데이터를 수치형으로 변환
dataA['date_num'] = dataA['date'].map(mdates.date2num)
dataB['date_num'] = dataB['date'].map(mdates.date2num)

# 선형 회귀 모델 학습
modelA.fit(dataA[['date_num']], dataA['volume'])
modelB.fit(dataB[['date_num']], dataB['volume'])

# 추세선을 위한 예측값 계산
dataA['trend'] = modelA.predict(dataA[['date_num']])
dataB['trend'] = modelB.predict(dataB[['date_num']])

# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.scatter(dataA['date'], dataA['volume'], color='blue', s=10, alpha=0.5)
plt.scatter(dataB['date'], dataB['volume'], color='green', s=10, alpha=0.5)
plt.plot(dataA['date'], dataA['trend'], color='blue', linewidth
