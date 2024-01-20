# 주식 가격 백분률 계산.
data['Price_Change_Percentage'] = data['Stock_Price_Open'].pct_change() * 100

# 그림과 서브플롯(subplots) 세트 작성
fig, ax1 = plt.subplots(figsize=(15, 8))

# 주식 시가 데이터
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price Open', color='red')
ax1.plot(data['date'], data['Stock_Price_Open'], color='red', label='Stock Price Open')
ax1.tick_params(axis='y', labelcolor='red')

# 3%이상 변화를 별표 마커로 표시
significant_increase = data['Price_Change_Percentage'] >= 3
significant_decrease = data['Price_Change_Percentage'] <= -3
ax1.scatter(data['date'][significant_increase], data['Stock_Price_Open'][significant_increase], color='red', marker='*', s=100, label='>3% Increase')
ax1.scatter(data['date'][significant_decrease], data['Stock_Price_Open'][significant_decrease], color='blue', marker='*', s=100, label='>3% Decrease')

# 거래량을 표기하기 위한 y축을 생성
ax2 = ax1.twinx()
ax2.set_ylabel('Stock Volume', color='black')
ax2.bar(data['date'], data['Stock_Volume'], color='black', label='Stock Volume')
ax2.tick_params(axis='y', labelcolor='black')

# 범례를 추가
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# 표시
plt.title('Nexon Stock Price and Volume with Significant Changes Marked')
plt.show()
