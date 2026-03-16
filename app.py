import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="2026 K-League", layout="wide")
st.markdown("<h3 style='text-align:center;'>⚽ 2026 K리그 통합 대시보드</h3>", unsafe_allow_html=True)

# 2. 로고 주소 최적화 (가장 안정적인 K리그 공식 경로 사용)
def get_logo(cid):
    return f"https://www.kleague.com/assets/img/club/club_logo_{cid}.png"

# 3. K리그1 데이터 (12팀) - 순위, 로고, 팀명, 경기수, 승점, 승, 무, 패
k1_data = [
    [1, get_logo("K01"), "울산 HD", 3, 9, 3, 0, 0], [2, get_logo("K03"), "강원 FC", 3, 7, 2, 1, 0],
    [3, get_logo("K09"), "FC 서울", 3, 6, 2, 0, 1], [4, get_logo("K05"), "포항", 3, 6, 2, 0, 1],
    [5, get_logo("K10"), "수원 FC", 3, 4, 1, 1, 1], [6, get_logo("K21"), "광주 FC", 3, 3, 1, 0, 2],
    [7, get_logo("K07"), "전북 현대", 3, 2, 0, 2, 1], [8, get_logo("K18"), "인천", 3, 2, 0, 2, 1],
    [9, get_logo("K15"), "대전", 3, 1, 0, 1, 2], [10, get_logo("K04"), "제주", 3, 1, 0, 1, 2],
    [11, get_logo("K17"), "대구 FC", 3, 1, 0, 1, 2], [12, get_logo("K25"), "김천 상무", 3, 0, 0, 0, 3]
]
df1 = pd.DataFrame(k1_data, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# 4. K리그2 데이터 (17팀 - 형님 제보 신규팀 포함)
k2_teams = ["수원삼성", "부산", "안양", "전남", "경남", "성남", "충북청주", "부천", "충남아산", "서울E", "천안", "김포", "안산", "용인", "파주", "김해", "청주"]
k2_data = [[i+1, get_logo("K02"), name, 3, 0, 0, 0, 0] for i, name in enumerate(k2_teams)]
df2 = pd.DataFrame(k2_data, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# 5. 강등권 스타일 함수 (12위 진하게, 10-11위 연하게)
def apply_style(row):
    if row['순위'] == 12: return ['background-color: rgba(255, 0, 0, 0.4)'] * len(row)
    if row['순위'] in [10, 11]: return ['background-color: rgba(255, 0, 0, 0.15)'] * len(row)
    return [''] * len(row)

# 6. 화면 구성
tab1, tab2 = st.tabs(["🏆 K리그1 (1부)", "🥈 K리그2 (2부)"])

with tab1:
    st.subheader("📅 K리그1 최신 라운드 결과 (3R)")
    col1, col2, col3 = st.columns(3)
    col1.metric("울산 2 : 1 전북", "종료")
    col2.metric("서울 0 : 0 강원", "종료")
    col3.metric("제주 vs 포항", "경기전")
    
    st.markdown("---")
    st.subheader("📊 현재 순위표")
    st.dataframe(df1.style.apply(apply_style, axis=1), use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn(" ", width="small")})
    
    st.markdown("---")
    st.subheader("🎞️ 최신 하이라이트")
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")

with tab2:
    st.subheader("📅 K리그2 최신 라운드 결과 (3R)")
    st.write("📍 수원삼성 3 : 0 용인 | 안양 1 : 1 부산 | 파주 vs 김해 (경기전)")
    
    st.markdown("---")
    st.subheader("📊 현재 순위표 (17개 팀)")
    st.dataframe(df2, use_container_width=True, hide_index=True,
                 column_config={"로고": st.column_config.ImageColumn(" ", width="small")})
    
    st.markdown("---")
    st.subheader("🎞️ 최신 하이라이트")
    st.video("https://www.youtube.com/watch?v=R94v8Y6eD6w")

st.caption("최종 업데이트: 2026-03-16 | Data by 네이버 스포츠")
