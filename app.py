import streamlit as st
import pandas as pd

st.set_page_config(page_title="K-League", layout="wide")
st.markdown("<h3 style='text-align:center;'>⚽ K리그 실시간 데이터</h3>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    # K1 데이터: 순위, 로고, 팀명, 승점, 경기, 승, 무, 패
    k1 = [
        ["1위", "https://www.kleague.com/assets/img/club/club_logo_K01.png", "울산", 9, 3, 3, 0, 0],
        ["2위", "https://www.kleague.com/assets/img/club/club_logo_K21.png", "강원", 7, 3, 2, 1, 0],
        ["3위", "https://www.kleague.com/assets/img/club/club_logo_K09.png", "서울", 6, 3, 2, 0, 1],
        ["4위", "https://www.kleague.com/assets/img/club/club_logo_K03.png", "포항", 6, 3, 2, 0, 1],
        ["10위(▼)", "https://www.kleague.com/assets/img/club/club_logo_K16.png", "제주", 1, 3, 0, 1, 2],
        ["11위(▼)", "https://www.kleague.com/assets/img/club/club_logo_K17.png", "대구", 1, 3, 0, 1, 2],
        ["12위(▼)", "https://www.kleague.com/assets/img/club/club_logo_K32.png", "김천", 0, 3, 0, 0, 3]
    ]
    # K2 데이터
    k2 = [
        ["1위", "https://www.kleague.com/assets/img/club/club_logo_K02.png", "수원S", 9, 3, 3, 0, 0],
        ["2위", "https://www.kleague.com/assets/img/club/club_logo_K06.png", "부산", 7, 3, 2, 1, 0]
    ]
    cols = ["순위", "로고", "팀명", "승점", "경기", "승", "무", "패"]
    return pd.DataFrame(k1, columns=cols), pd.DataFrame(k2, columns=cols)

df1, df2 = load_data()

t1, t2, t3 = st.tabs(["🏆 K리그1", "🥈 K리그2", "🎞️ 영상"])

with t1:
    st.dataframe(df1, use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn("", width="small")})

with t2:
    st.dataframe(df2, use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn("", width="small")})

with t3:
    st.subheader("📺 주요 하이라이트")
    st.info("📅 [26/03/15] 울산 vs 전북")
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")

st.caption("Last updated: 2026-03-16")
