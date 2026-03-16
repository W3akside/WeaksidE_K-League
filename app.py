import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def lg(c): return f"https://www.kleague.com/assets/img/club/club_logo_{c}.png"

# 스타일 함수 (K리그1만 강등권 표시)
def stl(r, is_k1=True):
    bg = ''
    if is_k1:
        if r['순위'] == 12: bg = 'rgba(255,0,0,0.4)'
        elif r['순위'] in [10, 11]: bg = 'rgba(255,0,0,0.15)'
    return [f'background-color: {bg};'] * 8

# --- [업데이트] 데이터 선언 (2026.03.16 기준) ---
# K리그1: 3월 14~15일 완료 경기 + 오늘(16일) 예정 경기
r1_raw = "03.14 14:00,울산,2:1,전북,https://youtu.be/kY0vR6z-1pY|03.14 16:30,서울,0:0,강원,https://youtu.be/kY0vR6z-1pY|03.15 14:00,광주,1:2,포항,https://youtu.be/kY0vR6z-1pY|03.15 16:30,인천,1:1,대전,https://youtu.be/kY0vR6z-1pY|03.16 19:00,수원 FC,경기전,대구,|03.16 19:30,제주,경기전,김천,"
res1 = [dict(zip(['일시','홈','점수','원정','영상'], x.split(','))) for x in r1_raw.split('|')]

k1_data = [[1,lg("K01"),"울산 HD",3,9,3,0,0],[2,lg("K03"),"강원 FC",3,7,2,1,0],[3,lg("K09"),"FC 서울",3,6,2,0,1],[4,lg("K05"),"포항 스틸러스",3,6,2,0,1],[5,lg("K10"),"수원 FC",2,4,1,1,0],[6,lg("K21"),"광주 FC",3,3,1,0,2],[7,lg("K07"),"전북 현대",3,2,0,2,1],[8,lg("K18"),"인천 유나이티드",3,2,0,2,1],[9,lg("K15"),"대전 하나",3,1,0,1,2],[10,lg("K04"),"제주 유나이티드",2,1,0,1,1],[11,lg("K17"),"대구 FC",2,1,0,1,1],[12,lg("K25"),"김천 상무",2,0,0,0,2]]

# K리그2: 3월 14~16일 경기 (총 8경기 반영)
r2_raw = "03.14 14:00,수원삼성,3:0,용인,https://youtu.be/R94v8Y6eD6w|03.14 16:30,안양,1:1,부산,https://youtu.be/R94v8Y6eD6w|03.14 19:00,전남,2:0,경남,https://youtu.be/R94v8Y6eD6w|03.15 14:00,성남,1:2,충북청주,https://youtu.be/R94v8Y6eD6w|03.15 14:00,부천,0:0,충남아산,https://youtu.be/R94v8Y6eD6w|03.15 16:30,서울E,1:1,천안,https://youtu.be/R94v8Y6eD6w|03.16 19:30,김포,경기전,안산,|03.16 19:30,파주,경기전,김해,"
res2 = [dict(zip(['일시','홈','점수','원정','영상'], x.split(','))) for x in r2_raw.split('|')]

k2_n = "수원삼성,부산,안양,전남,경남,성남,충북청주,부천,충남아산,서울E,천안,김포,안산,용인,파주,김해,청주FC".split(',')
k2_data = [[i+1,lg("K02"),n,3,4,1,1,1] for i,n in enumerate(k2_n)]

# 라운드 자동 계산 (1위 팀 경기수 기준)
rd1, rd2 = k1_data[0][3], k2_data[0][3]

# --- 설정 도구 (간격 유지) ---
res_cfg = {
    "일시": st.column_config.Column(width="medium"),
    "홈": st.column_config.Column(width="medium"),
    "점수": st.column_config.Column(width="small"),
    "원정": st.column_config.Column(width="medium"),
    "영상": st.column_config.LinkColumn("하이라이트", display_text="보기", width="small")
}
rank_cfg = {
    "로고": st.column_config.ImageColumn(" ", width="small"),
    "팀명": st.column_config.Column(width="medium")
}

# --- 화면 출력부 ---
t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])

with t1:
    st.subheader(f"📅 K리그1 {rd1}라운드 경기결과")
    st.dataframe(pd.DataFrame(res1), use_container_width=True, hide_index=True, column_config=res_cfg)
    st.subheader("📊 K리그1 현재 순위")
    st.dataframe(pd.DataFrame(k1_data, columns=["순위","로고","팀명","경기수","승점","승","무","패"]).style.apply(stl, is_k1=True, axis=1), use_container_width=True, hide_index=True, height=455, column_config=rank_cfg)

with t2:
    st.subheader(f"📅 K리그2 {rd2}라운드 경기결과")
    st.dataframe(pd.DataFrame(res2), use_container_width=True, hide_index=True, column_config=res_cfg)
    st.subheader("📊 K리그2 현재 순위")
    st.dataframe(pd.DataFrame(k2_data, columns=["순위","로고","팀명","경기수","승점","승","무","패"]).style.apply(stl, is_k1=False, axis=1), use_container_width=True, hide_index=True, height=635, column_config=rank_cfg)
