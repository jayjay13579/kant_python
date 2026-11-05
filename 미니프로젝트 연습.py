# MINI PROJECT 1


print("="*30)
print("      가위 / 바위 / 보 게임      ")
print("="*30)

player_name = input("플레이어 이름을 입력하세요. : ")
# break를 빠져나와 완전히 게임을 초기화하지 않는 한, 이름을 다시 안 적어도 되도록 while 밖으로 빼버림

# ------------------------------------------------기초 작업
# while문 전에 미리 선언해야하는 + while 문 나오면 초기화 되어야 하는 변수 미리 작성
c_score = 0 # 컴퓨터의 스코어
h_score = 0 # 사람의 스코어
result_list = [] # 나중에 승패 결과 하나씩 넣어서 한번에 보여줄 때 쓸 결과 리스트
relay_win_count = 1 # 연승기록. 이 변수가 나타날때는 이미 이전에 승리를 한 상태여야 하므로 1로 시작
game_result = "미정" # 뒤에 연승 체크 때문에 변수를 먼저 선언...안적으면 error가 발생해서.. while 안에 넣으면 연승 확인 못함

while True:
    import random # 난수 생성을 위한 random import
    c_sign = random.randint(1,3) # 1 = 가위, 2 = 바위, 3 = 보 이므로 컴퓨터는 1~3 까지의 난수 발생
    print("1. 가위 / 2. 바위 / 3. 보") # 번호 쓰기 전에 항상 나올 수 있도록 while 안에 추가하였음
    h_sign = int(input("번호를 선택하세요. : ")) # 사람이 낼 sign이 무엇인지 입력받고 숫자로 변환

    # 결과 분석
    # 서로 다른 것 냈을 때
    if c_sign != h_sign:
        # 내가 이기는 경우 = 컴이 지는 경우
        if (c_sign == 1 and h_sign == 2) or (c_sign == 2 and h_sign == 3) or (c_sign == 3 and h_sign == 1) :
            if game_result == "승리": # 직전에 저장되어있던 game_result가 "승리"일때 -> 즉 이번에 연승일때
                relay_win_count += 1
            h_score += 1 # 사람 스코어 +1
            game_result = "승리" # 게임 결과를 사람기준으로 승리로 저장
            counter_result = "패배" # 컴 결과는 패배로 저장

        else: # 내가 지는 경우 = 컴이 이기는 경우
            c_score += 1
            game_result = "패배"
            counter_result = "승리"

    else: # 서로 같은 것 내서 비겼을 때, 이때는 스코어 누계안함
        game_result = "비김"
        counter_result = "비김"

    # 한 턴의 결과 분석 후 나중에 승패 목록으로 보여줄 리스트에 해당 데이터를 넣어둠
    result_list_element = f"       {game_result} | {counter_result}"
    result_list.append(result_list_element)

    # 결과 표시
    signs = ["가위","바위","보"] # 결과 표시할 때 숫자를 가위, 바위,보로 바꿔주려고 넣어줌
    print("-------------------------") # 가독성을 위한 구분선 추가
    print("[게임결과]")
    print(f"{player_name} : {signs[h_sign-1]} vs 컴퓨터 : {signs[c_sign-1]}") # signs 리스트에서 인덱스로 가위바위보로 빼오기
    print(f"현재 스코어 - {player_name} {h_score} : 컴퓨터 {c_score} ")
    print("-------------------------")


    if relay_win_count >=2: # 만약 연승 상태라면 메시지 보여주기
        print(f"{relay_win_count}연승째입니다!")

    if h_score == 2 or c_score == 2: # 만약 누군가가 2승을 한 상태라면
        print("3판 2선승 게임 종료!")
        print("---------승패목록---------")
        print(f"     {player_name} vs 컴퓨터 ")
        for result in result_list:
            print(result)
        
        c_score = 0 # 스코어 초기화 -> 새 게임(3판2선승) 시작 대비
        h_score = 0 # 스코어 초기화 -> 새 게임(3판2선승) 시작 대비

        challenge = input("다시 도전 (yes/no) : ") # while 계속 진행여부 확인
        if challenge == "yes":
            print("-------------------------") # 구분선(그냥 결과 구분해서 보려고 넣음)
            continue # while 계속 돌기, 즉 게임 계속하기
        else:
            break # while 빠져나오기

    else: # 만약 아직 2승이 나오지 않은 상태라면
        continue # 게임 계속 진행

