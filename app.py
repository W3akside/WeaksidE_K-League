import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League", page_icon="⚽", layout="wide")

# 제목 (모바일 한 줄 최적화)
st.markdown("<h3 style='text-align: center;'>⚽ K리그 실시간 데이터 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성
@st.cache_data
def get_data():
    # 팀별 로고 URL 정리
    logos = {
        "울산": "https://upload.wikimedia.org/wikipedia/ko/d/d4/Ulsan_HD_FC_logo.png",
        "강원": "https://upload.wikimedia.org/wikipedia/ko/a/af/Gangwon_FC_logo.png",
        "서울": "https://upload.wikimedia.org/wikipedia/ko/5/55/FC_Seoul_logo.png",
        "포항": "https://upload.wikimedia.org/wikipedia/ko/c/c0/Pohang_Steelers_logo.png",
        "수원F": "https://upload.wikimedia.org/wikipedia/ko/7/73/Suwon_FC_logo.png",
        "광주": "https://upload.wikimedia.org/wikipedia/ko/e/e3/Gwangju_FC_logo.png",
        "전북": "https://upload.wikimedia.org/wikipedia/ko/d/d0/Jeonbuk_Hyundai_Motors_logo.png",
        "인천": "https://upload.wikimedia.org/wikipedia/ko/c/c1/Incheon_United_FC_logo.png",
        "대전": "https://upload.wikimedia.org/wikipedia/ko/d/d2/Daejeon_Hana_Citizen_logo.png",
        "제주": "https://upload.wikimedia.org/wikipedia/ko/a/a3/Jeju_United_FC_logo.png",
        "대구": "https://upload.wikimedia.org/wikipedia/ko/d/d2/Daegu_FC_logo.png",
        "김천": "https://upload.wikimedia.org/wikipedia/ko/d/d6/Gimcheon_Sangmu_FC_logo.png"
    }
    
    k1_list = [
        [logos["울산"], 1, "울산 HD", 3, 9, 3, 0, 0, 7, 2, "WWW--"],
        [logos["강원"], 2, "강원 FC", 3, 7, 2, 1, 0, 5, 2, "WWD--"],
        [logos["서울"], 3, "FC 서울", 3, 6, 2, 0, 1, 4, 3, "WWL--"],
        [logos["포항"], 4, "포항", 3, 6, 2, 0, 1, 3, 2, "WLW--"],
        [logos["수원F"], 5, "수원 FC", 3, 4, 1, 1, 1, 4, 4, "DWL--"],
        [logos["광주"], 6, "광주 FC", 3, 3, 1, 0, 2, 3, 5, "LWL--"],
        [logos["전북"], 7, "전북 현대", 3, 2, 0, 2, 1, 3, 4, "DDL--"],
        [logos["인천"], 8, "인천", 3, 2, 0, 2, 1, 2, 3, "LDD--"],
        [logos["대전"], 9, "대전", 3, 1, 0, 1, 2, 2, 5, "DLL--"],
        [logos["제주"], 10, "제주", 3, 1, 0, 1, 2, 1, 4, "LDL--"],
        [logos["대구"], 11, "대구 FC", 3, 1, 0, 1, 2, 1, 4, "LLD--"],
        [logos["김천"], 12, "김천 상무", 3, 0, 0, 0, 3, 1, 6, "LLL--"]
    ]
    cols
