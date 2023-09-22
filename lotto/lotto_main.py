import random

# 대한민국 방식의 6/45 로또 프로그램
# 로또 5장 자동 생성 후 당첨 번호 추출하여 비교

# 1~45 범위 로또번호 리스트 생성
numbers = list(range(1, 46))

while(True):
    # 사용자에게 게임 진행 여부 입력받기
    print("자동 로또 생성기입니다. 5개의 로또 용지가 자동 생성됩니다.")
    press = input("시작하려면 1을, 종료하려면 0을 입력하세요 : ")

    # 게임 시작
    if press == '1':
        # 로또 용지 5장 각각의 일치하는 숫자 카운트용 리스트
        count_list = [0, 0, 0, 0, 0]
        # 로또 용지 5장의 로또 번호를 담을 리스트(2차원 리스트)
        selected_numbers_list = []
        # 로또 용지 5장 번호 자동 추출
        for i in range(5):
            selected_numbers = random.sample(numbers, 6)
            selected_numbers.sort()
            selected_numbers_list.append(selected_numbers)
            print(chr(65+i) + " 자  동 ", end="")
            for n in selected_numbers:
                print("%3d" % n, end="  ")
            print()
        print()

        # 로또 당첨 번호 추첨 (메인 번호 6개 + 보너스 번호 1개 = 총 7개)
        selected_numbers = random.sample(numbers, 7)
        # 메인 번호 6개 추출
        main_numbers = selected_numbers[:6]
        main_numbers.sort()
        # 보너스 번호 1개 추출
        bonus_number = selected_numbers[6]

        # 당첨 번호 출력 및 로또 용지 번호와 대조
        print("당첨 번호 : ", end="")
        # 먼저 당첨 메인 번호 조회
        for m in main_numbers:
            # A~E 용지의 번호와 비교
            for i, selected_numbers in enumerate(selected_numbers_list):
                # 용지 번호와 당첨 번호가 일치하는 횟수(카운트) 계산
                if m in selected_numbers:
                    count_list[i] += 1
            # 당첨 메인 번호 출력
            print("%3d" % m, end=" ")
        # 보너스 번호 조회 및 출력
        print(" + " + "%3d\n" % bonus_number)
        # print(count_list) # 당첨 확인 디버깅용

        # 당첨 내역 출력
        print("당첨 내역 : ")
        # 상금 변수 초기화
        prize = 0
        # A~E 로또용지 비교
        for i in range(5):
            print(chr(65+i), end=" ")
            # 메인 번호 6개 일치 시 1등
            if count_list[i] == 6:
                prize += 1952160000
                print("1등 당첨")
            # 메인 번호 5개 일치 및 보너스 번호 일치 시 2등
            elif count_list[i] == 5 and bonus_number in selected_numbers_list[i]:
                prize += 54226666
                print("2등 당첨")
            # 메인 번호 5개 일치 시 3등
            elif count_list[i] == 5:
                prize += 1427017
                print("3등 당첨")
            # 메인 번호 4개 일치 시 4등
            elif count_list[i] == 4:
                prize += 50000
                print("4등 당첨")
            # 메인 번호 3개 일치 시 5등
            elif count_list[i] == 3:
                prize += 5000
                print("5등 당첨")
            # 2개 이하 일치 시 당첨 없음
            else:
                print("해당 없음")
        
        # 상금 수령 시 축하메시지 출력
        if prize > 0:
            print("\n축하합니다. 당첨된 상금은 " + str(prize) + "원입니다.\n")
        # 꽝
        else:
            print("\n아쉽지만 상금이 없습니다.\n")


        print("=" * 50 + "\n")
            
    # 프로그램 종료
    elif press == '0':
        quit()
    # 입력 오류 시 재입력 요구
    else:
        print("다시 입력하세요") 