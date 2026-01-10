import streamlit as st
import streamlit.components.v1 as components
import json

st.title("🪜 두근두근 사다리 타기")

col1, col2 = st.columns([1, 3])
with col1:
    names_input = st.text_area("이름 (쉼표)", "A,B,C,D", height=100)
    names = [n.strip() for n in names_input.split(",") if n.strip()]
    
    res_mode = st.radio("결과 입력 방식", ["직접 입력", "자동 생성(당첨/꽝)"])
    if res_mode == "직접 입력":
        results_input = st.text_area("결과 (쉼표)", "꽝,통과,꽝,당첨", height=100)
        results = [r.strip() for r in results_input.split(",") if r.strip()]
    else:
        win_count = st.number_input("당첨 개수", 1, len(names) if names else 1, 1)
        results = ["당첨"] * int(win_count) + ["꽝"] * (max(0, len(names) - int(win_count)))
        import random
        random.shuffle(results)

if len(names) == len(results) and len(names) > 1:
    html_code = f"""
    <div style="background:#fff; padding:20px; border-radius:20px; box-shadow:0 5px 15px rgba(0,0,0,0.05); text-align:center;">
        <p style="color:#666; font-size:14px; margin-bottom:10px;">상단의 <b>이름을 클릭</b>하여 사다리를 내려보내세요!</p>
        <canvas id="ladderCanvas" width="700" height="450" style="background:#fff;"></canvas>
        <div id="resultArea" style="margin-top:20px; font-size:18px; color:#333; min-height:60px; padding:15px; border-top:2px solid #f0f0f0; line-height:1.6;">
            <span style="color:#999;">이름을 클릭하면 결과가 여기에 표시됩니다.</span>
        </div>
        <button onclick="resetLadder()" style="padding:10px 25px; background:#4A90E2; color:white; border:none; border-radius:10px; cursor:pointer; font-weight:bold; margin-top:10px;">전체 리셋</button>
    </div>

    <script>
        const names = {json.dumps(names)};
        const results = {json.dumps(results)};
        const canvas = document.getElementById('ladderCanvas');
        const ctx = canvas.getContext('2d');
        const colors = ['#FF6B6B', '#4D96FF', '#6BCB77', '#FFD93D', '#9966FF', '#FF9F40'];
        
        let lines = [];
        let completed = new Set(); // 사다리를 다 탄 인덱스 저장
        const colWidth = 700 / (names.length + 1);

        function initLines() {{
            lines = [];
            for(let i=0; i<names.length-1; i++) {{
                for(let j=0; j<6; j++) {{
                    lines.push({{col: i, y: Math.random() * 280 + 80}});
                }}
            }}
            lines.sort((a,b) => a.y - b.y);
        }}

        function drawBase() {{
            ctx.clearRect(0,0,700,450);
            ctx.strokeStyle = '#eee'; ctx.lineWidth = 4;
            ctx.lineCap = "round";
            
            names.forEach((n, i) => {{
                let x = colWidth * (i+1);
                // 기둥
                ctx.beginPath(); 
                ctx.strokeStyle = '#eee';
                ctx.moveTo(x, 70); ctx.lineTo(x, 380); ctx.stroke();
                
                // 이름 버튼 느낌
                ctx.fillStyle = completed.has(i) ? "#ccc" : colors[i % colors.length];
                ctx.beginPath();
                ctx.roundRect(x - 30, 20, 60, 35, 8);
                ctx.fill();
                
                ctx.fillStyle = "#fff"; ctx.font = "bold 15px Arial"; ctx.textAlign = "center";
                ctx.fillText(n, x, 43);
                
                // 결과창 (숨김 처리 했다가 완료되면 공개)
                if(completed.has(i)) {{
                    ctx.fillStyle = "#333";
                    ctx.font = "bold 15px Arial";
                    // 어떤 결과가 이 위치에 있는지 찾아야 함
                }} else {{
                    ctx.fillStyle = "#eee";
                    ctx.fillText("???", x, 410);
                }}
            }});
            
            // 사다리 가로선
            ctx.strokeStyle = '#eee'; ctx.lineWidth = 3;
            lines.forEach(l => {{
                ctx.beginPath(); ctx.moveTo(colWidth*(l.col+1), l.y);
                ctx.lineTo(colWidth*(l.col+2), l.y); ctx.stroke();
            }});
        }}

        // 특정 플레이어의 경로를 그림
        function tracePath(playerIdx) {{
            if(completed.has(playerIdx)) return;
            
            let currCol = playerIdx;
            let currY = 70;
            ctx.strokeStyle = colors[playerIdx % colors.length];
            ctx.lineWidth = 6;
            ctx.beginPath(); 
            ctx.moveTo(colWidth*(currCol+1), currY);
            
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
            ctx.lineTo(colWidth*(currCol+1), 380);
            ctx.stroke();

            // 결과 텍스트 업데이트
            completed.add(playerIdx);
            
            const resArea = document.getElementById('resultArea');
            if(completed.size === 1) resArea.innerHTML = ""; // 초기 안내문구 삭제
            
            resArea.innerHTML += `<span style="display:inline-block; margin-right:15px; background:${{colors[playerIdx % colors.length]}}; color:white; padding:2px 10px; border-radius:5px;">${{names[playerIdx]}} ➔ ${{results[currCol]}}</span> `;
            
            // 사다리 하단 결과 표시
            ctx.fillStyle = "#333";
            ctx.font = "bold 16px Arial";
            ctx.fillText(results[currCol], colWidth*(currCol+1), 410);
        }}

        canvas.addEventListener('mousedown', function(e) {{
            const rect = canvas.getBoundingClientRect();
            const mouseX = e.clientX - rect.left;
            const mouseY = e.clientY - rect.top;

            // 이름 버튼 클릭 감지
            if(mouseY >= 20 && mouseY <= 55) {{
                for(let i=0; i<names.length; i++) {{
                    let btnX = colWidth * (i+1);
                    if(mouseX >= btnX - 30 && mouseX <= btnX + 30) {{
                        tracePath(i);
                        break;
                    }}
                }}
            }}
        }});

        // 마우스 커서 변경
        canvas.addEventListener('mousemove', function(e) {{
            const rect = canvas.getBoundingClientRect();
            const mouseX = e.clientX - rect.left;
            const mouseY = e.clientY - rect.top;
            if(mouseY >= 20 && mouseY <= 55) {{
                canvas.style.cursor = "pointer";
            }} else {{
                canvas.style.cursor = "default";
            }}
        }});

        function resetLadder() {{
            completed.clear();
            document.getElementById('resultArea').innerHTML = '<span style="color:#999;">이름을 클릭하면 결과가 여기에 표시됩니다.</span>';
            initLines();
            drawBase();
        }}

        initLines();
        drawBase();
    </script>
    """
    components.html(html_code, height=650)
else:
    st.info("이름과 결과의 개수가 맞지 않거나 사람이 너무 적습니다.")
