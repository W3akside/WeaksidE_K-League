import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League", page_icon="⚽", layout="wide")

# 제목 (폰 최적화)
st.markdown("<h3 style='text-align: center;'>⚽ K리그 실시간 데이터 대시보드</h3>", unsafe_allow_html=True)

# 2. 데이터 구성
@st.cache_data
def get_data():
    # 팀별 로고 URL
    l = {
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
    
    k1 = [
        {"로고": l["울산"], "순위": 1, "팀명": "울산 HD", "경기": 3, "승점": 9, "승": 3, "무": 0, "패": 0, "득": 7, "실": 2, "최근5경기": "WWW--"},
        {"로고": l["강원"], "순위": 2, "팀명": "강원 FC", "경기": 3, "승점": 7, "승": 2, "무": 1, "패": 0, "득": 5, "실": 2, "최근5경기": "WWD--"},
        {"로고": l["서울"], "순위": 3, "팀명": "FC 서울", "경기": 3, "승점": 6, "승": 2, "무": 0, "패": 1, "득": 4, "실": 3, "최근5경기": "WWL--"},
        {"로고": l["포항"], "순위": 4, "팀명": "포항", "경기": 3, "승점": 6, "승": 2, "무": 0, "패": 1, "득": 3, "실": 2, "최근5경기": "WLW--"},
        {"로고": l["수원F"], "순위": 5, "팀명": "수원 FC", "경기": 3, "승점": 4, "승": 1, "무": 1, "패": 1, "득": 4, "실": 4, "최근5경기
