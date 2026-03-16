import streamlit as st
import pandas as pd

# 1. 화면 초기 설정
st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

# 로고 가져오기 도구
def get_logo(code): 
    return f"https://www.kleague.com/assets/img/club/club_logo_{code}.png"

# 표 스타일 (가운데 정렬 + 강등권 색상)
def apply_style(row):
    bg = ''
    if row['순위'] == 12: bg = 'rgba(255,0,0,0.4)'
    elif row['순위'] in [10, 11]: bg = 'rgba(255,0,0,0.15)'
    return [f'background-color: {bg}; text-align: center;'] * 8

# 2. 최신 경기 결과 데이터
match_data = [
    ["03.14 14:00", "울산 HD", "2:1", "전북 현대", "https://youtu.be/kY0vR6z-1pY"],
    ["03.14 16:30", "FC 서울", "0:0", "강원 FC", "https://youtu.be/kY0vR6z-1pY"],
    ["03.15 14:00", "광주 FC", "1:2", "포항 스틸러스", "https://youtu.be/kY0vR6z-1pY"],
    ["03.15 16:30", "인천 유나이티드", "1:1", "대전 하나", "https://youtu.be/kY0vR6z-1pY"],
    ["03.16 19:00", "수원 FC", "경기전", "대구 FC", ""],
    ["03.16 19:30", "제주 유나이티드", "경기전", "김천 상무", ""]
]

# 3. K리그1 순위 데이터
rank_data = [
    [1, get_logo("K01"), "울산 HD", 3, 9, 3, 0, 0],
    [2, get_logo("K05"), "포항 스틸러스", 3, 7, 2, 1, 0],
    [3, get_logo("K03"), "강원 FC", 3, 7, 2, 1, 0],
    [4, get_logo("K09"), "FC 서울", 3, 6, 2, 0, 1],
    [5, get_logo("K10"), "수원 FC", 3, 4, 1, 1, 1],
    [6, get_logo("K21"), "광주 FC", 3, 3, 1, 0, 2],
    [7, get_logo("K07"), "전북 현대", 3, 2, 0, 2, 1],
    [8, get_logo("K18"), "인천 유나이티드", 3, 2, 0, 2, 1],
    [9, get_logo("K15"), "대전 하나", 3, 1, 0, 1, 2],
    [10, get_logo("K04"), "제주 유나이티
