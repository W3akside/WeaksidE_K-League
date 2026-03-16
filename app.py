import streamlit as st
import pandas as pd

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="2026 K-League Dashboard", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

# 로고 호출 함수 (공식 홈페이지 경로 사용)
def get_logo(cid):
    return f"https://www.kleague.com/assets/img/club/club_logo_{cid}.png"

# --- [데이터 선언: K리그1] ---
res1_data = [
    {"일시": "03.14 14:00", "홈": "울산 HD", "점수": "2:1", "원정": "전북 현대", "하이라이트": "https://www.youtube.com/watch?v=kY0vR6z-1pY"},
    {"일시": "03.14 16:30", "홈": "FC 서울", "점수": "0:0", "원정": "강원 FC", "하이라이트": "https://www.youtube.com/watch?v=kY0vR6z-1pY"},
    {"일시": "03.15 14:00", "홈": "광주 FC", "점수": "1:2", "원정": "포항 스틸러스", "하이라이트": "https://www.youtube.com/watch?v=kY0vR6z-1pY"},
    {"일시": "03.15 16:30", "홈": "인천 유나이티드", "점수": "1:1", "원정": "대전 하나", "하이라이트": "https://www.youtube.com/watch?v=kY0vR6z-1pY"},
    {"일시": "03.16 19:00", "홈": "수원 FC", "점수": "경기전", "원정": "대구 FC", "하이라이트": ""},
    {"일시": "03.16 19:30", "홈": "제주 유나이티드", "점수": "경기전", "원정": "김천 상무", "하이라이트": ""}
]

k1_rank = [
    [1, get_logo("K01"), "울산 HD", 3, 9, 3, 0, 0], [2, get_logo("K03"), "강원 FC", 3, 7, 2, 1, 0],
    [3, get_logo("K09"), "FC 서울", 3, 6, 2, 0, 1], [4, get_logo("K05"), "포항 스틸러스", 3, 6, 2, 0, 1],
    [5, get_logo("K10"), "수원 FC", 3, 4, 1, 1, 1], [6, get_logo("K21"), "광주 FC", 3, 3, 1, 0, 2],
    [7, get_logo("K07"), "전북 현대", 3, 2, 0, 2, 1], [8, get_logo("K18"), "인천 유나이티드", 3, 2, 0
