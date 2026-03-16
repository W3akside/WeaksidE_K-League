import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League", page_icon="⚽", layout="wide")

# 제목 (모바일 한 줄 최적화)
st.markdown("<h3 style='text-align: center;'>⚽ K리그 실시간 데이터 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성
@st.cache_data
def get_data():
    k1_list = [
        [1, "울산 HD", 3, 9, 3, 0, 0, 7, 2, "WWW--"],
        [2, "강원 FC", 3, 7, 2, 1, 0, 5, 2, "WWD--"],
        [3, "FC 서울", 3, 6, 2, 0, 1, 4, 3, "WWL--"],
        [4, "포항", 3, 6, 2, 0, 1, 3, 2, "WLW--"],
        [5, "수원 FC", 3, 4, 1, 1, 1, 4, 4, "DWL--"],
        [6, "광주 FC", 3, 3, 1, 0, 2, 3, 5, "LWL--"],
        [7, "전북 현대", 3, 2, 0, 2, 1, 3, 4, "DDL--"],
        [8, "인천", 3, 2, 0, 2, 1, 2, 3, "LDD--"],
        [9, "대전", 3, 1, 0, 1, 2, 2, 5, "DLL--"],
        [10, "제주", 3, 1, 0, 1, 2, 1, 4, "LDL--"],
        [11, "대구 FC", 3, 1, 0, 1, 2, 1, 4, "LLD--"],
        [12, "김천 상무", 3, 0, 0, 0, 3, 1, 6, "LLL--"]
    ]
    k2_list = [
        [1, "수원 삼성", 3, 9, 3, 0, 0, 6, 1, "WWW--"],
        [2, "부산 IPK", 3, 7, 2, 1, 0, 5, 2, "WWD--"]
    ]
    cols = ["순위", "팀명", "경기", "승점", "승", "무", "패", "득", "실", "최근5경기"]
    return pd.DataFrame(k1_list, columns=cols), pd.DataFrame(k2_list, columns=cols)

df1, df2 = get_data()

# 3. 화면 구성
t1, t2, t3 = st.tabs(["🏆 K리그1", "🥈 K리그2", "🎞️ 하이라이트"])

with t1:
    st.dataframe(df1, use_container_width=True, hide_index=True)

with t2:
    st.dataframe(df2, use_container_width=True, hide_index=True)

with t3:
    st.subheader("📺 최근 경기 하이라이트")
    st.info("⚽ [3/15] 울산 2 : 1 전북")
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")
    st.divider()
    st.info("⚽ [3/15] 서울 2 : 1 강원")
    st.write("공식 하이라이트 영상 준비 중입니다.")

st.divider()
st.caption("Last updated: 2026-03-16 | Created by W3akside")
