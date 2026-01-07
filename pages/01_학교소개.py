import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="목일중학교 소개",
    page_icon="🏫",
    layout="wide"
)

st.title("🏫 목일중학교에 오신 것을 환영합니다")
st.subheader("꿈과 끼를 키우는 행복한 배움터")

st.image("https://via.placeholder.com/800x400.png?text=Mok-il+Middle+School+Main+Image") # 학교 관련 이미지 URL로 변경 가능

st.markdown("""
### 학교 소개
목일중학교는 학생들이 바른 인성과 실력을 갖춘 인재로 성장할 수 있도록 돕습니다.

- **교훈**: 바른 마음, 밝은 지혜
- **상징**: 목련 (교화), 은행나무 (교목)
- **주요 활동**: 다양한 동아리 활동 및 학생 중심 수업
""")

st.sidebar.success("위의 메뉴에서 페이지를 선택하세요.")
