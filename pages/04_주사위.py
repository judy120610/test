import streamlit as st
import random
import time

st.set_page_config(page_title="굴러가라 주사위")
st.title("🎲 굴러가라 주사위")

# 주사위 이모지 매핑
dice_faces = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}

st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("주사위 굴리기", use_container_width=True):
        placeholder = st.empty()
        for _ in range(10): # 애니메이션 효과
            rand_val = random.randint(1, 6)
            placeholder.markdown(f"<h1 style='text-align: center; font-size: 150px;'>{dice_faces[rand_val]}</h1>", unsafe_allow_html=True)
            time.sleep(0.1)
        
        final_val = random.randint(1, 6)
        placeholder.markdown(f"<h1 style='text-align: center; font-size: 150px; color: #FF4B4B;'>{dice_faces[final_val]}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>숫자 {final_val}이(가) 나왔습니다!</h3>", unsafe_allow_html=True)
