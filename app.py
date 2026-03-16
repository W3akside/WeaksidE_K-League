import streamlit as st
import pandas as pd

# 1. 초기 설정
st.set_page_config(page_title="2026 KLeague", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

# 스타일 설정 (가운데 정렬)
def stl(r):
    bg = ''
    if r['순위'] == 12: bg = 'rgba(255,0,0,0.4)'
    elif r['순위'] in [10, 11]: bg = 'rgba(255,0,0,0.15)'
    return [f'background-color: {bg}; text-align: center;'] * 8

# 2. 최신 경기 결과 (한 줄씩 짧게 입력)
res = []
res.append(["03.14", "울산", "2:1", "전북", "Link"])
res.append(["03.14", "서울", "0:0", "강원", "Link"])
res.append(["03.15", "광주", "1:2", "포항", "Link"])
res.append(["03.15", "인천", "1:1", "대전", "Link"])
res.append(["03.16", "수원F", "경기전", "대구", "- "])
res.append(["03.16", "제주", "경기전", "김천", "- "])

# 3. K리그1 순위 데이터 (끊기지 않게 쪼개서 선언)
k1 = []
k1.append([1, "울산 HD", 3, 9, 3, 0, 0])
k1.append([2, "포항", 3, 7, 2, 1, 0])
k1.append([3, "강원", 3, 7, 2, 1, 0])
k1.append([4, "서울", 3, 6, 2, 0, 1])
k1.append([5, "수원F", 3, 4, 1, 1, 1])
k1.append([6, "광주", 3, 3, 1, 0, 2])
k1.append([7, "전북", 3, 2, 0, 2, 1])
k1.append([8, "인천", 3, 2, 0, 2, 1])
k1.append([9, "대전", 3, 1, 0, 1, 2])
k1.append([10, "제주", 3, 1, 0, 1, 2])
k1.append([11, "대구", 3, 1, 0, 1, 2])
k1.append([12, "김천", 3, 0, 0, 0,
