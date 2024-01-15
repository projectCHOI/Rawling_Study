import random
def generate_numbers_with_limited_duplicates(required_numbers, exclude_numbers):
    available_numbers = [num for num in range(0, 10) if num not in exclude_numbers]
    numbers = required_numbers.copy()
    
    while len(numbers) < 6:
        number = random.choice(available_numbers)
        if numbers.count(number) < 2:
            numbers.append(number)
    
    return numbers

# 사용자 입력 처리
items_input = input("시도할 조 이름은?(다중선택 가능, 띄어쓰기로 구분): ")
items = items_input.split() if items_input else [f'{i}조' for i in range(1, 6)]

required_numbers_input = input("반드시 포함해야 하는 번호를 입력하세요(띄어쓰기로 구분) : ")
required_numbers = [int(num) for num in required_numbers_input.split()] if required_numbers_input else []

exclude_numbers_input = input("반드시 제외해야 하는 번호를 입력하세요(띄어쓰기로 구분) : ")
exclude_numbers = [int(num) for num in exclude_numbers_input.split()] if exclude_numbers_input else []

# 복권 번호 생성 및 출력
for _ in range(5):
    random_item = random.choice(items)
    lotto_numbers = generate_numbers_with_duplicates(required_numbers, exclude_numbers)

    print("출력된 번호:", random_item, lotto_numbers)