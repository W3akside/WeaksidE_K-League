import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League", page_icon="⚽", layout="wide")

# 제목 (모바일 최적화)
st.markdown("<h3 style='text-align: center;'>⚽ K리그 실시간 데이터 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성 (에러 방지를 위해 스타일 함수 제거)
@st.cache_data
def get_data():
    # K리그1 (12개 팀)
    k1_list = [
        ["https://www.kleague.com/assets/img/club/club_logo_K01.png", "1위", "울산 HD", 3, 9, 3, 0, 0, 7, 2],
        ["https://www.kleague.com/assets/img/club/club_logo_K21.png", "2위", "강원 FC", 3, 7, 2, 1, 0, 5, 2],
        ["https://www.kleague.com/assets/img/club/club_logo_K09.png", "3위", "FC 서울", 3, 6, 2, 0, 1, 4, 3],
        ["https://www.kleague.com/assets/img/club/club_logo_K03.png", "4위", "포항", 3, 6, 2, 0, 1, 3, 2],
        ["https://www.kleague.com/assets/img/club/club_logo_K29.png", "5위", "수원 FC", 3, 4, 1, 1, 1, 4, 4],
        ["https://www.kleague.com/assets/img/club/club_logo_K22.png", "6위", "광주 FC", 3, 3, 1, 0, 2, 3, 5],
        ["https://www.kleague.com/assets/img/club/club_logo_K05.png", "7위", "전북 현대", 3, 2, 0, 2, 1, 3, 4],
        ["https://www.kleague.com/assets/img/club/club_logo_K18.png", "8위", "인천", 3, 2, 0, 2, 1, 2, 3],
        ["https://www.kleague.com/assets/img/club/club_logo_K10.png", "9위", "대전", 3, 1, 0, 1, 2, 2, 5],
        ["https://www.kleague.com/assets/img/club/club_logo_K16.png", "10위(▼)", "제주", 3, 1, 0, 1, 2, 1, 4],
        ["https://www.kleague.com/assets/img/club/club_logo_K17.png", "11위(▼)", "대구 FC", 3, 1, 0, 1, 2, 1, 4],
        ["https://www.kleague.com/assets/img/club/club_logo_K32.png", "12위(▼)", "김천 상무", 3, 0, 0, 0, 3, 1, 6]
    ]
    # K리그2 (확장)
    k2_list = [
        ["https://www.kleague.com/assets/img/club/club_logo_K02.png", "1위", "수원 삼성", 3, 9, 3, 0, 0, 6, 1],
        ["
