# 만들어진 데이터 프레임에서 성향 을 가져오고 원 그래프로 만들어라.
import matplotlib.pyplot as plt

# '성향' 열의 값으로 원 그래프 생성
plt.figure(figsize=(4, 4)) #크기
plt.pie(attitude_counts, labels=attitude_counts.index, autopct=lambda p: f'{p:.1f}%', #비율 표시 스타일
        startangle=140, colors=colors, textprops={'weight': 'bold'})#색상
colors = ['lightyellow' if x == 0 else 'orange' if x == 2 else 'yellow' for x in attitude_counts.index] #색상2
plt.title('Kakao-game') #제목
plt.show()
