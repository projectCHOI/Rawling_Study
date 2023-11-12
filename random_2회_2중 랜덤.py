#랜덤하게 정해진 텍스트와 1~9의 숫자 중 6개를 5회 반복 추출
def generate_numbers():
    return random.sample(range(1, 9), 6)

items = ['1조', '2조', '3조', '4조', '5조']

for _ in range(5):
    random_item = random.choice(items)
    lotto_numbers = generate_numbers()

    print("출력된 번호 :", random_item, lotto_numbers)
