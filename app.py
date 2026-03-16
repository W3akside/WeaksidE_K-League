import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 대시보드")

# 1. 로고 함수
def lg(c): return f"https://www.kleague.com/assets/img/club/club_logo_{c}.png"

# 2. K1 데이터 (일단 12팀 핵심 요약)
k1 = [[i+1, lg(f"K0{i+1}" if i < 9 else f"K{i+1}"), f"팀{i+1}", 3, 9-i, 3, 0, 0] for i in range(12)]
df1 = pd.DataFrame(k1, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# 3. K2 데이터 (17팀 생성 - 에러 방지용 루프)
k2 = [[i+1, lg("K02"), f"K2팀{i+1}", 3, 0, 0, 0, 0] for i in range(17)]
df2 = pd.DataFrame(k2, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# 4. 강등권 색상 (12위 진하게, 10-11위 연하게)
def stl(r):
    if r['순위'] == 12: return ['background-color: rgba(255,0,0,0.4)']*8
    if r['순위'] in [10,11]: return ['background-color: rgba(255,0,0,0.15)']*8
    return ['']*8

# 5. 출력부
t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])

with t1:
    st.write("### 📅 최신 결과")
    st.table(pd.DataFrame([{"경기": "울산 2:1 전북", "영상": "Link"}]))
    st.write("### 📊 순위표")
    st.dataframe(df1.style.apply(stl, axis=1), use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn(" ", width="small")})

with t2:
    st.write("### 📊 K2 순위표 (17팀)")
    st.dataframe(df2, use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn(" ", width="small")})
