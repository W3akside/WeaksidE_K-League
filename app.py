import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def lg(c): return f"https://www.kleague.com/assets/img/club/club_logo_{c}.png"

def stl(r, is_k1=True):
    bg = ''
    if is_k1:
        if r['순위'] == 12: bg = 'rgba(255,0,0,0.4)'
        elif r['순위'] in [10, 11]: bg = 'rgba(255,0,0,0.15)'
    return [f'background-color: {bg}; text-align: center;'] * 8
    r1 = []
r1.append(["03.14 14:00","울산 HD","2:1","전북 현대","https://youtu.be/kY0vR6z-1pY"])
r1.append(["03.14 16:30","FC 서울","0:0","강원 FC","https://youtu.be/kY0vR6z-1pY"])
r1.append(["03.15 14:00","광주 FC","1:2","포항 스틸러스","https://youtu.be/kY0vR6z-1pY"])
r1.append(["03.15 16:30","인천 유나이티드","1:1","대전 하나","https://youtu.be/kY0vR6z-1pY"])
r1.append(["03.16 19:00","수원 FC","경기전","대구 FC",""])
r1.append(["03.16 19:30","제주 유나이티드","경기전","김천 상무",""])
k1 = []
k1.append([1,lg("K01"),"울산 HD",3,9,3,0,0])
k1.append([2,lg("K05"),"포항 스틸러스",3,7,2,1,0])
k1.append([3,lg("K03"),"강원 FC",3,7,2,1,0])
k1.append([4,lg("K09"),"FC 서울",3,6,2,0,1])
k1.append([5,lg("K10"),"수원 FC",3,4,1,1,1])
k1.append([6,lg("K21"),"광주 FC",3,3,1,0,2])
k1.append([7,lg("K07"),"전북 현대",3,2,0,2,1])
k1.append([8,lg("K18"),"인천 유나이티드",3,2,0,2,1])
k1.append([9,lg("K15"),"대전 하나",3,1,0,1,2])
k1.append([10,lg("K04"),"제주 유나이티드",3,1,0,1,2])
k1.append([11,lg("K17"),"대구 FC",3,1,0,1,2])
k1.append([12,lg("K25"),"김천 상무",3,0,0,0,3])
t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])
with t1:
    st.subheader("📅 K리그1 최신 결과")
    df_r1 = pd.DataFrame(r1, columns=["일시","홈","점수","원정","영상"])
    st.dataframe(df_r1.style.set_properties(**{'text-align': 'center'}), use_container_width=True, hide_index=True, column_config={"영상": st.column_config.LinkColumn("보기")})
    st.subheader("📊 K리그1 현재 순위")
    df1 = pd.DataFrame(k1, columns=["순위","로고","팀명","경기수","승점","승","무","패"])
    st.dataframe(df1.style.apply(stl, axis=1), use_container_width=True, hide_index=True, column_config={"로고": st.column_config.ImageColumn(" "), "팀명": st.column_config.Column(width="medium")})
with t2:
    st.info("K리그2 데이터는 업데이트 중입니다.")
