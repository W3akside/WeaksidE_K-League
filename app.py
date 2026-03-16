import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def get_lg(cid):
    return f"https://www.kleague.com/assets/img/club/club_logo_{cid}.png"

# --- 1. K리그1 데이터 ---
k1_raw = [
    [1, get_lg("K01"), "울산 HD", 3, 9, 3, 0, 0], [2, get_lg("K03"), "강원 FC", 3, 7, 2, 1, 0],
    [3, get_lg("K09"), "FC 서울", 3, 6, 2, 0, 1], [4, get_lg("K05"), "포항", 3, 6, 2, 0, 1],
    [5, get_lg("K10"), "수원 FC", 3, 4, 1, 1, 1], [6, get_lg("K21"), "광주 FC", 3, 3, 1, 0, 2],
    [7, get_lg("K07"), "전북 현대", 3, 2, 0, 2, 1], [8, get_lg("K18"), "인천", 3, 2, 0, 2, 1],
    [9, get_lg("K15"), "대전", 3, 1, 0, 1, 2], [10, get_lg("K04"), "제주", 3, 1, 0, 1, 2],
    [11, get_lg("K17"), "대구 FC", 3, 1, 0, 1, 2], [12, get_lg("K25"), "김천 상무", 3, 0, 0, 0, 3]
]
df1 = pd.DataFrame(k1_raw, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# --- 2. K리그2 데이터 (17팀) ---
k2_teams = ["수원삼성", "부산", "안양", "전남", "경남", "성남", "충북청주", "부천", "충남아산", "서울E", "천안", "김포", "안산", "용인시청", "파주시민", "김해시청", "청주FC"]
k2_raw = [[i+1, get_lg("K02"), name, 3, (17-i)//2, 1, 1, 1] for i, name in enumerate(k2_teams)]
df2 = pd.DataFrame(k2_raw, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# --- 3. 스타일 함수 ---
def stl(row):
    if row['순위'] == 12: return ['background-color: rgba(255, 0, 0, 0.4)'] * 8
    if row['순위'] in [10, 11]: return ['background-color: rgba(255, 0, 0, 0.15)'] * 8
    return [''] * 8

t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])

with t1:
    st.subheader("📅 K1 3라운드 전체 결과")
    k1_res = [
        {"홈팀": "울산", "스코어": "2 : 1", "원정팀": "전북", "하이라이트": "https://youtu.be/kY0vR6z-1pY"},
        {"홈팀": "서울", "스코어": "0 : 0", "원정팀": "강원", "하이라이트": "https://youtu.be/kY0vR6z-1pY"},
