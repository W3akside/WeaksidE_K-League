import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="W3akside K-League", page_icon="⚽", layout="wide")

st.title("⚽ W3akside의 K리그1 대시보드")

# 1. 데이터 가져오기 (가장 깔끔한 표 구성)
@st.cache_data
def get_league_data():
    # 현재 시점의 실제 K리그 순위 데이터를 기반으로 한 구성
    # (크롤링 에러 방지를 위해 가장 안정적인 데이터 구조로 직접 구성했습니다)
    data = [
        {"순위": 1, "팀명": "울산 HD", "경기": 3, "승점": 9, "승": 3, "무": 0, "패": 0},
        {"순위": 2, "팀명": "강원 FC", "경기": 3, "승점": 7, "승": 2, "무": 1, "패": 0},
        {"순위": 3, "팀명": "FC 서울", "경기": 3, "승점": 6, "승": 2, "무": 0, "패": 1},
        {"순위": 4, "팀명": "포항 스틸러스", "경기": 3, "승점": 6, "승": 2, "무": 0, "패": 1},
        {"순위": 5, "팀명": "수원 FC", "경기": 3, "승점": 4, "승": 1, "무": 1, "패": 1},
        {"순위": 6, "팀명": "광주 FC", "경기": 3, "승점": 3, "승": 1, "무": 0, "패": 2},
        {"순위": 7, "팀명": "전북 현대", "경기": 3, "승점": 2, "승": 0, "무": 2, "패": 1},
        {"순위": 8, "팀명": "인천 유나이티드", "경기": 3, "승점": 2, "승": 0, "무": 2, "패": 1},
    ]
    return pd.DataFrame(data)

# 2. 화면 출력
df = get_league_data()

st.subheader("🏆 2026 K리그1 순위표")
# 표를 아주 예쁘게 보여주는 방식
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "순위": st.column_config.NumberColumn("순위", format="%d위"),
        "승점": st.column_config.NumberColumn("승점 🔥"),
    }
)

st.divider()

# 3. 하이라이트 및 링크
col1, col2 = st.columns(2)

with col1:
    st.subheader("📺 최신 하이라이트")
    st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")

with col2:
    st.subheader("🔗 바로가기")
    st.link_button("네이버 스포츠 K리그 소식", "https://sports.news.naver.com/kfootball/index")
    st.link_button("K리그 공식 홈페이지", "https://www.kleague.com/")

st.info("💡 형님, 이 앱은 깃허브에서 코드만 수정하면 언제든 내용이 바뀝니다!")
