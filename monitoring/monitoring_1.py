# 현재 순간의 메모리와 CPU 사용량 정보 출력

import psutil

# 실시간 메모리 사용 정보 로드
memory_usage = psutil.virtual_memory()
# 메모리 사용 전체 정보 출력
print(memory_usage)
# 메모리 사용 정보 중 메모리 사용량을 뽑아 소숫점 아래 2자리까지 출력
print(f"메모리 사용량: {memory_usage[2]:.2f}%")
# 0.001초 간격의 CPU 사용량을 로드하여 소숫점 아래 2자리까지 출력
print(f"CPU 사용량: {psutil.cpu_percent(interval=0.1):.2f}")