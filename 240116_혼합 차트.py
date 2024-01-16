#!pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# 데이터 파일 불러오기
dataA = pd.read_csv('경로/데이터A.csv')
dataB = pd.read_csv('경로/데이터B.csv')

# 날짜 형식을 datetime으로 변환 (필요한 경우)
dataA['날짜'] = pd.to_datetime(dataA['날짜'])
dataB['날짜'] = pd.to_datetime(dataB['날짜'])

# 데이터 정렬
dataA = dataA.sort_values(by='날짜')
dataB = dataB.sort_values(by='날짜')

# 그래프 그리기
plt.figure(figsize=(10, 6))

plt.plot(dataA['날짜'], dataA['거래량'], color='blue', label='데이터A')
plt.plot(dataB['날짜'], dataB['거래량'], color='green', label='데이터B')

# Y축 범위 설정
plt.ylim(100, 1000000)

# 레이블 및 제목 추가
plt.xlabel('날짜')
plt.ylabel('거래량')
plt.title('데이터A와 데이터B의 거래량 추세')
plt.legend()

# 그래프 표시
plt.show()