import streamlit as st
import pandas as pd

st.set_page_config(page_title="K-League", layout="wide")
st.markdown("<h3 style='text-align:center;'>⚽ K리그1 & K리그2 통합 대시보드</h3>", unsafe_allow_html=True)

# 1. 데이터 로드 (잘림 방지를 위해 리스트를 최소화하여 구성)
@st.cache_data
def load_data():
    # K1 데이터 (12팀)
    k1_raw = [
        [1, "울산 HD", 9, 3, "https://upload.wikimedia.org/wikipedia/ko/d/d4/Ulsan_HD_FC_logo.png"],
        [2, "강원 FC", 7, 3, "https://upload.wikimedia.org/wikipedia/ko/a/af/Gangwon_FC_logo.png"],
        [3, "FC 서울", 6, 3, "https://upload.wikimedia.org/wikipedia/ko/5/55/FC_Seoul_logo.png"],
        [4, "포항", 6, 3, "https://upload.wikimedia.org/wikipedia/ko/c/c0/Pohang_Steelers_logo.png"],
        [5, "수원 FC", 4, 3, "https://upload.wikimedia.org/wikipedia/ko/7/73/Suwon_FC_logo.png"],
        [6, "광주 FC", 3, 3, "https://upload.wikimedia.org/wikipedia/ko/e/e3/Gwangju_FC_logo.png"],
        [7, "전북 현대", 2, 3, "https://upload.wikimedia.org/wikipedia/ko/d/d0/Jeonbuk_Hyundai_Motors_logo.png"],
        [8, "인천", 2, 3, "https://upload.wikimedia.org/wikipedia/ko/c/c1/Incheon_United_FC_logo.png"],
        [9, "대전", 1, 3, "https://upload.wikimedia.org/wikipedia/ko/d/d2/Daejeon_Hana_Citizen_logo.png"],
        [10, "제주", 1, 3, "https://upload.wikimedia.org/wikipedia/ko/a/a3/Jeju_United_FC_logo.png"],
        [11, "대구 FC", 1, 3, "https://upload.wikimedia.org/wikipedia/ko/d/d2/Daegu_FC_logo.png"],
        [12, "김천 상무", 0, 3, "https://upload.wikimedia.org/wikipedia/ko/d/d6/Gimcheon_Sangmu_FC_logo.png"]
    ]
    # K2 데이터 (2025년 기준 13개 팀)
    k2_raw = [[i+1, team, 0, 0, "https://www.kleague.com/assets/img/club/club_logo_K02.png"] for i, team in enumerate(["수원삼성", "부산", "안양", "전남", "경남", "성남", "부천", "이랜드", "충북청주", "충남아산", "김포", "천안", "안산"])]
    
    cols = ["순위", "팀명", "승점", "경기", "로고"]
    return pd.DataFrame(k1_raw, columns=cols), pd.DataFrame(k2_raw, columns=cols)

df1, df2 = load_data()

# 2. 강등권 스타일 (10~12위 연한 빨강)
def style_relegation(row):
    return ['background-color: rgba(255,0,0,0.1)' if row['순위'] >= 10 else '' for _ in row]

# 3. 화면 구성
t1, t2, t3 = st.tabs(["🏆 K리그1", "🥈 K리그2", "🎞️ 영상"])

with t1:
    st.dataframe(df1.style.apply(style_relegation, axis=1), use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn("로고")})

with t2:
    st.dataframe(df2, use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn("로고")})

with t3:
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")
