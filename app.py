import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League Dashboard", page_icon="⚽", layout="wide")

# 제목
st.markdown("<h3 style='text-align: center;'>⚽ K리그 실시간 데이터 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성 (기능 고정: 로고, 순위 맨 앞, K리그 1&2)
@st.cache_data
def get_league_data():
    # K리그1 (순위를 맨 앞으로 배치)
    k1 = [
        ["1위", "https://www.kleague.com/assets/img/club/club_logo_K01.png", "울산 HD", 3, 9, 3, 0, 0, 7, 2],
        ["2위", "https://www.kleague.com/assets/img/club/club_logo_K21.png", "강원 FC", 3, 7, 2, 1, 0, 5, 2],
        ["3위", "https://www.kleague.com/assets/img/club/club_logo_K09.png", "FC 서울", 3, 6, 2, 0, 1, 4, 3],
        ["4위", "https://www.kleague.com/assets/img/club/club_logo_K03.png", "포항", 3, 6, 2, 0, 1, 3, 2],
        ["5위", "https://www.kleague.com/assets/img/club/club_logo_K29.png", "수원 FC", 3, 4, 1, 1, 1, 4, 4],
        ["6위", "https://www.kleague.com/assets/img/club/club_logo_K22.png", "광주 FC", 3, 3, 1, 0, 2, 3, 5],
        ["7위", "https://www.kleague.com/assets/img/club/club_logo_K05.png", "전북 현대", 3, 2, 0, 2, 1, 3, 4],
        ["8위", "https://www.kleague.com/assets/img/club/club_logo_K18.png", "인천", 3, 2, 0, 2, 1, 2, 3],
        ["9위", "https://www.kleague.com/assets/img/club/club_logo_K10.png", "대전", 3, 1, 0, 1, 2, 2, 5],
        ["10위(▼)", "https://www.kleague.com/assets/img/club/club_logo_K16.png", "제주", 3, 1, 0, 1, 2, 1, 4],
        ["11위(▼)", "https://www.kleague.com/assets/img/club/club_logo_K17.png", "대구 FC", 3, 1, 0, 1, 2, 1, 4],
        ["12위(▼)", "https://www.kleague.com/assets/img/club/club_logo_K32.png", "김천 상무", 3, 0, 0, 0, 3, 1, 6]
    ]
    # K리그2 (순위 맨 앞 고정)
    k2 = [
        ["1위", "https://www.kleague.com/assets/img/club/club_logo_K02.png", "수원 삼성", 3, 9, 3, 0, 0, 6, 1],
        ["2위", "https://www.kleague.com/assets/img/club/club_logo_K06.png", "부산 IPK", 3, 7, 2, 1, 0, 5, 2],
        ["3위", "https://www.kleague.com/assets/img/club/club_logo_K25.png", "안양", 3, 6, 2, 0, 1, 4, 3],
        ["4위", "https://www.kleague.com/assets/img/club/club_logo_K20.png", "경남", 3, 4, 1, 1, 1, 3, 3],
        ["5위", "https://www.kleague.com/assets/img/club/club_logo_K07.png", "전남", 3, 3, 1, 0, 2, 2, 4]
    ]
    cols = ["순위", "로고", "팀명", "경기", "승점", "승", "무", "패", "득", "실"]
    return pd.DataFrame(k1, columns=cols), pd.DataFrame(k2, columns=cols)

df1, df2 = get_league_data()

# 3. 화면 구성
tab1, tab2, tab3 = st.tabs(["🏆 K리그1", "🥈 K리그2", "🎞️ 하이라이트"])

with tab1:
    st.dataframe(df1, use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn(" ", width="small")})
    st.caption("※ 10~12위(▼)는 강등권 및 승강 플레이오프 대상입니다.")

with tab2:
    st.dataframe(df2, use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn(" ", width="small")})

with tab3:
    st.subheader("📺 2026 시즌 주요 하이라이트")
    st.info("📅 [2026/03/15] 울산 HD 2 : 1 전북 현대")
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")
    st.divider()
    st.info("📅 [2026/03/15] FC 서울 1 : 1 강원 FC")
    st.video("
