# pip install streamlit 라이브러리 설치

import streamlit as st
import pandas as pd

# 제목 설정
st.title('YouTube Comment Viewer')

# 파일 경로 설정
file_path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\Rawling_Study\Rawling_Study\240317_streamlit\YouTube_comment_61220.csv'

# CSV 파일 불러오기
data = pd.read_csv(file_path)

# 사이드바 옵션
# 'labels' 필터링 선택
name_to_filter = st.sidebar.selectbox(
    'Select a name to filter:',
    ['All'] + list(pd.unique(data['name']))
)

# '댓글'에 대한 키워드 검색
keyword = st.sidebar.text_input('Enter a keyword to filter comments:', '')

# 필터링 로직
# 'name' 필터링
if name_to_filter != 'All':
    data = data[data['name'] == name_to_filter]

# '댓글' 필터링
if keyword:
    data = data[data['댓글'].str.contains(keyword, case=False, na=False)]

# 필터링된 데이터 표시
st.write('Filtered YouTube Comments:', data)

# cd C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\Rawling_Study\Rawling_Study\240317_streamlit

# streamlit run YouTube_comment.py
