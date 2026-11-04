# MINI PROJECT 1 가위바위보 게임 만들기 (AX3기 이지혜)

print("="*30)
print("      가위 / 바위 / 보 게임      ")
print("="*30)

player_name = input("플레이어 이름을 입력하세요. : ")
# break를 빠져나와 완전히 게임을 초기화하지 않는 한, 이름을 다시 안 적어도 되도록 while 밖으로 빼버림

# ------------------------------------------------기초 작업
# while문 전에 미리 선언해야하는 + while 문 나오면 초기화 되어야 하는 변수 미리 작성
c_score = 0 # 컴퓨터의 스코어
h_score = 0 # 사람의 스코어
final_c_result = "미정" # 최종(3판2선승 한 세트 후) 컴 결과, 미리 선언 안하니 name 오류 나서 우선 "미정"으로 적어둠
final_h_result = "미정" # 최종(3판2선승 한 세트 후) 사람 플레이어 결과
final_relay_win_count = 1 # 세트 단위 연승기록. 이 변수가 변할때는 이미 이전에 승리를 한 상태여야 하므로 1로 시작
final_result_list=[] # 최종적으로 세트당 승패 결과 하나씩 넣어서 보여줄 때 쓸 결과 리스트

while True:
    import random # 난수 생성을 위한 random import
    c_sign = random.randint(1,3) # 1 = 가위, 2 = 바위, 3 = 보 이므로 컴퓨터는 1~3 까지의 난수 발생
    print("1. 가위 / 2. 바위 / 3. 보") # 번호 쓰기 전에 항상 나올 수 있도록 while 안에 추가하였음
    h_sign = input("번호를 선택하세요. : ")

    if not h_sign.isdecimal() or int(h_sign) not in range(1,4): # 입력값 검증
        print("**1~3사이의 숫자를 입력하세요!**") # 문자 등 입력하면 다시 처음으로 가서 입력받기
        continue

    h_sign = int(h_sign) # 사람이 낼 sign이 무엇인지 입력받고 문자가 아니라면 숫자로 변환

    # 결과 분석
    # 서로 다른 것 냈을 때
    if c_sign != h_sign:
        # 내가 이기는 경우 = 컴이 지는 경우
        if (c_sign == 1 and h_sign == 2) or (c_sign == 2 and h_sign == 3) or (c_sign == 3 and h_sign == 1) :
            # 이렇게 경우를 나열하는게 괜찮은지 모르겠음
            h_score += 1 # 사람이 이겼으니 human 스코어 +1
            game_result = "승리" # 게임 결과를 (사람기준) 승리로 저장

        else: # 내가 지는 경우 = 컴이 이기는 경우
            c_score += 1
            game_result = "패배" # 게임 결과 플레이어 기준 패배

    else: # 서로 같은 것 내서 비겼을 때, 이때는 스코어 누계안함
        game_result = "비김"

    # 결과 표시
    signs = ["가위","바위","보"] # 결과 표시할 때 숫자를 가위, 바위,보로 바꿔주려고 넣어줌
    print("-"*25) # 가독성을 위한 구분선 추가
    print("[게임결과]")
    print(f"{player_name} : {signs[h_sign-1]} vs 컴퓨터 : {signs[c_sign-1]}") # signs 리스트에서 인덱스로 가위바위보로 빼오기
    print(f"현재 스코어 - {player_name} {h_score} : 컴퓨터 {c_score} ")
    print("-"*25)

    if h_score == 2 or c_score == 2: # 만약 컴이든 사람이든 누군가가 2승을 한 상태라면? -> 3판 2선승
        if h_score == 2: # 3판2선승을 한 세트로 보고 세트별 승패 목록을 표시하기위해
            if final_h_result == "승리": # 사람이 2승인 상태일때
                final_relay_win_count += 1
            final_h_result = "승리" # 사람 승리
            final_c_result = "패배" # 컴 패배
        else: # 컴이 2승인 상태일 때 
            final_h_result = "패배" # 사람 패배
            final_c_result = "승리" # 컴 승리

        # 승패 결과 저장
        final_result_list_element = f"       {final_h_result} | {final_c_result}" # 승패 결과 한줄씩
        # 나중에 승패 결과 출력할때 '사람 vs 컴퓨터' 순으로 출력할 예정이므로 그 순서에 맞춰서 적어둠
        final_result_list.append(final_result_list_element) # 리스트 안에 쌓아두기

        # 3판2선승 종료 및 연승 안내
        print("3판 2선승 게임 종료!")
        if final_relay_win_count >=2: # 만약 연승 상태라면 메시지 보여주기
            print(f"**{final_relay_win_count}연승째입니다!**")

        # 새 게임 준비
        c_score = 0 # 스코어 초기화 -> 새 게임(3판2선승) 시작 대비
        h_score = 0 # 스코어 초기화 -> 새 게임(3판2선승) 시작 대비

        challenge = input("다시 도전 (yes/no) : ") # while 계속 진행여부 확인
        if challenge == "yes":
            print("="*25)
            continue # while 계속 돌기, 즉 게임 계속하기
        else: # 꼭 no 아니라도.. yes가 아닌 다른 내용 아무거나 넣으면 그냥 게임 종료되게
            # 게임 종료하며 현재까지 진행됐던 각 세트별 승패목록 출력
            print("=====게임을 종료합니다=====")
            print("---------승패목록---------")
            print(f"     {player_name} vs 컴퓨터 ")
            for result in final_result_list:
                print(result)
            break # while 빠져나와서 게임 종료하기

    else: # 만약 아직 2승이 나오지 않은 상태라면
        continue # 게임 계속 진행



# 코드를 효율적으로 깔끔하게 짜는 것이 어려움

# 입력값 검증 추가 필요