import streamlit as st
import pandas as pd

# 1. 설정 및 제목
st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

# 로고 경로 생성 함수
def get_lg(cid):
    return f"https://www.kleague.com/assets/img/club/club_logo_{cid}.png"

# 2. K리그1 데이터 (12팀)
k1_raw = [
    [1, get_lg("K01"), "울산 HD", 3, 9, 3, 0, 0], [2, get_lg("K03"), "강원 FC", 3, 7, 2, 1, 0],
    [3, get_lg("K09"), "FC 서울", 3, 6, 2, 0, 1], [4, get_lg("K05"), "포항", 3, 6, 2, 0, 1],
    [5, get_lg("K10"), "수원 FC", 3, 4, 1, 1, 1], [6, get_lg("K21"), "광주 FC", 3, 3, 1, 0, 2],
    [7, get_lg("K07"), "전북 현대", 3, 2, 0, 2, 1], [8, get_lg("K18"), "인천", 3, 2, 0, 2, 1],
    [9, get_lg("K15"), "대전", 3, 1, 0, 1, 2], [10, get_lg("K04"), "제주", 3, 1, 0, 1, 2],
    [11, get_lg("K17"), "대구 FC", 3, 1, 0, 1, 2], [12, get_lg("K25"), "김천 상무", 3, 0, 0, 0, 3]
]
df1 = pd.DataFrame(k1_raw, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# 3. K리그2 데이터 (17팀 - 승무패 데이터 누락 없이 수동 입력)
k2_raw = [
    [1, get_lg("K02"), "수원삼성", 3, 9, 3, 0, 0], [2, get_lg("K04"), "부산", 3, 7, 2, 1, 0],
    [3, get_lg("K15"), "안양", 3, 6, 2, 0, 1], [4, get_lg("K12"), "
