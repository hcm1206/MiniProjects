# 큐를 이용하여 과거 데이터를 제거하는 실시간 메모리 및 CPU 사용량 그래프

import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from collections import deque

# 0부터 카운트하는 count 객체 생성
index = count()

# x축(시간) 저장할 20 길이 큐 생성
x = deque(maxlen=20)
# y1축(메모리 사용량) 저장할 20 길이 큐 생성
y1 = deque(maxlen=20)
# y2축(CPU 사용량) 저장할 20 길이 큐 생성
y2 = deque(maxlen=20)

# 메모리 사용량, CPU 사용량 추출하는 함수
def check():
    # 메모리 사용 정보 로드
    memory_usage = psutil.virtual_memory()
    # 메모리 사용량 추출
    memory_used_percent = memory_usage[2]
    # 0.0005초 간격의 CPU 사용량 추출
    cpu_used_percent = psutil.cpu_percent(interval=0.5)
    # 메모리 사용량, CPU 사용량 반환
    return memory_used_percent, cpu_used_percent

# 실시간으로 갱신되는 그래프 생성 함수
def animate(_):
    # 메모리 및 CPU 사용량 추출
    memory, cpu = check()

    # 현재 카운트 된 숫자를 큐 x에 추가
    x.append(next(index))
    # 현재 메모리 사용량을 큐 y1에 추가
    y1.append(memory)
    # 현재 CPU 사용량을 큐 y2에 추가
    y2.append(cpu)

    # 그래프 좌표축 제거
    plt.cla()
    # x(시간축)에 대한 y1(메모리 사용량)을 그래프에 표시
    plt.plot(x, y1, label='memory')
    # x(시간축)에 대한 y2(CPU 사용량)을 그래프에 표시
    plt.plot(x, y2, label='CPU')
    # 적당한 위치에 범례 표시
    plt.legend(loc='best')
    # 그래프에 격자 추가
    plt.grid(True)
    # y축 범위를 0~120으로 설정
    plt.ylim(0, 120)
    # y축의 라벨 설정
    plt.ylabel('usage %')

# 1초 간격으로 그래프 갱신
realtime_plot = FuncAnimation(plt.gcf(), animate, interval=1000)
# 그래프 출력
plt.show()