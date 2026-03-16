import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League Dashboard", layout="wide")
st.markdown("<h3 style='text-align: center;'>⚽ K리그1 & K리그2 통합 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성 (K1: 12팀, K2: 17팀 전체 수록)
@st.cache_data
def get_league_data():
    # K리그1 (12팀)
    k1 = [
        [1, "https://upload.wikimedia.org/wikipedia/ko/d/d4/Ulsan_HD_FC_logo.png", "울산 HD", 9, 3, 3, 0, 0],
        [2, "https://upload.wikimedia.org/wikipedia/ko/a/af/Gangwon_FC_logo.png", "강원 FC", 7, 3, 2, 1, 0],
        [3, "https://upload.wikimedia.org/wikipedia/ko/5/55/FC_Seoul_logo.png", "FC 서울", 6, 3, 2, 0, 1],
        [4, "https://upload.wikimedia.org/wikipedia/ko/c/c0/Pohang_Steelers_logo.png", "포항", 6, 3, 2, 0, 1],
        [5, "https://upload.wikimedia.org/wikipedia/ko/7/73/Suwon_FC_logo.png", "수원 FC", 4, 3, 1, 1, 1],
        [6, "https://upload.wikimedia.org/wikipedia/ko/e/e3/Gwangju_FC_logo.png", "광주 FC", 3, 3, 1, 0, 2],
        [7, "https://upload.wikimedia.org/wikipedia/ko/d/d0/Jeonbuk_Hyundai_Motors_logo.png", "전북 현대", 2, 3, 0, 2, 1],
        [8, "https://upload.wikimedia.org/wikipedia/ko/c/c1/Incheon_United_FC_logo.png", "인천", 2, 3, 0, 2, 1],
        [9, "https://upload.wikimedia.org/wikipedia/ko/d/d2/Daejeon_Hana_Citizen_logo.png", "대전", 1, 3, 0, 1, 2],
        [10, "https://upload.wikimedia.org/wikipedia/ko/a/a3/Jeju_United_FC_logo.png", "제주", 1, 3, 0, 1, 2],
        [11, "https://upload.wikimedia.org/wikipedia/ko/d/d2/Daegu_FC_logo.png", "대구 FC", 1, 3, 0, 1, 2],
        [12, "https://upload.wikimedia.org/wikipedia/ko/d/d6/Gimcheon_Sangmu_FC_logo.png", "김천 상무", 0, 3, 0, 0, 3]
    ]
    # K리그2 (17팀 전체 수록)
    k2 = [
        [1, "https://upload.wikimedia.org/wikipedia/ko/0/03/Suwon_Samsung_Bluewings_logo.png", "수원 삼성", 9, 3, 3, 0, 0],
        [2, "https://upload.wikimedia.org/wikipedia/ko/b/be/Busan_IPark_logo.png", "부산", 7, 3, 2, 1, 0],
        [3, "https://upload.wikimedia.org/wikipedia/ko/5/52/FC_Anyang_logo.png", "안양", 6, 3, 2, 0, 1],
        [4, "https://upload.wikimedia.org/wikipedia/ko/4/4c/Gyeongnam_FC_logo.png", "경남", 4, 3, 1, 1, 1],
        [5, "https://upload.wikimedia.org/wikipedia/ko/b/b5/Jeonnam_Dragons_logo.png", "전남", 3, 3, 1, 0, 2],
        [6, "https://upload.wikimedia.org/wikipedia/ko/0/01/Seongnam_FC_logo.png", "성남 FC", 3, 3, 1, 0, 2],
        [7, "https://upload.wikimedia.org/wikipedia/ko/e/e0/Chungbuk_Cheongju_FC_logo.png", "충북청주", 3, 3, 1, 0, 2],
        [8, "https://upload.wikimedia.org/wikipedia/ko/8/8e/Bucheon_FC_1995_logo.png", "부천 FC", 2, 3, 0, 2, 1],
        [9, "https://upload.wikimedia.org/wikipedia/ko/7/7d/Chungnam_Asan_FC_logo.png", "충남아산", 1, 3, 0, 1, 2],
        [10, "https://upload.wikimedia.org/wikipedia/ko/0/0d/Seoul_E-Land_FC_logo.png", "서울 이랜드", 1, 3, 0, 1, 2],
        [11, "https://upload.wikimedia.org/wikipedia/ko/d/d0/Cheonan_City_FC_logo.png", "천안 시티", 1, 3, 0, 1, 2],
        [12, "https://upload.wikimedia.org/wikipedia/ko/f/f3/Gimpo_FC_logo.png", "김포 FC", 1, 3, 0, 1, 2],
        [13, "https://upload.wikimedia.org/wikipedia/ko/1/1d/Ansan_Greeners_FC_logo.png", "안산 그리너스", 0, 3, 0, 0, 3],
        [14, "https://upload.wikimedia.org/wikipedia/ko/2/23/Cheongju_FC_logo.png", "청주", 0, 3, 0, 0, 3],
        [15, "https://upload.wikimedia.org/wikipedia/ko/5/53/Goyang_Happiness_FC_logo.png", "고양", 0, 3, 0, 0, 3],
        [16, "https://upload.wikimedia.org/wikipedia/ko/d/d5/Pyeongtaek_Citizen_FC_logo.png", "평택", 0, 3, 0, 0, 3],
        [17, "
