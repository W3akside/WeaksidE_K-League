import streamlit as st
import pandas as pd

# 1. 설정 및 로고/스타일 함수
st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def lg(c): return f"https://www.kleague.com/assets/img/club/club_logo_{c}.png"

def stl(r, is_k1=True):
    bg = ''
    if is_k1:
        if r['순위'] == 12: bg = 'rgba(255,0,0,0.4)'
        elif r['순위'] in [10, 11]: bg = 'rgba(255,0,0,0.15)'
    return [f'background-color: {bg}; text-align: center;'] * 8

# 2. K리그1 데이터 (잘림 방지를 위해 한 줄씩 선언)
r1_list = []
r1_list.append(["03.14 14:00","울산 HD","2:1","전북 현대","https://youtu.be/kY0vR6z-1pY"])
r1_list.append(["03.14 16:30","FC 서울","0:0","강원 FC","https://youtu.be/kY0vR6z-1pY"])
r1_list.append(["03.15 14:00","광주 FC","1:2","포항 스틸러스","https://youtu.be/kY0vR6z-1pY"])
r1_list.append(["03.15 16:30","인천 유나이티드","1:1","대전 하나","https://youtu.be/kY0vR6z-1pY"])
r1_list.append(["03.16 19:00","수원 FC","경기전","대구 FC",""])
r1_list.append(["03.16 19:30","제주 유나이티드","경기전","김천 상무",""])

k1 = [
    [1,lg("K01"),"울산 HD",3,9,3,0,0],[2,lg("K03"),"강원 FC",3,7,2,1,0],
    [3,lg("K09"),"FC 서울",3,6,2,0,1],[4,lg("K05"),"포항 스틸러스",3,6,2,0,1],
    [5,lg("K10"),"수원 FC",3,4,1,1,1],[6,lg("K21"),"광주 FC",3,3,1,0,2],
    [7,lg("K07"),"전북 현대",3,2,0,2,1],[8,lg("K18"),"인천 유나이티드",3,2,0,2,1],
    [9,lg("K15"),"대전 하나",3,1,0,1,2],[10,lg("K04"),"제주 유나이티드",3,1,0,1,2],
    [11,lg("K17"),"대구 FC",3,1,0,1,2],[12,lg("K25"),"김천 상무",3,0,0,0,3]
]

# 3. K리그2 데이터 (17개 팀)
k2n = ["수원삼성","부산 아이파크","안양 FC","전남 드래곤즈","경남 FC","성남 FC","충북청주","부천 FC 1995","충남아산","서울 이랜드","천안 시티","김포 FC","안산 그리너스","용인시청","파주시민","김해시청","청주 FC"]
k2 = [[i+1,lg("K02"),n,3,4,1,1,1] for i,n in enumerate(k2n)]

# 4. 화면 출력
t1, t2 = st.tabs(["🏆 K리그1", "🥈 K리그2"])

with t1:
    st.subheader("📅 K리그1 결과")
    df_r1 = pd.DataFrame(r1_list, columns=["일시","홈","점수","원정","영상"])
    st.dataframe(df_r1.style.set_properties(**{'text-align': 'center'}), use_container_width=True, hide_index=True, column_config={"영상": st.column_config.LinkColumn("하이라이트", display_text="보기")})
    
    st.subheader("📊 K리그1 순위")
    df1 = pd.DataFrame(k1, columns=["순위","로고","팀명","경기수","승점","승","무","패"])
    st.dataframe(df1.style.apply(stl, is_k1=True, axis=1), use_container_width=True, hide_index=True, column_config={"로고": st.column_config.ImageColumn(" "), "팀명": st.column_config.Column(width="medium")})

with t2:
    st.subheader("📊 K리그2 순위")
    df2 = pd.DataFrame(k2, columns=["순위","로고","팀명","경기수","승점","승","무","패"])
    st.dataframe(df2.style.apply(stl, is_k1=False, axis=1), use_container_width=True, hide_index=True, column_config={"로고": st.column_config.ImageColumn(" "), "팀명": st.column_config.Column(width="medium")})
