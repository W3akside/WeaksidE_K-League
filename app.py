import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K리그", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

# 로고 및 스타일 설정
def lg(c): return f"https://www.kleague.com/assets/img/club/club_logo_{c}.png"

def stl(r, is_k1=True):
    bg = ''
    if is_k1:
        if r['순위'] == 12: bg = 'rgba(255,0,0,0.4)'
        elif r['순위'] in [10, 11]: bg = 'rgba(255,0,0,0.15)'
    return [f'background-color: {bg}; text-align: center;'] * 8

# --- K리그1 데이터 ---
k1_res = [
    ["03.14 14:00", "울산 HD", "2:1", "전북 현대", "https://www.youtube.com/watch?v=kY0vR6z-1pY"],
    ["03.14 16:30", "FC 서울", "0:0", "강원 FC", "https://www.youtube.com/watch?v=kY0vR6z-1pY"],
    ["03.15 14:00", "광주 FC", "1:2", "포항 스틸러스", "https://www.youtube.com/watch?v=kY0vR6z-1pY"],
    ["03.15 16:30", "인천 유나이티드", "1:1", "대전 하나", "https://www.youtube.com/watch?v=kY0vR6z-1pY"],
    ["03.16 19:00", "수원 FC", "경기전", "대구 FC", ""],
    ["03.16 19:30", "제주 유나이티드", "경기전", "김천 상무", ""]
]
k1_rnk = [
    [1,lg("K01"),"울산 HD",3,9,3,0,0],[2,lg("K03"),"강원 FC",3,7,2,1,0],
    [3,lg("K09"),"FC 서울",3,6,2,0,1],[4,lg("K05"),"포항 스틸러스",3,6,2,0,1],
    [5,lg("K10"),"수원 FC",3,4,1,1,1],[6,lg("K21"),"광주 FC",3,3,1,0,2],
    [7,lg("K07"),"전북 현대",3,2,0,2,1],[8,lg("K18"),"인천 유나이티드",3,2,0,2,1],
    [9,lg("K15"),"대전 하나",3,1,0,1,2],[10,lg("K04"),"제주 유나이티드",3,1,0,1,2],
    [11,lg("K17"),"대구 FC",3,1,0,1,2],[12,lg("K25"),"김천 상무",3,0,0,0,3]
]

# --- K리그2 데이터 ---
k2_res = [
    ["03.14 14:00", "수원삼성", "3:0", "용인시청", "https://www.youtube.com/watch?v=R94v8Y6eD6w"],
    ["03.14 16:30", "안양 FC", "1:1", "부산 아이파크", "https://www.youtube.com/watch?v=R94v8Y6eD6w"],
    ["03.15 14:00", "파주시민", "경기전", "김해시청", ""]
]
k2_nm = ["수원삼성","부산","안양","전남","경남","성남","충북청주","부천","충남아산","서울E","천안","김포","안산","용인","파주","김해","청주FC"]
k2_rnk = [[i+1,lg("K02"),n,3,4,1,1,1] for i,n in enumerate(k2_nm)]

# --- 화면 출력 ---
t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])

with t1:
    st.subheader("📅 K리그1 결과")
    st.dataframe(pd.DataFrame(k1_res, columns=["일시","홈","점수","원정","영상"]), use
