import streamlit as st
import streamlit.components.v1 as components
import random
import json

st.title("🎟️ 자동 제비뽑기 상자")
st.write("상자에서 제비가 하나씩 뽑혀 나옵니다!")

c1, c2 = st.columns(2)
total = c1.number_input("총 제비 개수", 2, 50, 5)
win = c2.number_input("당첨 개수", 1, total-1, 1)

if st.button("제비 뽑기 시작!"):
    items = ["당첨 🎉"] * win + ["꽝 💀"] * (total - win)
    random.shuffle(items)
    
    html_code = f"""
    <div id="draw-container" style="text-align:center; background:#f0f2f6; padding:30px; border-radius:20px;">
        <div id="box" style="width:150px; height:150px; background:#e67e22; margin:0 auto; border-radius:10px; position:relative; border-bottom:10px solid #d35400; box-shadow:0 10px 20px rgba(0,0,0,0.2);">
            <div style="position:absolute; top:-20px; left:25px; width:100px; height:40px; background:#d35400; border-radius:5px;"></div>
        </div>
        <div id="result-area" style="margin-top:50px; min-height:100px; display:flex; flex-direction:column-reverse; align-items:center; gap:10px;"></div>
    </div>

    <script>
        const data = {json.dumps(items)};
        const resultArea = document.getElementById('result-area');
        let idx = 0;

        function drawOne() {{
            if (idx < data.length) {{
                const lot = document.createElement('div');
                lot.innerText = "???";
                lot.style = "width:200px; padding:15px; background:white; border-radius:10px; border:2px solid #e67e22; font-weight:bold; transition:all 0.5s ease-out; transform:translateY(50px); opacity:0;";
                resultArea.appendChild(lot);

                // 애니메이션 효과
                setTimeout(() => {{
                    lot.style.transform = "translateY(0)";
                    lot.style.opacity = "1";
                }}, 50);

                // 0.8초 후 결과 공개
                setTimeout(() => {{
                    lot.innerText = (idx + 1) + "번째 제비: " + data[idx];
                    if(data[idx].includes("당첨")) {{
                        lot.style.background = "#fff3cd";
                        lot.style.borderColor = "#ffc107";
                    }}
                    idx++;
                    setTimeout(drawOne, 600); // 다음 제비 뽑기
                }}, 800);
            }}
        }}
        drawOne();
    </script>
    """
    components.html(html_code, height=600, scrolling=True)
