# 숫자 야구 게임 최종본

import random

print("숫자 야구 게임입니다.")

# 숫자 야구 게임 숫자 개수 설정
while True:
    try:
        game_number = int(input("맞출 숫자 개수를 입력하세요(최소 2개, 최대 4개) : "))
    except:
        print("경고 : 유효하지 않은 입력입니다.\n")
        continue
    if game_number > 1 and game_number < 5:
        break
    else:
        print("경고 : 유효한 숫자 개수를 입력해주세요.(최소 2, 최대 4)\n")

# 0~9 범위 숫자 리스트 생성
numbers = list(range(0, 10))

# 게임 종료 시까지 반복
while True:
    # 정답 숫자 추첨
    answer_numbers = random.sample(numbers, game_number)
    # print("맞춰야 할 숫자 :", answer_numbers) # 디버깅용

    # 라운드 변수 초기화
    round = 1

    # 라운드 반복
    while True:
        # 스트라이크, 볼 카운트 초기화
        strike = 0
        ball = 0

        print("\n[" + str(round) + "라운드]\n")
        
        # 사용자 입력
        try:
            user_input = input("0-9 사이의 숫자 {}개 입력(중복 안됨). ex)3 6 9 : ".format(game_number))
            user_numbers = [int(num) for num in user_input.split()]
        except:
            print("경고 : 유효하지 않은 입력입니다.")
            continue
        if len(user_numbers) != game_number:
            print("경고 : 입력하신 숫자 개수가 올바르지 않습니다. {}개의 숫자를 입력하세요.".format(game_number))
            continue
        
        if len(set(user_numbers)) != game_number:
            print("경고 : 중복된 숫자를 입력하지 마세요.")
            continue
        
        error_num = 0
        for n in user_numbers:
            if n < 0 or n > 9:
                error_num += 1
        if error_num > 0:
            print("경고 : 0-9 사이의 숫자만 입력 가능합니다.")
            continue
        
        # 스트라이크 판정
        for i, n in enumerate(user_numbers):
            if answer_numbers[i] == n:
                strike += 1
        
        # 볼 판정
        for i, n in enumerate(user_numbers):
            if answer_numbers[i] != n and n in answer_numbers:
                ball += 1
        
        # 스트라이크 볼 출력
        print(strike, "strike", ball, "ball\n")

        # 게임 종료 시 반복 종료
        if strike == game_number:
            print("[게임 종료]", round, "라운드만에 맞추셨습니다.")
            break
    
        # 게임 종료가 아니면 라운드 횟수 1 추가하여 반복
        round += 1
    
    # 게임 재시작 여부 결정
    while True:
        try:
            replay = int(input("다시 하시려면 1을, 종료하려면 0을 입력하세요 : "))
        except:
            print("경고 : 유효하지 않은 입력입니다.\n")
            continue
        if replay == 1:
            print("\n\n")
            break
        elif replay == 0:
            quit()
        else:
            print("경고 : 유효하지 않은 입력입니다.\n")
            continue