import streamlit as st
import random
import plotly.graph_objects as go
import time

st.set_page_config(page_title="빙글빙글 돌림판")
st.title("🎡 빙글빙글 돌림판")

col1, col2 = st.columns([2, 1])

with col2:
    options_input = st.text_area("선택지를 입력하세요 (엔터로 구분)", "치킨\n피자\n떡볶이\n마라탕")
    options = [opt.strip() for opt in options_input.split('\n') if opt.strip()]
    spin_button = st.button("돌리기!")

with col1:
    if options:
        # 돌림판 시각화
        fig = go.Figure(data=[go.Pie(labels=options, values=[1]*len(options), hole=.3)])
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        if spin_button:
            with st.spinner('돌아가는 중...'):
                time.sleep(1)
                winner = random.choice(options)
                st.balloons()
                st.success(f"결과: ✨ {winner} ✨")
    else:
        st.warning("선택지를 입력해주세요.")
