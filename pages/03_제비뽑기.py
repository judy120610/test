import streamlit as st
import streamlit.components.v1 as components
import random
import json

st.title("🎟️ 두근두근 제비뽑기")
c1, c2 = st.columns(2)
total = c1.number_input("총 개수", 2, 50, 10)
win = c2.number_input("당첨 개수", 1, total-1, 1)

if st.button("자동 뽑기 시작"):
    items = ["당첨"] * win + ["꽝"] * (total - win)
    random.shuffle(items)
    
    html_code = f"""
    <style>
        .container {{ display: flex; flex-wrap: wrap; gap: 10px; background: #fff; padding: 20px; border-radius: 15px; }}
        .paper {{ width: 70px; height: 90px; background: #FFD1DC; border-radius: 5px; 
                  display: flex; align-items: center; justify-content: center; font-weight: bold;
                  transition: all 0.6s; border: 2px solid #ffb7b2; color: transparent; }}
        .paper.revealed {{ background: white; transform: rotateY(180deg); color: #333; border-color: #a2c2e1; }}
    </style>
    <div class="container" id="box"></div>
    <script>
        const data = {json.dumps(items)};
        const box = document.getElementById('box');
        data.forEach((v, i) => {{
            const el = document.createElement('div');
            el.className = 'paper';
            el.id = 'p' + i;
            el.innerText = v;
            box.appendChild(el);
        }});

        let idx = 0;
        function autoReveal() {{
            if(idx < data.length) {{
                document.getElementById('p' + idx).classList.add('revealed');
                idx++;
                setTimeout(autoReveal, 300);
            }}
        }}
        setTimeout(autoReveal, 500);
    </script>
    """
    components.html(html_code, height=500)
