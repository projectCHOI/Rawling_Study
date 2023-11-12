import random

def generate_numbers(required_numbers):
    all_numbers = list(set(list(range(1, 9)) + required_numbers))
    return random.sample(all_numbers, 6)

# 사용자로부터 items 값을 입력받아 리스트로 변환
items_input = input("시도할 조 이름은?(다중선택 가능, 띄어쓰기로 구분): ")
items = items_input.split() if items_input else ['1조', '2조', '3조', '4조', '5조']

# 사용자로부터 반드시 포함해야 하는 번호를 입력받아 리스트로 변환
required_numbers_input = input("반드시 포함해야 하는 번호는?(띄어쓰기로 구분): ")
required_numbers = [int(num) for num in required_numbers_input.split()]

for _ in range(5):
    random_item = random.choice(items)
    lotto_numbers = generate_numbers(required_numbers)

    print("출력된 번호:", random_item, lotto_numbers)
