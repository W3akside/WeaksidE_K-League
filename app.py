import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="K-League Dashboard", page_icon="⚽", layout="wide")

st.title("⚽ K리그 실시간 데이터 대시보드")
st.write("본 서비스는 K리그1 및 K리그2의 순위 정보를 제공합니다.")

# 2. 데이터 구성
@st.cache_data
def get_league_data():
    k1 = [
        {"순위": 1, "팀명": "울산 HD", "경기": 3, "승점": 9},
        {"순위": 2, "팀명": "강원 FC", "경기": 3, "승점": 7},
        {"순위": 3, "팀명": "FC 서울", "경기": 3, "승점": 6},
        {"순위": 4, "팀명": "포항 스틸러스", "경기": 3, "승점": 6},
        {"순위": 5, "팀명": "수원 FC", "경기": 3, "승점": 4},
        {"순위": 6, "팀명": "광주 FC", "경기": 3, "승점": 3},
        {"순위": 7, "팀명": "전북 현대", "경기": 3, "승점": 2},
        {"순위": 8, "팀명": "인천 유나이티드", "경기": 3, "승점": 2},
        {"순위": 9, "팀명": "대전 하나 시티즌", "경기": 3, "승점": 1},
        {"순위": 10, "팀명": "제주 유나이티드", "경기": 3, "승점": 1},
        {"순위": 11, "팀명": "대구 FC", "경기": 3, "승점": 1},
        {"순위": 12, "팀명": "김천 상무", "경기": 3, "승점": 0}
    ]
    k2 = [
        {"순위": 1, "팀명": "수원 삼성", "경기": 3, "승점": 9},
        {"순위": 2, "팀명": "부산 아이파크", "경기": 3, "승점": 7},
        {"순위": 3, "팀명": "서울 이랜드", "경기": 3, "승점": 6},
        {"순위": 4, "팀명": "전남 드래곤즈", "경기": 3, "승점": 6},
        {"순위": 5, "팀명": "경남 FC", "경기": 3, "승점": 4},
        {"순위": 6, "팀명": "성남 FC", "경기": 3, "승점": 3},
        {"순위": 7, "팀명": "충남 아산", "경기": 3, "승점": 3},
        {"순위": 8, "팀명": "부천 FC 1995", "경기": 3, "승점": 2},
        {"순위": 9, "팀명": "천안 시티", "경기": 3, "승점": 1},
        {"순위": 10, "팀명": "충북 청주", "경기": 3, "승점": 1},
        {"순위": 11, "팀명": "안산 그리너스", "경기": 3, "승점": 1},
        {"순위": 12, "팀명": "FC 안양", "경기": 3, "승점": 0},
        {"순위": 13, "팀명": "김포 FC", "경기": 3, "승점": 0}
    ]
    return pd.DataFrame(k1), pd.DataFrame(k2)

df1, df2 = get_league_data()

# 3. 화면 탭 구성
tab1, tab2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])

with tab1:
    st.subheader("2026 K리그1 현재 순위")
    st.dataframe(df1, use_container_width=True, hide_index=True)

with tab2:
    st.subheader("2026 K리그2 현재 순위")
    st.dataframe(df2, use_container_width=True, hide_index=True)

st.divider()

# 4. 하단 정보
st.subheader("🔗 관련 링크")
col1, col2 = st.columns(2)
with col1:
    st.link_button("네이버 스포츠 K리그", "https://sports.news.naver.com/kfootball/index")
with col2:
    st.link_button("K리그 공식 홈페이지", "https://www.kleague.com/")

st.caption("Last updated: 2026-03-16 | Created by W3akside Dashboard")
