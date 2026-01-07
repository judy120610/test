import streamlit as st
from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime
import requests
from io import BytesIO
import re

# --- 페이지 설정 ---
st.set_page_config(page_title="유튜브 영상 분석 마스터", page_icon="📊", layout="wide")

# --- 스타일링 ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 함수 정의 ---
def get_video_id(url):
    """유튜브 URL에서 비디오 ID 추출"""
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None

def get_video_details(youtube, video_id):
    """YouTube API를 사용하여 영상 정보 가져오기"""
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()
    
    if not response['items']:
        return None
    
    item = response['items'][0]
    snippet = item['snippet']
    stats = item['statistics']
    
    return {
        "title": snippet['title'],
        "published_at": snippet['publishedAt'],
        "thumbnail_url": snippet['thumbnails']['high']['url'],
        "view_count": int(stats.get('viewCount', 0)),
        "like_count": int(stats.get('likeCount', 0)),
        "comment_count": int(stats.get('commentCount', 0)),
        "channel_title": snippet['channelTitle']
    }

# --- 사이드바: 설정 ---
st.sidebar.title("⚙️ 설정")
api_key = st.sidebar.text_input("YouTube API Key를 입력하세요", type="password")
video_url = st.sidebar.text_input("분석할 유튜브 영상 URL", placeholder="https://www.youtube.com/watch?v=...")

# --- 메인 화면 ---
st.title("📊 YouTube 영상 정보 및 댓글 분석기")
st.info("YouTube API를 사용하여 영상의 통계와 정보를 실시간으로 가져옵니다.")

if not api_key:
    st.warning("⚠️ 왼쪽 사이드바에 API Key를 입력해 주세요.")
elif not video_url:
    st.write("👈 분석을 시작하려면 유튜브 링크를 입력하세요.")
else:
    try:
        # API 연결
        youtube = build("youtube", "v3", developerKey=api_key)
        video_id = get_video_id(video_url)
        
        if video_id:
            with st.spinner('데이터를 불러오는 중...'):
                data = get_video_details(youtube, video_id)
            
            if data:
                # 1. 썸네일 및 다운로드 버튼
                st.subheader(f"🎥 {data['title']}")
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.image(data['thumbnail_url'], use_container_width=True)
                
                with col2:
                    st.write(f"**채널명**: {data['channel_title']}")
                    # 이미지 다운로드 기능
                    response = requests.get(data['thumbnail_url'])
                    img_bytes = BytesIO(response.content)
                    st.download_button(
                        label="🖼️ 썸네일 다운로드",
                        data=img_bytes,
                        file_name=f"thumbnail_{video_id}.jpg",
                        mime="image/jpeg"
                    )

                st.divider()

                # 2. 통계 지표 (조회수, 댓글수 등)
                st.subheader("📈 주요 통계")
                m1, m2, m3 = st.columns(3)
                m1.metric("조회수", f"{data['view_count']:,}회")
                m2.metric("댓글 수", f"{data['comment_count']:,}개")
                m3.metric("좋아요 수", f"{data['like_count']:,}개")

                # 3. 상세 정보 테이블 (게시일, 댓글 수 등 요약)
                st.subheader("📅 영상 정보 요약")
                
                # 날짜 포맷팅
                pub_date = datetime.strptime(data['published_at'], "%Y-%m-%dT%H:%M:%SZ")
                formatted_date = pub_date.strftime("%Y년 %m월 %d일 %H:%M")

                summary_df = pd.DataFrame({
                    "항목": ["영상 제목", "채널명", "게시 일시", "총 조회수", "총 댓글 수"],
                    "내용": [data['title'], data['channel_title'], formatted_date, f"{data['view_count']:,}", f"{data['comment_count']:,}"]
                })
                st.table(summary_df)

            else:
                st.error("영상을 찾을 수 없습니다. URL을 확인해 주세요.")
        else:
            st.error("유효한 유튜브 URL이 아닙니다.")
            
    except Exception as e:
        st.error(f"에러 발생: {e}")

# --- 하단 정보 ---
st.caption("Powered by Streamlit & YouTube Data API v3")
