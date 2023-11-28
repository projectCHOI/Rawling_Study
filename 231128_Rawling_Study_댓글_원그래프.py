# 만들어진 데이터 프레임에서 성향 을 가져오고 원 그래프로 만들어라.

import matplotlib.pyplot as plt

# '성향' 열의 값으로 원 그래프 생성
attitude_counts = df['성향'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(attitude_counts, labels=attitude_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('댓글 성향 분포')
plt.show()
