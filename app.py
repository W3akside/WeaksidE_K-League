import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def lg(cid):
    return f"https://www.kleague.com/assets/img/club/club_logo_{cid}.png"

# --- K리그1 순위 데이터 ---
k1 = {}
k1[0] = [1, lg("K01"), "울산 HD", 3, 9, 3, 0, 0]
k1[1] = [2, lg("K03"), "강원 FC", 3, 7, 2, 1, 0]
k1[2] = [3, lg("K09"), "FC 서울", 3, 6, 2, 0, 1]
k1[3] = [4, lg("K05"), "포항", 3, 6, 2, 0, 1]
k1[4] = [5, lg("K10"), "수원 FC", 3, 4, 1, 1, 1]
k1[5] = [6, lg("K21"), "광주 FC", 3, 3, 1, 0, 2]
k1[6] = [7, lg("K07"), "전북 현대", 3, 2, 0, 2, 1]
k1[7] = [8, lg("K18"), "인천", 3, 2, 0, 2, 1]
k1[8] = [9, lg("K15"), "대전", 3, 1, 0, 1, 2]
k1[9] = [10, lg("K04"), "제주", 3, 1, 0, 1, 2]
k1[10] = [11, lg("K17"), "대구 FC", 3, 1, 0, 1, 2]
k1[11] = [12, lg("K25"), "김천 상무", 3, 0, 0, 0, 3]
df1 = pd.DataFrame(list(k1.values()), columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# --- K리그1 경기 결과 (6경기) ---
res = []
res.append({"홈": "울산", "점수": "2:1", "원정": "전북", "영상": "Link"})
res.append({"홈": "서울", "점수": "0:0", "원정": "강원", "영상": "Link"})
res.append({"홈": "광주", "점수": "1:2", "원정": "포항", "영상": "Link"})
res.append({"홈": "인천", "점수": "1:1", "원정": "대전", "영상": "Link"})
res.append({"홈": "수원F", "점수": "경기전", "원정": "대구", "영상": "-"})
res.append({"홈": "제주", "점수": "경기전", "원정": "김천", "영상": "-"})

# --- K리그2 데이터 (17팀) ---
k2_n = ["수원삼성", "부산", "안양", "전남", "경남", "성남", "충북청주", "부천", "충남아산", "서울E", "천안", "김포", "안산", "용인", "파주", "김해", "청주FC"]
df2 = pd.DataFrame([[i+1, lg("K02"), name, 3, 0, 0, 0, 0] for i, name in enumerate(k2_n)], columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

def stl(r):
    c = 'rgba(255,0,0,0.4)' if r['순위']==12 else ('rgba(255,0,0,0.15)' if r['순위'] in [10,11] else '')
    return [f'background-color: {c}'] * 8 if c else [''] * 8

t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])
with t1:
    st.subheader("📅 최신 결과")
    st.table(pd.DataFrame(res))
    st.subheader("📊 순위표")
    st.dataframe(df1.style.apply(stl, axis=1), use_container_width=True, hide_index=True, column_config={"로고": st.column_config.ImageColumn(" ")})
with t2:
    st.subheader("📊 K2 순위")
    st.dataframe(df2, use_container_width=True, hide_index=True, column_config={"로고": st.column_config.ImageColumn(" ")})
