import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def lg(c): return f"https://www.kleague.com/assets/img/club/club_logo_{c}.png"

# K1 결과 데이터 (문자열로 압축하여 잘림 방지)
r_txt = "03.14 14:00,울산,2:1,전북,▶️|03.14 16:30,서울,0:0,강원,▶️|03.15 14:00,광주,1:2,포항,▶️|03.15 16:30,인천,1:1,대전,▶️|03.16 19:00,수원 FC,경기전,대구,-|03.16 19:30,제주,경기전,김천,-"
res = [dict(zip(['일시','홈','점수','원정','영상'], x.split(','))) for x in r_txt.split('|')]

# K1 순위 데이터 (핵심 정보 유지)
k1_d = [[1,lg("K01"),"울산 HD",3,9,3,0,0],[2,lg("K03"),"강원 FC",3,7,2,1,0],[3,lg("K09"),"FC 서울",3,6,2,0,1],[4,lg("K05"),"포항",3,6,2,0,1],[5,lg("K10"),"수원 FC",3,4,1,1,1],[6,lg("K21"),"광주 FC",3,3,1,0,2],[7,lg("K07"),"전북 현대",3,2,0,2,1],[8,lg("K18"),"인천",3,2,0,2,1],[9,lg("K15"),"대전",3,1,0,1,2],[10,lg("K04"),"제주",3,1,0,1,2],[11,lg("K17"),"대구 FC",3,1,0,1,2],[12,lg("K25"),"김천 상무",3,0,0,0,3]]
df1 = pd.DataFrame(k1_d, columns=["순위","로고","팀명","경기수","승점","승","무","패"])

# K2 데이터 (17팀)
k2_n = "수원삼성,부산,안양,전남,경남,성남,충북청주,부천,충남아산,서울E,천안,김포,안산,용인,파주,김해,청주FC".split(',')
df2 = pd.DataFrame([[i+1,lg("K02"),n,3,4,1,1,1] for i,n in enumerate(k2_n)], columns=["순위","로고","팀명","경기수","승점","승","무","패"])

def stl(r):
    bg = 'rgba(255,0,0,0.4)' if r['순위']==12 else ('rgba(255,0,0,0.15)' if r['순위'] in [10,11] else '')
    return [f'background-color: {bg}; text-align: center;'] * 8

t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])
with t1:
    st.subheader("📅 K1 3라운드 결과")
    st.dataframe(pd.DataFrame(res), use_container_width=True, hide_index=True)
    st.subheader("📊 K1 현재 순위")
    st.dataframe(df1.style.apply(stl, axis=1), use_container_width=True, hide_index=True, column_config={"로고": st.column_config.ImageColumn(" "), "팀명": st.column_config.Column(width="medium")})
with t2:
    st.subheader("📊 K2 현재 순위")
    st.dataframe(df2, use_container_width=True, hide_index=True, column_config={"로고": st.column_config.ImageColumn(" ")})
