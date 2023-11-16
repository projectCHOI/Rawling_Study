import random

def numbers(required_numbers, exclude_numbers):
    all_numbers = list(range(1, 46))
    
    # 반드시 포함해야 하는 숫자 추가
    for num in required_numbers:
        if num not in all_numbers:
            all_numbers.append(num)
    
    # 제외할 숫자 제거
    for num in exclude_numbers:
        if num in all_numbers:
            all_numbers.remove(num)
    
    return random.sample(all_numbers, 6)

# 사용자로부터 반드시 포함해야 하는 숫자를 입력받아 리스트로 변환
required_input = input("반드시 포함해야 하는 숫자(띄어쓰기로 구분) : ")
required_list = [int(num) for num in required_input.split()]

# 사용자로부터 숫자를 입력받아 리스트로 변환
exclude_input = input("반드시 제외할 숫자(띄어쓰기로 구분) : ")
exclude_list = [int(num) for num in exclude_input.split()]

# 추첨 및 출력
for _ in range(5):
    happy = numbers(required_list, exclude_list)
    print("출력된 번호:", happy)
