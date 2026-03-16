import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def lg(c): return f"https://www.kleague.com/assets/img/club/club_logo_{c}.png"

# K1 순위 (데이터 선언을 한 줄씩 짧게 축소)
k1 = []
k1.append([1, lg("K01"), "울산 HD", 3, 9, 3, 0, 0])
k1.append([2, lg("K03"), "강원 FC", 3, 7, 2, 1, 0])
k1.append([3, lg("K09"), "FC 서울", 3, 6, 2, 0, 1])
k1.append([4, lg("K05"), "포항 스틸러스", 3, 6, 2, 0, 1])
k1.append([5, lg("K10"), "수원 FC", 3, 4, 1, 1, 1])
k1.append([6, lg("K21"), "광주 FC", 3, 3, 1, 0, 2])
k1.append([7, lg("K07"), "전북 현대", 3, 2, 0, 2, 1])
k1.append([8, lg("K18"), "인천 유나이티드", 3, 2, 0, 2, 1])
k1.append([9, lg("K15"), "대전 하나", 3, 1, 0, 1, 2])
k1.append([10, lg("K04"), "제주 유나이티드", 3, 1, 0, 1, 2])
k1.append([11, lg("K17"), "대구 FC", 3, 1, 0, 1, 2])
k1.append([12, lg("K25"), "김천 상무", 3, 0, 0, 0, 3])
df1 = pd.DataFrame(k1, columns=["순위", "로고", "팀명", "경기수", "승점", "승", "무", "패"])

# K1 결과 (날짜 포함)
res = [
    {"일시": "03.14 14:00", "홈": "울산", "점수": "2:1", "원정": "전북", "영상": "▶️ 보기"},
    {"일시": "03.14 16:30", "홈": "서울", "점수": "0:0", "원정": "강원", "영상": "▶️ 보기"},
    {"일시": "03.15 14:00", "홈": "광주", "점수": "1:2", "원정": "포항
