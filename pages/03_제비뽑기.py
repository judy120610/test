import streamlit as st
import streamlit.components.v1 as components
import random
import json
elif menu == "🎟️ 제비뽑기":
    st.title("🎟️ 두근두근 제비뽑기")
    c1, c2 = st.columns(2)
    total = c1.number_input("총 개수", 2, 50, 10)
    win = c2.number_input("당첨 개수", 1, total-1, 1)

    if st.button("제비 새로 만들기"):
        items = ["당첨"] * win + ["꽝"] * (total - win)
        random.shuffle(items)
        
        html_code = f"""
        <style>
            .container {{ display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; perspective: 1000px; }}
            .paper {{ width: 80px; height: 100px; position: relative; transform-style: preserve-3d; transition: transform 0.6s; cursor: pointer; }}
            .paper.revealed {{ transform: rotateY(180deg); }}
            .face {{ position: absolute; width: 100%; height: 100%; backface-visibility: hidden; border-radius: 8px; 
                     display: flex; align-items: center; justify-content: center; font-weight: bold; border: 2px solid #ffb7b2; }}
            .front {{ background: #FFD1DC; color: #ffb7b2; font-size: 20px; }}
            .back {{ background: white; transform: rotateY(180deg); color: #333; font-size: 16px; border-color: #a2c2e1; }}
        </style>
        <div class="container" id="box"></div>
        <script>
            const data = {json.dumps(items)};
            const box = document.getElementById('box');
            data.forEach((v, i) => {{
                const card = document.createElement('div');
                card.className = 'paper';
                card.innerHTML = `<div class="face front">?</div><div class="face back">${{v}}</div>`;
                card.onclick = () => card.classList.toggle('revealed');
                box.appendChild(card);
            }});
        </script>
        """
        components.html(html_code, height=500, scrolling=True)
