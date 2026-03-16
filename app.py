import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League Dashboard", page_icon="⚽", layout="wide")

# 제목 (모바일 최적화)
st.markdown("<h3 style='text-align: center;'>⚽ K리그 실시간 데이터 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성
@st.cache_data
def get_data():
    # K리그1 (12개 팀 풀 데이터)
    k1 = [
        ["https://upload.wikimedia.org/wikipedia/ko/d/d4/Ulsan_HD_FC_logo.png", 1, "울산 HD", 3, 9, 3, 0, 0, 7, 2, "WWW--"],
        ["https://upload.wikimedia.org/wikipedia/ko/a/af/Gangwon_FC_logo.png", 2, "강원 FC", 3, 7, 2, 1, 0, 5, 2, "WWD--"],
        ["https://upload.wikimedia.org/wikipedia/ko/5/55/FC_Seoul_logo.png", 3, "FC 서울", 3, 6, 2, 0, 1, 4, 3, "WWL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/c/c0/Pohang_Steelers_logo.png", 4, "포항", 3, 6, 2, 0, 1, 3, 2, "WLW--"],
        ["https://upload.wikimedia.org/wikipedia/ko/7/73/Suwon_FC_logo.png", 5, "수원 FC", 3, 4, 1, 1, 1, 4, 4, "DWL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/e/e3/Gwangju_FC_logo.png", 6, "광주 FC", 3, 3, 1, 0, 2, 3, 5, "LWL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/d/d0/Jeonbuk_Hyundai_Motors_logo.png", 7, "전북 현대", 3, 2, 0, 2, 1, 3, 4, "DDL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/c/c1/Incheon_United_FC_logo.png", 8, "인천", 3, 2, 0, 2, 1, 2, 3, "LDD--"],
        ["https://upload.wikimedia.org/wikipedia/ko/d/d2/Daejeon_Hana_Citizen_logo.png", 9, "대전", 3, 1, 0, 1, 2, 2, 5, "DLL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/a/a3/Jeju_United_FC_logo.png", 10, "제주", 3, 1, 0, 1, 2, 1, 4, "LDL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/d/d2/Daegu_FC_logo.png", 11, "대구 FC", 3, 1, 0, 1, 2, 1, 4, "LLD--"],
        ["https://upload.wikimedia.org/wikipedia/ko/d/d6/Gimcheon_Sangmu_FC_logo.png", 12, "김천 상무", 3, 0, 0, 0, 3, 1, 6, "LLL--"]
    ]
    # K리그2 (확장 데이터)
    k2 = [
        ["https://upload.wikimedia.org/wikipedia/ko/0/03/Suwon_Samsung_Bluewings_logo.png", 1, "수원 삼성", 3, 9, 3, 0, 0, 6, 1, "WWW--"],
        ["https://upload.wikimedia.org/wikipedia/ko/b/be/Busan_IPark_logo.png", 2, "부산 IPK", 3, 7, 2, 1, 0, 5, 2, "WWD--"],
        ["https://upload.wikimedia.org/wikipedia/ko/5/52/FC_Anyang_logo.png", 3, "안양", 3, 6, 2, 0, 1, 4, 3, "WWL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/4/4c/Gyeongnam_FC_logo.png", 4, "경남", 3, 4, 1, 1, 1, 3, 3, "DWL--"],
        ["https://upload.wikimedia.org/wikipedia/ko/b/b5/Jeonnam_Dragons_logo.png", 5, "전남", 3, 3, 1, 0, 2, 2, 4, "LWL--"]
    ]
