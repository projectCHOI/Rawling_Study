import FinanceDataReader as fdr
import datetime

date = datetime.datetime(2022, 1, 1)
code = '종목코드'  # 예시 종목 코드

if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close']

    # 차트 데이터 출력
    print(data)

    # 데이터프레임 출력
    print(df.sort_index(ascending=False))

    # 컬럼 설명
    column_description = '''
    - Open: 시가
    - High: 고가
    - Low: 저가
    - Close: 종가
    - Adj Close: 수정 종가
    - Volumn: 거래량
    '''
    print(column_description)
