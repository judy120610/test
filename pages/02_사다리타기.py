import streamlit as st
import streamlit.components.v1 as components
import random
import json
if menu == "🪜 사다리 타기":
    st.title("🪜 즐거운 사다리 타기")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        names_input = st.text_area("이름 (쉼표로 구분)", "A,B,C,D", height=100)
        res_mode = st.radio("결과 입력 방식", ["직접 입력", "자동 생성(당첨/꽝)"])
        
        if res_mode == "직접 입력":
            results_input = st.text_area("결과 (쉼표로 구분)", "꽝,통과,꽝,당첨", height=100)
        else:
            win_count = st.number_input("당첨 개수", 1, 10, 1)
            results_input = ",".join(["당첨"] * win_count + ["꽝"] * (len(names_input.split(",")) - win_count))

    names = [n.strip() for n in names_input.split(",") if n.strip()]
    results = [r.strip() for r in results_input.split(",") if r.strip()]

    if len(names) != len(results):
        st.warning(f"이름({len(names)}개)과 결과({len(results)}개)의 개수를 맞춰주세요!")
    elif len(names) > 1:
        html_code = f"""
        <div id="ladder-container" style="background:#fff; padding:20px; border-radius:20px; box-shadow:0 5px 15px rgba(0,0,0,0.05); text-align:center;">
            <canvas id="ladderCanvas" width="700" height="450" style="cursor:pointer;"></canvas>
            <div id="resultText" style="margin-top:20px; font-size:18px; color:#555; min-height:60px; padding:10px; border-top:1px solid #eee; line-height:1.6;"></div>
            <button onclick="resetAndDraw()" style="padding:10px 20px; background:#ffb7b2; border:none; border-radius:10px; cursor:pointer; font-weight:bold;">다시 시작</button>
        </div>
        <script>
            const names = {json.dumps(names)};
            const results = {json.dumps(results)};
            const canvas = document.getElementById('ladderCanvas');
            const ctx = canvas.getContext('2d');
            const colors = ['#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7', '#C7CEEA', '#F3B0C3'];
            let lines = [];

            function initLines() {{
                lines = [];
                for(let i=0; i<names.length-1; i++) {{
                    for(let j=0; j<6; j++) {{
                        lines.push({{col: i, y: Math.random() * 300 + 70}});
                    }}
                }}
                lines.sort((a,b) => a.y - b.y);
            }}

            function drawBase() {{
                ctx.clearRect(0,0,700,450);
                const colWidth = 700 / (names.length + 1);
                ctx.strokeStyle = '#ddd'; ctx.lineWidth = 3;
                names.forEach((n, i) => {{
                    let x = colWidth * (i+1);
                    ctx.beginPath(); ctx.moveTo(x, 60); ctx.lineTo(x, 390); ctx.stroke();
                    ctx.fillStyle = "#333"; ctx.font = "bold 14px Arial"; ctx.textAlign = "center";
                    ctx.fillText(n, x, 50); ctx.fillText(results[i], x, 420);
                }});
                lines.forEach(l => {{
                    ctx.beginPath(); ctx.moveTo(colWidth*(l.col+1), l.y);
                    ctx.lineTo(colWidth*(l.col+2), l.y); ctx.stroke();
                }});
            }}

            function runLadder() {{
                document.getElementById('resultText').innerHTML = "결과 계산 중...";
                const colWidth = 700 / (names.length + 1);
                let finalRes = "";
                
                names.forEach((_, idx) => {{
                    let currCol = idx;
                    ctx.strokeStyle = colors[idx % colors.length];
                    ctx.lineWidth = 5;
                    ctx.beginPath(); ctx.moveTo(colWidth*(currCol+1), 60);
                    
                    let currY = 60;
                    lines.forEach(l => {{
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
                    finalRes += `<span style="color:${{colors[idx % colors.length]}}; font-weight:bold;">${{names[idx]}}</span>: ${{results[currCol]}} | `;
                }});
                document.getElementById('resultText').innerHTML = finalRes;
            }}

            function resetAndDraw() {{
                initLines();
                drawBase();
                document.getElementById('resultText').innerHTML = "화면을 클릭하면 사다리를 탑니다.";
            }}

            canvas.onclick = () => {{ drawBase(); runLadder(); }};
            resetAndDraw();
        </script>
        """
        components.html(html_code, height=650)
