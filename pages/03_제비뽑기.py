import streamlit as st
import streamlit.components.v1 as components
import random

st.title("🎟️ 두근두근 제비뽑기")
total = st.number_input("총 개수", 2, 50, 10)
win = st.number_input("당첨 개수", 1, total-1, 1)

if st.button("제비 준비"):
    items = ["당첨"] * win + ["꽝"] * (total - win)
    random.shuffle(items)
    
    html_code = f"""
    <style>
        .box {{ display: flex; flex-wrap: wrap; gap: 10px; }}
        .paper {{ width: 60px; height: 80px; background: #ffd700; border: 1px solid #b8860b; 
                  cursor: pointer; display: flex; align-items: center; justify-content: center;
                  transition: transform 0.5s; font-size: 12px; font-weight: bold; }}
        .paper.open {{ transform: rotateY(180deg); background: white; }}
    </style>
    <div class="box">
        {" ".join([f'<div class="paper" onclick="this.classList.add(\'open\'); this.innerText=\'{v}\'">?</div>' for v in items])}
    </div>
    """
    components.html(html_code, height=500)
