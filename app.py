import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League", page_icon="⚽", layout="wide")

# 제목 (폰 최적화)
st.markdown("<h3 style='text-align: center;'>⚽ K리그 실시간 데이터 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성
@st.cache_data
def get_league_data():
    # 데이터 리스트 (로고 URL, 순위, 팀명, 경기, 승점, 승, 무, 패, 득, 실, 최근5경기)
    data = [
        ["https://upload.wikimedia.org/wikipedia/ko/d/d4/Ulsan_HD_FC_logo.png", 1, "울산 HD", 3, 9, 3, 0, 0, 7, 2, "WWW--"],
        ["https://upload.wikimedia.org/wikipedia/ko/a/af/Gangwon_FC_logo.png", 2, "강원 FC", 3, 7, 2, 1, 0, 5, 2, "WWD--"],
        ["https://upload.wikimedia.org/wikipedia/ko/5/55/FC_Seoul_logo.png", 3, "FC 서울", 3, 6, 2, 0, 1, 4, 3, "WWL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/c/c0/Pohang_Steelers_logo.png", 4, "포항", 3, 6, 2, 0, 1, 3, 2, "WLW--"],
        ["https://upload.wikimedia.org/wikipedia/ko/7/73/Suwon_FC_logo.png", 5, "수원 FC", 3, 4, 1, 1, 1, 4, 4, "DWL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/e/e3/Gwangju_FC_logo.png", 6, "광주 FC", 3, 3, 1, 0, 2, 3, 5, "LWL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/d/d0/Jeonbuk_Hyundai_Motors_logo.png", 7, "전북 현대", 3, 2, 0, 2, 1, 3, 4, "DDL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/c/c1/Incheon_United_FC_logo.png", 8, "인천", 3, 2, 0, 2, 1, 2, 3, "LDD--"],
        ["https://upload.wikimedia.org/wikipedia/ko/d/d2/Daejeon_Hana_Citizen_logo.png", 9, "대전", 3, 1, 0, 1, 2, 2, 5, "DLL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/a/a3/Jeju_United_FC_logo.png", 10, "제주(강등권)", 3, 1, 0, 1, 2, 1, 4, "LDL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/d/d2/Daegu_FC_logo.png", 11, "대구(강등권)", 3, 1, 0, 1, 2, 1, 4, "LLD--"],
        ["https://upload.wikimedia.org/wikipedia/ko/d/d6/Gimcheon_Sangmu_FC_logo.png", 12, "김천(강등권)", 3, 0, 0, 0, 3, 1, 6, "LLL--"]
    ]
    cols = ["로고", "순위", "팀명", "경기", "승점", "승", "무", "패", "득", "실", "최근5경기"]
    return pd.DataFrame(data, columns=cols)

df = get_league_data()

# 3. 화면 구성
tab1, tab2 = st.tabs(["🏆 순위표", "🎞️ 하이라이트"])

with tab1:
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "로고": st.column_config.ImageColumn("로고", width="small"),
            "순위": st.column_config.NumberColumn("순위", format="%d위")
        }
    )
    st.warning("⚠️ 10위~12위는 강등권(승강 플레이오프 대상)입니다.")

with tab2:
    st.subheader("📺 주요 경기 하이라이트")
    st.info("⚽ [3/15] 울산 2 : 1 전북")
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")

st.divider()
st.caption("Last updated: 2026-03-16 | Created by W3akside")
