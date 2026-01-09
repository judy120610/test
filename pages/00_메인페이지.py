import streamlit as st

st.set_page_config(page_title="파스텔 미니게임 천국", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hahmlet:wght@300;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Hahmlet', serif;
        background-color: #fdfcf0; /* 부드러운 크림색 */
    }
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 60vh;
        background: linear-gradient(135deg, #fff5f5 0%, #f0f4ff 100%);
        border-radius: 30px;
        margin-top: 50px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }
    .main-title {
        font-size: 60px !important;
        font-weight: 700;
        color: #ffb7b2; /* 파스텔 핑크 */
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-title {
        font-size: 22px !important;
        color: #a2c2e1; /* 파스텔 블루 */
        font-weight: 300;
    }
    </style>
    <div class="main-container">
        <p class="main-title">즐거운 미니게임</p>
        <p class="sub-title">왼쪽 메뉴를 클릭해 미니게임을 선택하세요</p>
    </div>
    """, unsafe_allow_html=True)
