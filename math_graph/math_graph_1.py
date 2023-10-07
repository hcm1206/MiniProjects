# matplotlib을 활용한 기본적인 그래프

import numpy as np
import matplotlib.pyplot as plt

# x축 입력값 범위 시퀀스
x = np.arange(-5, 5, 0.01)
# 임의의 1차 함수식 y
y = 2*x - 4

# 그래프 객체 생성하여 x와 y에 대하여 그래프 생성
fig, ax = plt.subplots()
ax.plot(x, y)
# 그래프 출력
plt.show()