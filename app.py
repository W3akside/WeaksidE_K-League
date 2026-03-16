import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def get_lg(cid):
    return f"https://www.kleague.com/assets/img/club/club_logo_{cid}.png"

# K리그1 데이터
k1_raw = [
    [1, get_lg("K01"), "울산 HD", 3, 9, 3, 0, 0], [2, get_lg("K03"), "강원 FC", 3, 7, 2, 1, 0],
    [3, get_lg("K09"), "FC 서울", 3, 6, 2, 0, 1], [4, get_lg("K05"), "포항", 3, 6, 2, 0, 1],
    [5, get_lg("K10"), "수원 FC", 3, 4, 1, 1, 1], [6, get_lg("K21"), "광주 FC", 3, 3, 1, 0, 2],
    [7, get_lg("K07"), "전북 현대", 3, 2, 0, 2, 1], [8, get_lg("K18"), "인천", 3, 2, 0, 2, 1],
    [9, get_lg("K15"), "대전", 3, 1, 0, 1, 2], [10, get_lg("K04"), "제주", 3, 1, 0, 1, 2],
    [11, get_lg("K17"), "대구 FC", 3, 1, 0, 1, 2], [12, get_lg("K25"), "김천 상무", 3, 0, 0, 0, 3]
]
df1 = pd.DataFrame(k1_raw, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# K리그2 데이터 (17팀 분할 선언 - 잘림 방지)
k2_p1 = [[1, get_lg("K02"), "수원삼성", 3, 9, 3, 0, 0], [2, get_lg("K04"), "부산", 3, 7, 2, 1, 0],
         [3, get_lg("K15"), "안양", 3, 6, 2, 0, 1], [4, get_lg("K12"), "전남", 3, 6, 2, 0, 1],
         [5, get_lg("K14"), "경남", 3, 5, 1, 2, 0], [6, get_lg("K06"), "성남", 3, 4, 1, 1, 1]]
k2_p2 = [[7, get_lg("K26"), "충북청주", 3, 4, 1, 1, 1], [8, get_lg("K13"), "부천", 3, 4, 1, 1, 1],
         [9, get_lg("K23"), "충남아산", 3, 3, 1, 0, 2], [10, get_lg("K22"), "서울E", 3, 3, 1, 0, 2],
         [11, get_lg("K27"), "천안", 3, 2, 0, 2, 1], [12, get_lg("K29"), "김포", 3, 1, 0, 1, 2]]
k2_p3 = [[13, get_lg("K11"), "안산", 3, 1, 0, 1, 2], [14, get_lg("K30"), "용인시청", 3, 0, 0, 0, 3],
         [15, get_lg("K31"), "파주시민", 3, 0, 0, 0, 3], [16, get_lg("K32"), "김해시청", 3, 0, 0, 0, 3],
         [17, get_lg("K33"), "청주FC", 3, 0, 0, 0, 3]]
df2 = pd.DataFrame(k2_p1 + k2_p2 + k2_p3, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

def stl(row):
    if row['순위'] == 12: return ['background-color: rgba(255, 0, 0, 0.4)'] * 8
    if row['순위'] in [10, 11]: return ['background-color: rgba(255, 0, 0, 0.15)'] * 8
    return [''] * 8
