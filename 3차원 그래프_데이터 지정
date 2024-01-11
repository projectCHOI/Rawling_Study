import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 데이터 생성
x = np.linspace(0, 5, 100)
y = np.linspace(0, 3, 100)
z = np.linspace(0, 7, 100)

# 3D 그래프 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# X, Y, Z 축에 데이터 플로팅
ax.scatter(x, y, z)

# 라벨 설정
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# 축 범위 설정
ax.set_xlim([0, 5])
ax.set_ylim([0, 3])
ax.set_zlim([0, 7])

# 그래프 표시
plt.show()
