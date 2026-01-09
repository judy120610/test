import streamlit as st

st.set_page_config(page_title="미니게임 천국", layout="wide")

# 사이드바 예쁘게 만들기 위한 CSS
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .main-title {
        font-size: 50px !important;
        font-weight: 800;
        color: #FF4B4B;
        text-align: center;
    }
    .sub-title {
        font-size: 25px !important;
        text-align: center;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">즐거운 미니게임</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">왼쪽 메뉴를 클릭해 미니게임을 선택하세요</p>', unsafe_allow_html=True)
