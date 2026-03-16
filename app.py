import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League Dashboard", layout="wide")
st.markdown("<h3 style='text-align:center;'>⚽ K리그 실시간 데이터</h3>", unsafe_allow_html=True)

# 2. 데이터 로드 (순위 1~12위 풀 데이터)
@st.cache_data
def load_data():
    # K1: 순위, 로고, 팀명, 승점, 경기, 승, 무, 패
    k1 = [
        ["1위", "https://upload.wikimedia.org/wikipedia/ko/d/d4/Ulsan_HD_FC_logo.png", "울산 HD", 9, 3, 3, 0, 0],
        ["2위", "https://upload.wikimedia.org/wikipedia/ko/a/af/Gangwon_FC_logo.png", "강원 FC", 7, 3, 2, 1, 0],
        ["3위", "https://upload.wikimedia.org/wikipedia/ko/5/55/FC_Seoul_logo.png", "FC 서울", 6, 3, 2, 0, 1],
        ["4위", "https://upload.wikimedia.org/wikipedia/ko/c/c0/Pohang_Steelers_logo.png", "포항", 6, 3, 2, 0, 1],
        ["5위", "https://upload.wikimedia.org/wikipedia/ko/7/73/Suwon_FC_logo.png", "수원 FC", 4, 3, 1, 1, 1],
        ["6위", "https://upload.wikimedia.org/wikipedia/ko/e/e3/Gwangju_FC_logo.png", "광주 FC", 3, 3, 1, 0, 2],
        ["7위", "https://upload.wikimedia.org/wikipedia/ko/d/d0/Jeonbuk_Hyundai_Motors_logo.png", "전북 현대", 2, 3, 0, 2, 1],
        ["8위", "https://upload.wikimedia.org/wikipedia/ko/c/c1/Incheon_United_FC_logo.png", "인천", 2, 3, 0, 2, 1],
        ["9위", "https://upload.wikimedia.org/wikipedia/ko/d/d2/Daejeon_Hana_Citizen_logo.png", "대전", 1, 3, 0, 1, 2],
        ["10위(▼)", "https://upload.wikimedia.org/wikipedia/ko/a/a3/Jeju_United_FC_logo.png", "제주", 1, 3, 0, 1, 2],
        ["11위(▼)", "https://upload.wikimedia.org/wikipedia/ko/d/d2/Daegu_FC_logo.png", "대구 FC", 1, 3, 0, 1, 2],
        ["12위(▼)", "https://upload.wikimedia.org/wikipedia/ko/d/d6/Gimcheon_Sangmu_FC_logo.png", "김천 상무", 0, 3, 0, 0, 3]
    ]
    # K2: 주요 팀 데이터
    k2 = [
        ["1위", "https://upload.wikimedia.org/wikipedia/ko/0/03/Suwon_Samsung_Bluewings_logo.png", "수원 삼성", 9, 3, 3, 0, 0],
        ["2위", "https://upload.wikimedia.org/wikipedia/ko/b/be/Busan_IPark_logo.png", "부산 IPK", 7, 3, 2, 1, 0],
        ["3위", "https://upload.wikimedia.org/wikipedia/ko/5/52/FC_Anyang_logo.png", "안양", 6, 3, 2, 0, 1]
    ]
    cols = ["순위", "로고", "팀명", "승점", "경기", "승", "무", "패"]
    return pd.DataFrame(k1, columns=cols), pd.DataFrame(k2, columns=cols)

df1, df2 = load_data()

# 3. 화면 구성
t1, t2, t3 = st.tabs(["🏆 K리그1", "🥈 K리그2", "🎞️ 하이라이트"])

with t1:
    st.dataframe(df1, use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn("", width="small")})
    st.caption("※ 10~12위(▼)는 강등권 및 승강 플레이오프 대상입니다.")

with t2:
    st.dataframe(df2, use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn("", width="small")})

with t3:
    st.subheader("📺 주요 하이라이트")
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")

st.caption("최종 업데이트: 2026-03-16")
