import random

def generate_numbers():
    return random.sample(range(1, 9), 6)

# 사용자로부터 items 값을 입력받아 리스트로 변환
items_input = input("시도할 조 이름은?(다중선택 가능, 띄어쓰기로 구분) : ")
items = items_input.split() if items_input else ['1조', '2조', '3조', '4조', '5조']

for _ in range(5):
    random_item = random.choice(items)
    lotto_numbers = generate_numbers()

    print("출력된 번호 :", random_item, lotto_numbers)
