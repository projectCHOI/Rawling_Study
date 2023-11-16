import random

def generate_numbers(required_numbers, exclude_numbers):
    all_numbers = list(set(range(1, 9)).union(required_numbers) - set(exclude_numbers))
    return random.sample(all_numbers, 6)

# 사용자로부터 items 값을 입력받아 리스트로 변환
items_input = input("시도할 조 이름은?(다중선택 가능, 띄어쓰기로 구분): ")
items = items_input.split() if items_input else [f'{i}조' for i in range(1, 6)]

# 사용자로부터 반드시 포함해야 하는 번호를 입력받아 리스트로 변환
required_numbers_input = input("반드시 포함해야 하는 번호를 입력하세요(띄어쓰기로 구분) : ")
required_numbers = [int(num) for num in required_numbers_input.split()] if required_numbers_input else []

# 사용자로부터 반드시 제외해야 하는 번호를 입력받아 리스트로 변환
exclude_numbers_input = input("반드시 제외해야 하는 번호를 입력하세요(띄어쓰기로 구분) : ")
exclude_numbers = [int(num) for num in exclude_numbers_input.split()] if exclude_numbers_input else []

for _ in range(5):
    random_item = random.choice(items)
    lotto_numbers = generate_numbers(required_numbers, exclude_numbers)

    print("출력된 번호:", random_item, lotto_numbers)
