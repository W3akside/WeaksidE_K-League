import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def get_lg(cid):
    return f"https://www.kleague.com/assets/img/club/club_logo_{cid}.png"

# --- 1. K리그1 데이터 (순위표) ---
k1_d = [
    [1, get_lg("K01"), "울산 HD", 3, 9, 3, 0, 0], [2, get_lg("K03"), "강원 FC", 3, 7, 2, 1, 0],
    [3, get_lg("K09"), "FC 서울", 3, 6, 2, 0, 1], [4, get_lg("K05"), "포항", 3, 6, 2, 0, 1],
    [5, get_lg("K10"), "수원 FC", 3, 4, 1, 1, 1], [6, get_lg("K21"), "광주 FC", 3, 3, 1, 0, 2],
    [7, get_lg("K07"), "전북 현대", 3, 2, 0, 2, 1], [8, get_lg("K18"), "인천", 3, 2, 0, 2, 1],
    [9, get_lg("K15"), "대전", 3, 1, 0, 1, 2], [10, get_lg("K04"), "제주", 3, 1, 0, 1, 2],
    [11, get_lg("K17"), "대구 FC", 3, 1, 0, 1, 2], [12, get_lg("K25"), "김천 상무", 3, 0, 0, 0, 3]
]
df1 = pd.DataFrame(k1_d, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# --- 2. K리그1 최신 결과 (6경기 모두 유지) ---
k1_res_p1 = [
    {"홈팀": "울산", "스코어": "2 : 1", "원정팀": "전북", "하이라이트": "https://youtu.be/kY0vR6z-1pY"},
    {"홈팀": "서울", "스코어": "0 : 0", "원정팀": "강원", "하이라이트": "https://youtu.be/kY0vR6z-1pY"},
    {"홈팀": "광주", "스코어": "1 : 2", "원정팀": "포항", "하이라이트": "https://youtu.be/kY0vR6z-1pY"}
]
k1_res_p2 = [
    {"홈팀": "인천", "스코어": "1 : 1", "원정팀": "대전", "하이라이트": "https://youtu.be/kY0vR6z-1pY"},
    {"홈팀": "수원F", "스코어": "경기전", "원정팀": "대구", "하이
