import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv('path_to_your_file.csv')  # 'path_to_your_file.csv'를 파일의 경로로 대체하세요

# 'Stock_Price_Open'과 'Stock_Volume'의 쉼표 제거 및 정수형으로 변환
df['Stock_Price_Open'] = df['Stock_Price_Open'].str.replace(',', '').astype(int)
df['Stock_Volume'] = df['Stock_Volume'].str.replace(',', '').astype(int)

# 'date'를 datetime 객체로 변환
df['date'] = pd.to_datetime(df['date'])

# 시각화
plt.figure(figsize=(10, 6))

# 꺽은선 그래프 (Stock_Price_Open)
plt.plot(df['date'], df['Stock_Price_Open'], label='Stock Price Open', color='blue')

# 막대 그래프 (Stock_Volume)
plt.bar(df['date'], df['Stock_Volume'], label='Stock Volume', color='orange', alpha=0.5)

# 레이블, 제목, 범례 추가
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Nexon Stock Price and Volume')
plt.legend()

# 그래프 표시
plt.show()
