import streamlit as st
import streamlit.components.v1 as components
import json

st.title("🪜 즐거운 사다리 타기")

col1, col2 = st.columns([1, 3])
with col1:
    names_input = st.text_area("이름 (쉼표)", "A,B,C,D", height=100)
    results_input = st.text_area("결과 (쉼표)", "꽝,통과,꽝,당첨", height=100)

names = [n.strip() for n in names_input.split(",")]
results = [r.strip() for r in results_input.split(",")]

if len(names) == len(results) and len(names) > 1:
    html_code = f"""
    <div style="background:#fff; padding:20px; border-radius:20px; box-shadow:0 5px 15px rgba(0,0,0,0.05);">
        <canvas id="ladderCanvas" width="700" height="450"></canvas>
        <div id="resultText" style="margin-top:20px; font-size:20px; color:#555; min-height:50px; padding:10px; border-top:1px solid #eee;"></div>
    </div>
    <script>
        const names = {json.dumps(names)};
        const results = {json.dumps(results)};
        const canvas = document.getElementById('ladderCanvas');
        const ctx = canvas.getContext('2d');
        const colors = ['#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7', '#C7CEEA', '#F3B0C3'];
        const count = names.length;
        const colWidth = 700 / (count + 1);
        const lines = [];

        for(let i=0; i<count-1; i++) {{
            for(let j=0; j<6; j++) {{
                lines.push({{col: i, y: Math.random() * 300 + 70}});
            }}
        }}

        function drawBase() {{
            ctx.clearRect(0,0,700,450);
            ctx.strokeStyle = '#ddd'; ctx.lineWidth = 3;
            names.forEach((n, i) => {{
                let x = colWidth * (i+1);
                ctx.beginPath(); ctx.moveTo(x, 60); ctx.lineTo(x, 390); ctx.stroke();
                ctx.fillStyle = "#555"; ctx.font = "bold 16px Arial";
                ctx.fillText(n, x-10, 50); ctx.fillText(results[i], x-10, 420);
            }});
            lines.forEach(l => {{
                ctx.beginPath(); ctx.moveTo(colWidth*(l.col+1), l.y);
                ctx.lineTo(colWidth*(l.col+2), l.y); ctx.stroke();
            }});
        }}

        function runLadder(idx) {{
            let currCol = idx;
            let currY = 60;
            ctx.strokeStyle = colors[idx % colors.length];
            ctx.lineWidth = 5;
            ctx.beginPath(); ctx.moveTo(colWidth*(currCol+1), currY);
            
            let sortedLines = lines.sort((a,b) => a.y - b.y);
            sortedLines.forEach(l => {{
                if(l.y > currY) {{
                    if(l.col === currCol) {{
                        ctx.lineTo(colWidth*(currCol+1), l.y);
                        ctx.lineTo(colWidth*(currCol+2), l.y);
                        currCol++; currY = l.y;
                    }} else if(l.col === currCol - 1) {{
                        ctx.lineTo(colWidth*(currCol+1), l.y);
                        ctx.lineTo(colWidth*(currCol), l.y);
                        currCol--; currY = l.y;
                    }}
                }}
            }});
            ctx.lineTo(colWidth*(currCol+1), 390); ctx.stroke();
            document.getElementById('resultText').innerHTML += `<span style="color:${{colors[idx % colors.length]}}; font-weight:bold;">${{names[idx]}}</span>: ${{results[currCol]}} | `;
        }}

        drawBase();
        // 자동 실행 버튼 대신 이름 클릭 시 애니메이션
        canvas.onclick = () => {{ drawBase(); document.getElementById('resultText').innerHTML=""; names.forEach((_, i) => runLadder(i)); }};
        setTimeout(() => {{ names.forEach((_, i) => runLadder(i)); }}, 500);
    </script>
    <p style="text-align:center; color:gray;">화면을 클릭하면 사다리를 다시 탑니다.</p>
    """
    components.html(html_code, height=600)
