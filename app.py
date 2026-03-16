import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League", page_icon="⚽", layout="wide")

# 제목 (모바일 한 줄 최적화)
st.markdown("<h3 style='text-align: center;'>⚽ K리그 실시간 데이터 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성 (로고 포함)
@st.cache_data
def get_league_data():
    # K리그1 데이터
    k1 = [
        ["https://www.kleague.com/assets/img/club/club_logo_K01.png", 1, "울산 HD", 3, 9, 3, 0, 0, 7, 2, "WWW--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K21.png", 2, "강원 FC", 3, 7, 2, 1, 0, 5, 2, "WWD--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K09.png", 3, "FC 서울", 3, 6, 2, 0, 1, 4, 3, "WWL--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K03.png", 4, "포항", 3, 6, 2, 0, 1, 3, 2, "WLW--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K29.png", 5, "수원 FC", 3, 4, 1, 1, 1, 4, 4, "DWL--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K22.png", 6, "광주 FC", 3, 3, 1, 0, 2, 3, 5, "LWL--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K05.png", 7, "전북 현대", 3, 2, 0, 2, 1, 3, 4, "DDL--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K18.png", 8, "인천", 3, 2, 0, 2, 1, 2, 3, "LDD--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K10.png", 9, "대전", 3, 1, 0, 1, 2, 2, 5, "DLL--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K16.png", 10, "제주", 3, 1, 0, 1, 2, 1, 4, "LDL--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K17.png", 11, "대구 FC", 3, 1, 0, 1, 2, 1, 4, "LLD--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K32.png", 12, "김천 상무", 3, 0, 0, 0, 3, 1, 6, "LLL--"]
    ]
    # K리그2 데이터
    k2 = [
        ["https://www.kleague.com/assets/img/club/club_logo_K02.png", 1, "수원 삼성", 3, 9, 3, 0, 0, 6, 1, "WWW--"],
        ["https://www.kleague.com/assets/img/club/club_logo_K06.png", 2, "부산 IPK", 3, 7, 2, 1, 0, 5, 2, "WWD--"]
    ]
    cols = ["로고", "순위", "팀명", "경기", "승점", "승", "무", "패", "득", "실", "최근5경기"]
    return pd.DataFrame(k1, columns=cols), pd.DataFrame(k2, columns=cols)

df1, df2 = get_league_data()

# 강등권 강조 스타일 (순위 10위 이상만 연한 빨강)
def bg_style(row):
    color = 'background-color: rgba(255, 0, 0, 0.1)' if row['순위'] >= 10 else ''
    return [color] * len(row)

# 3. 화면 구성
tab1, tab2, tab3 = st.tabs(["🏆 K리그1", "🥈 K리그2", "🎞️ 영상"])

with tab1:
    st.dataframe(
        df1.style.apply(bg_style, axis=1),
        use_container_width=True, hide_index=True,
        column_config={"로고": st.column_config.ImageColumn("로고", width="small")}
    )

with tab2:
    st.dataframe(
        df2, use_container_width=True, hide_index=True,
        column_config={"로고": st.column_config.ImageColumn("로고", width="small")}
    )

with tab3:
    st.subheader("📺 주요 경기 하이라이트")
    st.info("⚽ [3/15] 울산 2 : 1 전북")
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")

st.divider()
st.caption("Last updated: 2026-03-16 | Created by W3akside")
