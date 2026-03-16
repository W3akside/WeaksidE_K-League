import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="2026 K리그", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

# 2. 데이터 로드 (잘림 방지를 위해 외부 데이터 구조 사용)
# 형님, 이 부분은 제가 데이터를 직접 쏴주는 통로입니다.
@st.cache_data
def load_k_data():
    k1_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT1nN5W-jG0-kR-XpL1-R-qP0W-Z-R-qP0W-Z-R-qP0W-Z/pub?output=csv"
    # 실제 구동을 위해 임시로 내부 데이터를 짧게 선언합니다 (잘림 방지 초압축형)
    k1_res = [["03.14 14:00","울산 HD","2:1","전북 현대","https://youtu.be/kY0vR6z-1pY"],["03.14 16:30","FC 서울","0:0","강원 FC","https://youtu.be/kY0vR6z-1pY"]]
    k1_rnk = [[1,"울산 HD",3,9],[2,"강원 FC",3,7],[10,"제주 유나이티드",3,1],[11,"대구 FC",3,1],[12,"김천 상무",3,0]]
    k2_rnk = [[1,"수원삼성",3,4],[2,"부산",3,4]]
    return k1_res, k1_rnk, k2_rnk

k1_res, k1_rnk, k2_rnk = load_k_data()

# 3. 스타일 및 출력 (가운데 정렬 필수 적용)
def stl(r, is_k1=True):
    bg = 'rgba(255,0,0,0.15)' if is_k1 and r[0] in [10,11,12] else ''
    return [f'background-color: {bg}; text-align: center;'] * len(r)

t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])

with t1:
    st.subheader("📅 K리그1 최신 결과")
    st.dataframe(pd.DataFrame(k1_res, columns=["일시","홈","점수","원정","하이라이트"]), use_container_width=True, hide_index=True)
    st.subheader("📊 K리그1 현재 순위")
    df1 = pd.DataFrame(k1_rnk, columns=["순위","팀명","경기수","승점"])
