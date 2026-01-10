import streamlit as st
import streamlit.components.v1 as components

elif menu == "🎲 주사위 굴리기":
    st.title("🎲 굴러가라 주사위")
    html_code = """
    <style>
        .scene { width: 100px; height: 100px; perspective: 600px; margin: 80px auto; }
        .cube { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; transition: transform 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .face { position: absolute; width: 100px; height: 100px; background: white; border: 4px solid #ffb7b2; 
                line-height: 100px; font-size: 40px; text-align: center; border-radius: 15px; backface-visibility: initial; color: #333; }
        .f1 { transform: rotateY(0deg) translateZ(50px); }
        .f6 { transform: rotateY(180deg) translateZ(50px); }
        .f3 { transform: rotateY(90deg) translateZ(50px); }
        .f4 { transform: rotateY(-90deg) translateZ(50px); }
        .f2 { transform: rotateX(90deg) translateZ(50px); }
        .f5 { transform: rotateX(-90deg) translateZ(50px); }
    </style>
    <div class="scene"><div id="cube" class="cube">
        <div class="face f1">1</div><div class="face f6">6</div>
        <div class="face f3">3</div><div class="face f4">4</div>
        <div class="face f2">2</div><div class="face f5">5</div>
    </div></div>
    <div style="text-align:center;"><button onclick="roll()" style="padding:15px 30px; border-radius:10px; background:#C7CEEA; border:none; cursor:pointer; font-size:18px; font-weight:bold;">주사위 던지기</button></div>
    <script>
        let currentX = 0;
        let currentY = 0;
        function roll() {
            const cube = document.getElementById('cube');
            // 이전 회전값에 누적하여 매번 애니메이션이 실행되도록 함
            currentX += 900 + Math.floor(Math.random() * 4) * 90;
            currentY += 900 + Math.floor(Math.random() * 4) * 90;
            cube.style.transform = `rotateX(${currentX}deg) rotateY(${currentY}deg)`;
        }
    </script>
    """
    components.html(html_code, height=400)
