import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="2026 K-League", layout="wide")
st.markdown("<h3 style='text-align:center;'>⚽ 2026 K리그 통합 대시보드</h3>", unsafe_allow_html=True)

# 2. 로고 함수 및 데이터 준비
def get_logo(cid):
    return f"https://www.kleague.com/assets/img/club/club_logo_{cid}.png"

# K1 순위 데이터 (12팀)
k1_data = [
    [1, get_logo("K01"), "울산 HD", 3, 9, 3, 0, 0], [2, get_logo("K03"), "강원 FC", 3, 7, 2, 1, 0],
    [3, get_logo("K09"), "FC 서울", 3, 6, 2, 0, 1], [4, get_logo("K05"), "포항", 3, 6, 2, 0, 1],
    [5, get_logo("K10"), "수원 FC", 3, 4, 1, 1, 1], [6, get_logo("K21"), "광주 FC", 3, 3, 1, 0, 2],
    [7, get_logo("K07"), "전북 현대", 3, 2, 0, 2, 1], [8, get_logo("K18"), "인천", 3, 2, 0, 2, 1],
    [9, get_logo("K15"), "대전", 3, 1, 0, 1, 2], [10, get_logo("K04"), "제주", 3, 1, 0, 1, 2],
    [11, get_logo("K17"), "대구 FC", 3, 1, 0, 1, 2], [12, get_logo("K25"), "김천 상무", 3, 0, 0, 0, 3]
]
df1 = pd.DataFrame(k1_data, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# 3. 스타일 함수 (12위 진한빨강, 10-11위 연한빨강)
def apply_style(row):
    if row['순위'] == 12: return ['background-color: rgba(255, 0, 0, 0.4)'] * len(row)
    if row['순위'] in [10, 11]: return ['background-color: rgba(255, 0, 0, 0.15)'] * len(row)
    return [''] * len(row)

# 4. 화면 구성
tab1, tab2 = st.tabs(["🏆 K리그1 (1부)", "🥈 K리그2 (2부)"])

with tab1:
    st.subheader("📅 K리그1 최신 라운드 결과 & 하이라이트")
    # 경기 결과 표 (홈팀 골
