import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 K-League", layout="wide")
st.title("⚽ 2026 K리그 실시간 대시보드")

def lg(cid):
    return f"https://www.kleague.com/assets/img/club/club_logo_{cid}.png"

# --- K리그1 순위 데이터 ---
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
k1.append([12, lg("K25"), "김천 상무", 3, 0, 0,
