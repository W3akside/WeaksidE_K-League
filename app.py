import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def lg(c): return f"https://www.kleague.com/assets/img/club/club_logo_{c}.png"

# 스타일 함수 (가운데 정렬 + 강등권 색상)
def stl(r):
    bg = 'rgba(255,0,0,0.4)' if r['순위']==12 else ('rgba(255,0,0,0.15)' if r['순위'] in [10,11] else '')
    return [f'background-color: {bg}; text-align: center;'] * 8

# --- 2. 최신 라운드 경기 데이터 확장 (K1 6경기, K2 8경기 이상) ---
r1 = "03.14 14:00,울산,2:1,전북,https://youtu.be/kY0vR6z-1pY|03.14 16:30,서울,0:0,강원,https://youtu.be/kY0vR6z-1pY|03.15 14:00,광주,1:2,포항,https://youtu.be/kY0vR6z-1pY|03.15 16:30,인천,1:1,대전,https://youtu.be/kY0vR6z-1pY|03.16 19:00,수원 FC,경기전,대구,|03.16 19:30,제주,경기전,김천,"
res1 = [dict(zip(['일시','홈','점수','원정','영상'], x.split(','))) for x in r1.split('|')]

k1_data = [[1,lg("K01"),"울산 HD",3,9,3,0,0],[2,lg("K03"),"강원 FC",3,7,2,1,0],[3,lg("K09"),"FC 서울",3,6,2,0,1],[4,lg("K05"),"포항 스틸러스",3,6,2,0,1],[5,lg("K10"),"수원 FC",3,4,1,1,1],[6,lg("K21"),"광주 FC",3,3,1,0,2],[7,lg("K07"),"전북 현대",3,2,0,2,1],[8,lg("K18"),"인천 유나이티드",3,2,0,2,1],[9,lg("K15"),"대전 하나",3,1,0,1,2],[10,lg("K04"),"제주 유나이티드",3,1,0,1,2],[11,lg("K17"),"대구 FC",3,1,0,1,2],[12,lg("K25"),"김천 상무",3,0,0,0,3]]

# K리그2 8경기 데이터 구성
r2 = "03.14 14:00,수원삼성,3:0,용인,https://youtu.be/R94v8Y6eD6w|03.14 16:30,안양,1:1,부산,https://youtu.be/R94v8Y6eD6w|03.14 19:00,전남,2:0,경남,https://youtu.be/R94v8Y6eD6w|03.15 14:00,성남,1:2,충북청주,https://youtu.be/R94v8Y6eD6w|03.15 14:00,부천,0:0,충남아산,https://youtu.be/R94v8Y6eD6w|03.15 16:30,서울E,1:1,천안,https://youtu.be/R94v8Y6eD6w|03.16 19:30,김포,경기전,안산,|03.16 19:30,파주,경기전,김해,"
res2 = [dict(zip(['일시','홈','점수','원정','영상'], x.split(','))) for x in r2.split('|')]

k2_n = "수원삼성,부산,안양,전남,경남,성남,충북청주,부천,충남아산,서울E,천안,김포,안산,용인,파주,김해,청주FC".split(',')
k2_data = [[i+1,lg("K02"),n,3,4,1,1,1] for i,n in enumerate(k2_n)]

# --- 1. 탭 명칭 수정 (K리그1, K리그2) ---
t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])

with t1:
    st.subheader("📅 K리그1 최신 결과")
    st.dataframe(pd.DataFrame(res1), use_container_width=True, hide_index=True, column_config={"영상": st.column_config.LinkColumn("하이라이트", display_text="보기")})
    st.subheader("📊 K리그1 현재 순위")
    # 3. height=None 설정으로 순위표 스크롤 제거
    st.dataframe(pd.DataFrame(k1_data, columns=["순위","로고","팀명","경기수","승점","승","무","패"]).style.apply(stl, axis=1), use_container_width=True, hide_index=True, height=None, column_config={"로고": st.column_config.ImageColumn(" "), "팀명": st.column_config.Column(width="medium")})

with t2:
    st.subheader("📅 K리그2 최신 결과")
    st.dataframe(pd.DataFrame(res2), use_container_width=True, hide_index=True, column_config={"영상": st.column_config.LinkColumn("하이라이트", display_text="보기")})
    st.subheader("📊 K리그2 현재 순위 (17개 팀)")
    # 3. height=None 설정으로 순위표 스크롤 제거
    st.dataframe(pd.DataFrame(k2_data, columns=["순위","로고","팀명","경기수","승점","승","무","패"]).style.apply(stl, axis=1), use_container_width=True, hide_index=True, height=None, column_config={"로고": st.column_config.ImageColumn(" "), "팀명": st.column_config.Column(width="medium")})
