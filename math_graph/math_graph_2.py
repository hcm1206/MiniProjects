# (0,0) 좌표를 중심으로 하는 그래프

import numpy as np
import matplotlib.pyplot as plt

# -5 ~ 5 범위의 입력값 x 시퀀스 설정
x = np.arange(-5, 5, 0.01)
# 1차 함수식 y 설정
y = 2*x - 4

# 그래프 객체 생성
fig, ax = plt.subplots()
# 그래프 우측 경계선과 상단 경계선 제거
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 그래프 하단 경계선과 좌측 경계선의 위치를 각각 x = 0, y = 0 위치로 이동
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
# 그래프 객체 상에서 x와 y에 대하여 그래프 생성
ax.plot(x, y)
# 그래프 출력
plt.show()