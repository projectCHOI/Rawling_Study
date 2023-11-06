#랜덤하게 1~45의 숫자 중 6개를 5회 반복 추출
import random
def numbers():
    return random.sample(range(1, 45), 6)

for _ in range(5):
    random_item = random
    happy = numbers()
    print("출력된 번호:", happy)