import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 데이터 생성: 하나의 점 (예: (1, 2, 3))
x = [1]
y = [2]
z = [0]

# 3D 그래프 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# X, Y, Z 축에 데이터 플로팅 (하나의 점)
ax.scatter(x, y, z)

# 라벨 설정
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# 축의 한계를 설정
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([0, 5])

# 그래프 표시
plt.show()
