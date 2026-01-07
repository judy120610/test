import streamlit as st

st.set_page_config(page_title="학교 지도")

st.title("🗺️ 학교 시설 안내")

st.write("학교의 전체적인 배치와 주요 시설입니다.")

# 학교 배치도 이미지 (실제 이미지 파일이 있다면 "school_map.jpg" 등으로 변경)
st.image("https://via.placeholder.com/700x500.png?text=School+Layout+Map", caption="목일중학교 시설 배치도")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### [본관]
    - 1층: 행정실, 교장실
    - 2층: 교무실, 3학년 교실
    - 3층: 2학년 교실
    """)

with col2:
    st.markdown("""
    #### [별관 및 체육시설]
    - 강당: 실내 체육 활동
    - 급식실: 즐거운 점심 시간
    - 도서관: 독서 및 자습 공간
    """)
