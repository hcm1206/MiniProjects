# 그래프 x축과 y축의 비율(스케일) 조정

import numpy as np
import matplotlib.pyplot as plt

# -5 ~ 5 범위의 입력값 x 시퀀스
x = np.arange(-5, 5, 0.01)
# 입력값 x에 대한 함수값 y
y = 2*x - 4

# 그래프 객체 생성
fig, ax = plt.subplots()
# 그래프 우측, 상단 경계선 제거
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 그래프 하단, 좌측 경계선을 각각 x=0, y=0 위치로 이동
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
# x에 대한 함수값 y 그래프 생성
ax.plot(x, y)
# 그래프의 x축과 y축 범위를 -5 ~ 5로 설정
plt.ylim(-5, 5)
plt.xlim(-5, 5)
# 그래프의 x축과 y축의 스케일을 동일하게 설정
plt.gca().set_aspect('equal', adjustable='box')
# 그래프 출력
plt.show()