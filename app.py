import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League", layout="wide")

# 제목
st.markdown("<h3 style='text-align: center;'>⚽ K리그 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성
@st.cache_data
def get_data():
    # K리그1 데이터
    k1_data = [
        ["울산 HD", 3, 9, 3, 0, 0, 7, 2, "1위"],
        ["강원 FC", 3, 7, 2, 1, 0, 5, 2, "2위"],
        ["FC 서울", 3, 6, 2, 0, 1, 4, 3, "3위"],
        ["포항", 3, 6, 2, 0, 1, 3, 2, "4위"],
        ["수원 FC", 3, 4, 1, 1, 1, 4, 4, "5위"],
        ["광주 FC", 3, 3, 1, 0, 2, 3, 5, "6위"],
        ["전북 현대", 3, 2, 0, 2, 1, 3, 4, "7위"],
        ["인천", 3, 2, 0, 2, 1, 2, 3, "8위"],
        ["대전", 3, 1, 0, 1, 2, 2, 5, "9위"],
        ["제주", 3, 1, 0, 1, 2, 1, 4, "10위(PO)"],
        ["대구 FC", 3, 1, 0, 1, 2, 1, 4, "11위(PO)"],
        ["김천 상무", 3, 0, 0, 0, 3, 1, 6, "12위(강등)"]
    ]
    cols = ["팀명", "경기", "승점", "승", "무", "패", "득", "실", "순위"]
    return pd.DataFrame(k1_data, columns=cols)

df = get_data()

# 3. 화면 구성
tab1, tab2 = st.tabs(["🏆 순위표", "🎞️ 하이라이트"])

with tab1:
    # 에러 방지를 위해 가장 단순한 표 출력
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.info("※ 10~12위는 강등권 및 승강 플레이오프 대상입니다.")

with tab2:
    st.subheader("📺 주요 하이라이트")
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")

st.divider()
st.caption("Last updated: 2026-03-16")
