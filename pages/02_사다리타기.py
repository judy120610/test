import streamlit as st
import streamlit.components.v1 as components
import json

st.title("🪜 즐거운 사다리 타기")

names_input = st.text_input("이름 (쉼표 구분)", "A,B,C,D")
results_input = st.text_input("결과 (쉼표 구분)", "꽝,통과,꽝,당첨")

names = [n.strip() for n in names_input.split(",")]
results = [r.strip() for r in results_input.split(",")]

if len(names) == len(results) and len(names) > 1:
    html_code = f"""
    <canvas id="ladderCanvas" width="600" height="400" style="border:1px solid #ccc;"></canvas>
    <div id="btnArea" style="margin-top:20px;"></div>
    <div id="finalResult" style="margin-top:20px; font-weight:bold; color: blue;"></div>
    <script>
        const names = {json.dumps(names)};
        const results = {json.dumps(results)};
        const canvas = document.getElementById('ladderCanvas');
        const ctx = canvas.getContext('2d');
        const count = names.length;
        const width = 600; const height = 400;
        const colWidth = width / (count + 1);
        const lines = [];

        // 사다리 가로줄 생성
        for(let i=0; i<count-1; i++) {{
            for(let j=0; j<5; j++) {{
                lines.push({{col: i, y: Math.random() * (height-100) + 50}});
            }}
        }}

        function draw() {{
            ctx.clearRect(0,0,width,height);
            ctx.strokeStyle = '#333'; ctx.lineWidth = 2;
            for(let i=0; i<count; i++) {{
                let x = colWidth * (i+1);
                ctx.beginPath(); ctx.moveTo(x, 50); ctx.lineTo(x, 350); ctx.stroke();
                ctx.fillText(names[i], x-10, 40);
                ctx.fillText(results[i], x-10, 370);
            }}
            lines.forEach(l => {{
                ctx.beginPath();
                ctx.moveTo(colWidth*(l.col+1), l.y);
                ctx.lineTo(colWidth*(l.col+2), l.y);
                ctx.stroke();
            }});
        }}

        function trace(idx) {{
            let currCol = idx;
            let currY = 50;
            ctx.strokeStyle = 'red'; ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.moveTo(colWidth*(currCol+1), currY);
            
            let sortedLines = lines.sort((a,b) => a.y - b.y);
            sortedLines.forEach(l => {{
                if(l.col === currCol) {{
                    ctx.lineTo(colWidth*(currCol+1), l.y);
                    ctx.lineTo(colWidth*(currCol+2), l.y);
                    currCol++;
                }} else if(l.col === currCol - 1) {{
                    ctx.lineTo(colWidth*(currCol+1), l.y);
                    ctx.lineTo(colWidth*(currCol), l.y);
                    currCol--;
                }}
            }});
            ctx.lineTo(colWidth*(currCol+1), 350);
            ctx.stroke();
            alert(names[idx] + "님의 결과는: " + results[currCol]);
        }}

        const btnArea = document.getElementById('btnArea');
        names.forEach((n, i) => {{
            let btn = document.createElement('button');
            btn.innerText = n;
            btn.onclick = () => {{ draw(); trace(i); }};
            btnArea.appendChild(btn);
        }});
        
        let allBtn = document.createElement('button');
        allBtn.innerText = "한눈에 보기";
        allBtn.style.marginLeft = "20px";
        allBtn.onclick = () => {{
            document.getElementById('finalResult').innerText = "전체 결과는 알림창으로 확인하거나 개별 클릭해주세요!";
            alert("전체 사다리 생성 완료!");
        }};
        btnArea.appendChild(allBtn);

        draw();
    </script>
    """
    components.html(html_code, height=500)
