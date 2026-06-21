import random

# 1. 1~45의 숫자 중 반드시 포함해야 하는 숫자를 입력
required_input = input("반드시 포함해야 하는 숫자(띄어쓰기로 구분) : ")
if required_input.strip() == '':
    required_numbers = []
else:
    try:
        required_numbers = [int(num) for num in required_input.strip().split()]
    except ValueError:
        print("숫자를 정확히 입력해주세요. 프로그램을 종료합니다.")
        exit()

# 2. 1~45의 숫자 중 반드시 제외해야 하는 숫자를 입력
exclude_input = input("반드시 제외해야 하는 숫자(띄어쓰기로 구분) : ")
if exclude_input.strip() == '':
    exclude_numbers = []
else:
    try:
        exclude_numbers = [int(num) for num in exclude_input.strip().split()]
    except ValueError:
        print("숫자를 정확히 입력해주세요. 프로그램을 종료합니다.")
        exit()

# 유효성 검사
# 포함할 숫자와 제외할 숫자가 겹치는지 확인
if set(required_numbers) & set(exclude_numbers):
    print("포함할 숫자와 제외할 숫자가 겹칩니다. 프로그램을 종료합니다.")
    exit()

# 숫자 범위 검사
if not all(1 <= num <= 45 for num in required_numbers + exclude_numbers):
    print("숫자는 1부터 45 사이여야 합니다. 프로그램을 종료합니다.")
    exit()

# 포함할 숫자 개수 확인
if len(required_numbers) > 6:
    print("포함할 숫자는 최대 6개까지 가능합니다. 프로그램을 종료합니다.")
    exit()

# 3. 반드시 포함되는 숫자와 반드시 제외한 숫자를 반영한 랜덤 6개의 숫자 생성을 5회 반복
for _ in range(5):
    # 사용 가능한 숫자 목록 생성
    available_numbers = set(range(1, 46)) - set(required_numbers) - set(exclude_numbers)
    available_numbers = sorted(available_numbers)  # 시퀀스로 변환

    # 필요한 숫자 개수 확인
    required_random_numbers = 6 - len(required_numbers)
    if len(available_numbers) < required_random_numbers:
        print("사용 가능한 숫자가 부족합니다. 프로그램을 종료합니다.")
        exit()

    # 랜덤 숫자 생성
    random_numbers = random.sample(available_numbers, required_random_numbers)

    # 최종 번호 조합
    final_numbers = required_numbers + random_numbers
    final_numbers.sort()

    # 4. 결과 출력
    print("출력된 번호:", final_numbers)
