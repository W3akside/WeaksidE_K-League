import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def lg(c): return f"https://www.kleague.com/assets/img/club/club_logo_{c}.png"

# 스타일 함수 (가운데 정렬 + 강등권 색상)
def stl(r, is_k1=True):
    bg = ''
    if is_k1:
        if r['순위'] == 12: bg = 'rgba(255,0,0,0.4)'
        elif r['순위'] in [10, 11]: bg = 'rgba(255,0,0,0.15)'
    return [f'background-color: {bg}; text-align: center;'] * 8

# --- K리그1 데이터 ---
r1 = "03.14 14:00,울산,2:1,전북,https://youtu.be/kY0vR6z-1pY|03.14 16:30,서울,0:0,강원,https://youtu.be/kY0vR6z-1pY|03.15 14:00,광주,1:2,포항,https://youtu.be/kY0vR6z-1pY|03.15 16:30,인천,1:1,대전,https://youtu.be/kY0vR6z-1pY|03.16 19:00,수원 FC,경기전,대구,|03.16 19:30,제주,경기전,김천,"
res1 = [dict(zip(['일시','홈','점수','원정','영상'], x.split(','))) for x in r1.split('|')]

k1_data = [[1,lg("K01"),"울산 HD",3,9,3,0,0],[2,lg("K03"),"강원 FC",3,7,2,1,0],[3,lg("K09"),"FC 서울",3,6,2,0,1],[4,lg("K05"),"포항 스틸러스",3,6,2,0,1],[5,lg("K10"),"수원 FC",3,4,1,1,1],[6,lg("K21"),"광주 FC",3,3,1,0,2],[7,lg("K07"),"전북 현대",3,2,0,2,1],[8,lg("K18"),"인천 유나이티드",3,2,0,2,1],[9,lg("K15"),"대전 하나",3,1,0,1,2],[10,lg("K04"),"제주 유나이티드",3,1,0,1,2],[11,lg("K17"),"대구 FC",3,1,0,1,2],[12,lg("K25"),"김천
