# pip install streamlit 라이브러리 설치

import streamlit as st
import pandas as pd

# 제목 설정
st.title('YouTube Comment Viewer')

# 파일 경로 설정
file_path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\Rawling_Study\Rawling_Study\240317_streamlit\YouTube_comment_61220.csv'

# CSV 파일 불러오기
data = pd.read_csv(file_path)

# 필터링할 라벨 선택
label_to_filter = st.sidebar.selectbox(
    'Select a label to filter:',
    pd.unique(data['labels'])
)

# 필터링된 데이터 표시
filtered_data = data[data['labels'] == label_to_filter]
st.write('YouTube Comments filtered by label:', filtered_data)


# cd C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\Rawling_Study\Rawling_Study\240317_streamlit

# streamlit run YouTube_comment.py
