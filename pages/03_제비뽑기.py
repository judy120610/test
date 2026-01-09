import streamlit as st
import random

st.set_page_config(page_title="두근두근 제비뽑기")
st.title("🎟️ 두근두근 제비뽑기")

total = st.number_input("총 개수 (최대 50)", min_value=2, max_value=50, value=10)
win = st.number_input("당첨 개수", min_value=1, max_value=49, value=1)

if win >= total:
    st.error("당첨 개수는 총 개수보다 적어야 합니다.")
else:
    if st.button("뽑기 시작"):
        items = ["당첨"] * win + ["꽝"] * (total - win)
        random.shuffle(items)
        
        st.write("### 뽑기 결과")
        cols = st.columns(5)
        for i, item in enumerate(items):
            with cols[i % 5]:
                if item == "당첨":
                    st.success(f"{i+1}번: 당첨! 🎉")
                else:
                    st.info(f"{i+1}번: 꽝")
        
        st.balloons()
        winners = [i+1 for i, v in enumerate(items) if v == "당첨"]
        st.success(f"당첨 번호: {', '.join(map(str, winners))}")
