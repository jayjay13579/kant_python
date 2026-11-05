# 쇼핑카트 클래스 선언
class ShoppingCart:
    # 카트 생성
    def __init__(self,name):
        self.name = name
        self.shopping_list = [] # class 안에서 생성
        print(f"{self.name}님의 장바구니가 비어있습니다.") # self.name
    
    # 메서드1 - 장바구니 담기
    def in_cart(self, item):
        self.shopping_list.append(item)
        print(f"{item.name}을/를 장바구니에 담았습니다.") # item만 쓰면 객체가 나옴

    # 메서드2 - 장바구니에서 빼기
    def out_cart(self, item):
        self.shopping_list.remove(item)
        print(f"{item.name}을/를 장바구니에서 삭제했습니다.")

    # 메서드 3 - 상품목록 조회
    def show(self):
        return self.shopping_list


# 상품 클래스 생성
class Items:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}원"

# 상품 3개 생성
item_1 = Items("apple", 1_000)
item_2 = Items("banana", 2_000)
item_3 = Items("grape", 3_000)

# 쇼핑 카트 생성
cart = ShoppingCart("이지혜")
cart

# 상품 1개 장바구니 담기
cart.in_cart(item_1)

# 상품 1개 장바구니 담기
cart.in_cart(item_2)

# 상품 1개 장바구니 담기
cart.in_cart(item_3)

# 상품 1개 장바구니에서 빼기
cart.out_cart(item_2)

# 장바구니에 담긴 상품 목록 조회
print(cart.show()) # repr 써서 할수도 있음

# for item in cart.show():
#     print(item.name, item.price)  # 왜 print(cart.show())는 안돼??

# cart = ShoppingCart("이지혜")
# for item in cart.show():
#     print(item.name, item.price) # 모르고 다시 실행해버리면..? 비어버림