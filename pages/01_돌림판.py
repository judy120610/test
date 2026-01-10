import streamlit as st
import streamlit.components.v1 as components

st.title("🎡 빙글빙글 돌림판")

col1, col2 = st.columns([2, 1])

with col2:
    options_text = st.text_area("선택지를 입력 (엔터 구분)", "치킨\n피자\n족발\n보쌈\n초밥")
    options = [o.strip() for o in options_text.split("\n") if o.strip()]

with col1:
    # 파이썬 리스트를 자바스크립트 배열 형태로 변환
    import json
    options_json = json.dumps(options)

    html_code = f"""
    <div id="wrapper" style="text-align:center; position:relative;">
        <canvas id="wheel" width="400" height="400"></canvas>
        <br>
        <button onclick="spin()" style="padding:15px 30px; font-size:20px; cursor:pointer; background:#FF4B4B; color:white; border:none; border-radius:10px; font-weight:bold; margin-top:10px;">돌리기!</button>
        <h2 id="result" style="margin-top:20px; color:#333;"></h2>
    </div>
    <script>
        const canvas = document.getElementById('wheel');
        const ctx = canvas.getContext('2d');
        const options = {options_json};
        const colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'];
        
        let startAngle = 0;
        const arc = Math.PI / (options.length / 2);
        
        function drawWheel() {{
            // 1. 캔버스 초기화 (프레임 갱신 시 필수)
            ctx.clearRect(0, 0, 400, 400);

            // 2. 판 그리기
            options.forEach((opt, i) => {{
                const angle = startAngle + i * arc;
                ctx.fillStyle = colors[i % colors.length];
                ctx.beginPath();
                ctx.moveTo(200, 200);
                ctx.arc(200, 200, 180, angle, angle + arc, false);
                ctx.lineTo(200, 200);
                ctx.fill();
                
                // 테두리
                ctx.strokeStyle = "rgba(255,255,255,0.5)";
                ctx.lineWidth = 2;
                ctx.stroke();

                // 텍스트 그리기
                ctx.save();
                ctx.fillStyle = "white";
                ctx.font = "bold 16px Arial";
                ctx.translate(200 + Math.cos(angle + arc/2) * 120, 200 + Math.sin(angle + arc/2) * 120);
                ctx.rotate(angle + arc/2);
                ctx.fillText(opt, -ctx.measureText(opt).width / 2, 5);
                ctx.restore();
            }});

            // 3. 바늘(Pointer) 그리기 - 3시 방향 (결과 계산 기준점)
            drawNeedle();
        }}

        function drawNeedle() {{
            ctx.fillStyle = "#333";
            ctx.beginPath();
            // 바늘 몸체(삼각형)
            ctx.moveTo(400, 200);      // 끝점
            ctx.lineTo(370, 185);     // 위
            ctx.lineTo(370, 215);     // 아래
            ctx.fill();
            
            // 바늘 장식 (원형)
            ctx.beginPath();
            ctx.arc(385, 200, 5, 0, Math.PI * 2);
            ctx.fillStyle = "white";
            ctx.fill();
        }}

        function spin() {{
            let spinAngleStart = Math.random() * 10 + 10;
            let spinTimeTotal = Math.random() * 3 + 4 * 1000;
            let spinTime = 0;
            
            function rotate() {{
                spinTime += 30;
                if (spinTime >= spinTimeTotal) {{
                    // 기존 결과 계산 로직 유지
                    const index = Math.floor((((startAngle * 180 / Math.PI) % 360) + 360) % 360 / (360 / options.length));
                    const winner = options[options.length - 1 - index];
                    document.getElementById('result').innerText = "결과: " + winner;
                    return;
                }}
                const spinAngle = spinAngleStart - (spinTime / spinTimeTotal) * spinAngleStart;
                startAngle += (spinAngle * Math.PI / 180);
                drawWheel();
                requestAnimationFrame(rotate);
            }}
            rotate();
        }}
        
        // 초기 실행
        drawWheel();
    </script>
    """
    components.html(html_code, height=600)
