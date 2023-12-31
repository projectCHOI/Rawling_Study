# 웹사이트의 창을 내렸을 때 생기는 데이터 크롤링

import requests
#import json #json을 추가 한다면 사용
main_list = []

    #매개 변수를 바꾸어 정의 아래의 코드 값은 전부 0으로 만들어줌
magazineOffset = 0
contestOffset = 0
exhibitOffset = 0
galleryOffset = 0

    #아래 for문을 반복하라 (반복 횟수)
for i in range(5):
    #변경 전
    #response = requests.get('https://www.jungle.co.kr/recent.json?magazineOffset=23&contestOffset=40&exhibitOffset=3&galleryOffset=0')
    #변경 후
    response = requests.get(f'https://www.jungle.co.kr/recent.json?magazineOffset={magazineOffset}&contestOffset={contestOffset}&exhibitOffset={exhibitOffset}&galleryOffset={galleryOffset}')

    for item in response.json()['moreList']:
        
        main_list.append(
            {
                'title' : item['title'],
                'targetCode' : item['targetCode']

            }
        )

        #매개 변수를 바꾸어 정의 아래의 코드 값을 변하게 함.
        magazineOffset = response_json['magazineOffset']
        contestOffset = response_json['contestOffset']
        exhibitOffset = response_json['exhibitOffset']
        galleryOffset = response_json['galleryOffset']

#일반 출력
print(main_list)

#main_list를 json_file로 변환
# with open('main_list.ison', 'w') as json_file:
#     json.dump(main_list, json_file, ensure_ascii=False) 
