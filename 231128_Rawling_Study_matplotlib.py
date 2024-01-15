import matplotlib.pyplot as plt

# 날짜를 datetime 객체로 변환
df['날짜'] = pd.to_datetime(df['날짜'])

# 시계열 주가 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(df['날짜'], df['종가'], marker='o')
plt.title('Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 결과 그림 출력
plt.show()
