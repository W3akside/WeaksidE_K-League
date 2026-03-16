import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 페이지 설정
st.set_page_config(page_title="W3akside K-League", page_icon="⚽", layout="wide")

st.title("⚽ W3akside의 K리그1 실시간 대시보드")
st.write("네이버 스포츠 실시간 데이터를 자동으로 가져옵니다.")

# 1. 실시간 순위 크롤링 기능
@st.cache_data(ttl=3600) # 1시간마다 데이터 새로고침
def get_k_league_ranking():
    url = "https://sports.news.naver.com/kfootball/record/index.nhn?category=kleague"
    header = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # 네이버 순위 테이블 찾기
    table = soup.find('div', {'id': 'regularGroup_table'})
    rows = table.find_all('tr')
    
    data = []
    for row in rows[1:]: # 헤더 제외
        cols = row.find_all('td')
        if len(cols) > 1:
            rank = cols[0].text.strip()
            # 팀명 찾기 (정규표현식 대신 간단하게 추출)
            team = row.find('span', {'class': 'name'}).text.strip()
            match = cols[2].text.strip()
            point = cols[3].text.strip()
            win = cols[4].text.strip()
            draw = cols[5].text.strip()
            loss = cols[6].text.strip()
            data.append([rank, team, match, point, win, draw, loss])
    
    return pd.DataFrame(data, columns=['순위', '팀명', '경기수', '승점', '승', '무', '패'])

# 2. 화면에 순위표 출력
try:
    df = get_k_league_ranking()
    st.subheader("🏆 2026 K리그1 현재 순위")
    st.table(df) # 깔끔한 표로 출력
except Exception as e:
    st.error(f"데이터를 가져오는 중 오류가 발생했습니다: {e}")

st.divider()

# 3. 하이라이트 영상
st.subheader("📺 최신 하이라이트")
# K리그 공식 유튜브나 형님이 좋아하는 영상 주소를 넣으시면 됩니다.
st.video("https://www.youtube.com/watch?v=kY0vR6z-1pY")

st.info("💡 팁: 깃허브에서 코드를 수정하면 폰에 있는 앱도 자동으로 바뀝니다!")
