import streamlit as st
import random
import time

st.set_page_config(page_title="운명의 동전 던지기")
st.title("🪙 운명의 동전 던지기")

st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("동전 던지기", use_container_width=True):
        placeholder = st.empty()
        with st.spinner("동전 튕기는 중..."):
            time.sleep(1)
            result = random.choice(["앞면 (100 숫자)", "뒷면 (이순신 장군)"])
            
            if "앞면" in result:
                placeholder.markdown("<h1 style='text-align: center; font-size: 100px;'>🪙</h1>", unsafe_allow_html=True)
            else:
                placeholder.markdown("<h1 style='text-align: center; font-size: 100px;'>👤</h1>", unsafe_allow_html=True)
            
            st.markdown(f"<h2 style='text-align: center;'>{result}!</h2>", unsafe_allow_html=True)
