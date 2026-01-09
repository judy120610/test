import streamlit as st
import streamlit.components.v1 as components

st.title("🎡 빙글빙글 돌림판")

col1, col2 = st.columns([2, 1])

with col2:
    options_text = st.text_area("선택지를 입력 (엔터 구분)", "치킨\n피자\n족발\n보쌈\n초밥")
    options = [o.strip() for o in options_text.split("\n") if o.strip()]

with col1:
    html_code = f"""
    <div id="wrapper" style="text-align:center;">
        <canvas id="wheel" width="400" height="400"></canvas>
        <br>
        <button onclick="spin()" style="padding:10px 20px; font-size:20px; cursor:pointer; background:#FF4B4B; color:white; border:none; border-radius:5px;">돌리기!</button>
        <h2 id="result" style="margin-top:20px;"></h2>
    </div>
    <script>
        const canvas = document.getElementById('wheel');
        const ctx = canvas.getContext('2d');
        const options = {list(options)};
        const colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'];
        
        let startAngle = 0;
        const arc = Math.PI / (options.length / 2);
        
        function drawWheel() {{
            options.forEach((opt, i) => {{
                const angle = startAngle + i * arc;
                ctx.fillStyle = colors[i % colors.length];
                ctx.beginPath();
                ctx.moveTo(200, 200);
                ctx.arc(200, 200, 180, angle, angle + arc, false);
                ctx.lineTo(200, 200);
                ctx.fill();
                ctx.save();
                ctx.fillStyle = "white";
                ctx.translate(200 + Math.cos(angle + arc/2) * 120, 200 + Math.sin(angle + arc/2) * 120);
                ctx.rotate(angle + arc/2 + Math.PI/2);
                ctx.fillText(opt, -ctx.measureText(opt).width/2, 0);
                ctx.restore();
            }});
        }}

        function spin() {{
            let spinAngleStart = Math.random() * 10 + 10;
            let spinTimeTotal = Math.random() * 3 + 4 * 1000;
            let spinTime = 0;
            
            function rotate() {{
                spinTime += 30;
                if (spinTime >= spinTimeTotal) {{
                    const index = Math.floor((((startAngle * 180 / Math.PI) % 360) + 360) % 360 / (360 / options.length));
                    document.getElementById('result').innerText = "결과: " + options[options.length - 1 - index];
                    return;
                }}
                const spinAngle = spinAngleStart - (spinTime / spinTimeTotal) * spinAngleStart;
                startAngle += (spinAngle * Math.PI / 180);
                drawWheel();
                requestAnimationFrame(rotate);
            }}
            rotate();
        }}
        drawWheel();
    </script>
    """
    components.html(html_code, height=600)
