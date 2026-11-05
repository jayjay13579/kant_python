# # 클래스 정의(선언) : 붕어빵 틀 만들기_ 회원 정보에 대한 틀을 만들겠다!
# class User:  # 첫문자 대문자(파스칼 케이스)로 클래스 명 작성
#     def __init__ (self, name): # 생성자 : 인스턴스가 처음 생성될 때 자동 호출
#         # self : 클래스로 만들어진 인스턴스 자기 자신
#         self.name = name # 인스턴스self 내에 정의된 변수 name-> self.name에 인수 name을 넣어줌 -> 변수 초기화
#         # 왼쪽 : 회원 객체에 저장할 이름. 오른쪽 : 밖에서 전달받은 이름
#     def show(self): #이름 return / class안에서 def 사용시 함수가 아니라 메서드라고 함
#         return f"회원 이름 : {self.name}" # 인스턴스 내부 변수 name

# # 인스턴스 생성 : 붕어빵 만들기
# user_a = User("손흥민") # 내가 클래스에서 만든 인스턴스를 저장할 변수 # 여
# #self 변수는 자동 할당, 나머지 변수(name)만 넣기

# # 새 인스턴스 생성
# user_b = User("이강인")

# # User 클래스로 생성한 인스턴스 (메모리에 생성)

# # 클래스의 인스턴스 변수
# print(user_a.name)
# print(user_b.name)

# # 클래스의 메서드 접근
# print(user_a.show())
# print(user_b.show())



# print(type(user_a))
# print(user_a is user_b)
# print(id(user_a))
# print(id(user_b))

# # ==================

class Monitor:
    def display_info(self):
        # 인스턴스 변수
        self.resolution = "1920x1080"
        self.size = "27인치"
        print(f"모니터 정보\n해상도 : {self.resolution}\n크기 : {self.size}\n객체id : {id(self)}") #\n 줄바꿈

monitor = Monitor() # 인스턴스 생성(모니터 객체 생성) / parameter 없기 때문에 인수 없음
print(id(monitor)) # 모니터 인스턴스의 id 출력 

monitor.display_info() # 근데 클래스 안에 함수가 있으면 이렇게 하지 않아도 디스플레이 정보 나와야하는거 아냐?


# # ===========================

class SmartPhone:
    def __init__(self, model):
        self.model = model # 인스턴스 변수 = 속성(attribute)
        self.battery = 50 # 속성 기본값

    def charge(self, amount):
        self.battery += amount # init에서 정의한 self.battery를 다른 메서드에서 쓸 수 있음
        if self.battery > 100 :
            self.battery = 100 # 100이상이라는 개념이 없으니 우선 100으로 다시 정의해줌
            print(f"배터리 충전완료 : {self.battery}%")
        else:
            print(f"배터리 충전 중... : {self.battery}%")

phone_a = SmartPhone("아이폰")
print(phone_a.model)
phone_a.charge(30)
phone_a.charge(30)

phone_b = SmartPhone("갤럭시")
print(phone_b.model)
phone_a.charge(30)
phone_a.charge(30)

# 전체주석처리 ctrl + /

# 은행 계좌 클래스

class BankAccount:
    # 계좌 기본 정보 정의
    def __init__(self, owner, balance):
        self.owner = owner # 예금주
        self.balance = balance # 잔액

    def __str__(self): # str? 어떤때 쓰는거? 인스턴스를 사람이 읽기 좋은 문자열로 표현
        return f"예금주 : {self.owner}, 잔액 : {self.balance:,}" # 천단위 끊기 :,

    # def __repr__(self): # representation 위와 같은 기능
    #     return f"예금주 : {self.owner}, 잔액 : {self.balance:,}" # 천단위 끊기 :,

    #입금 처리 메서드
    def deposit(self, amount):
        self.balance += amount # 입금 처리
        print(f"{amount:,} 입금 완료 / 잔액 : {self.balance:,} 원")

    #출금 처리 메서드
    def withdrawl(self, amount):
        # psudo code : 로직을 미리 글로 표현해보기
        # 잔액 확인
        if amount > self.balance: # 잔액이 부족하면
            print(f"잔액이 부족합니다. 현재 잔액 : {self.balance:,} 원")
            return 0 # 이건 왜 하는거?? (아래 else안쓰고 이걸로 처리하는 이유는?)
        else:
            self.balance -= amount # 출금 
            print(f"{amount:,} 출금 완료 / 잔액 : {self.balance:,} 원")
            return self.balance # 출금 후 잔액 return 

account_a = BankAccount("이지혜", 100_000) # _로 세자리 끊어읽기
print(account_a)

account_a.deposit(500_000) # 500,000 입금 완료 / 잔액 : 600,000 원
account_a.withdrawl(500_000) # 500,000 출금 완료 / 잔액 : 100,000 원
account_a.withdrawl(500_000) # 잔액이 부족합니다. 현재 잔액 : 100,000 원
print(f"잔액: {account_a.withdrawl(100_000)}")  # 이미 print문 포함한 것을 다시 출력하면?
# 100,000 출금 완료 / 잔액 : 0 원
# 잔액: 0


account_c = BankAccount("홍길동", 200_000)
print([account_a, account_c])
