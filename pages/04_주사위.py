import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 굴러가라 주사위")

html_code = """
<style>
    .scene { width: 100px; height: 100px; perspective: 600px; margin: 80px auto; }
    .cube { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; transition: transform 1.5s cubic-bezier(0.2, 0.8, 0.3, 1.1); }
    .face { position: absolute; width: 100px; height: 100px; background: white; border: 4px solid #ffb7b2; 
            line-height: 100px; font-size: 40px; text-align: center; border-radius: 15px; color: #333; font-weight:bold; backface-visibility: visible; }
    /* 숫자 방향 정렬 */
    .f1 { transform: rotateY(0deg) translateZ(50px); }
    .f2 { transform: rotateY(90deg) translateZ(50px); }
    .f3 { transform: rotateX(90deg) translateZ(50px); }
    .f4 { transform: rotateX(-90deg) translateZ(50px); }
    .f5 { transform: rotateY(-90deg) translateZ(50px); }
    .f6 { transform: rotateY(180deg) translateZ(50px); }
</style>
<div class="scene"><div id="cube" class="cube">
    <div class="face f1">1</div><div class="face f6">6</div>
    <div class="face f3">3</div><div class="face f4">4</div>
    <div class="face f2">2</div><div class="face f5">5</div>
</div></div>
<div style="text-align:center;"><button onclick="rollDice()" style="padding:15px 30px; border-radius:10px; background:#C7CEEA; border:none; cursor:pointer; font-size:18px; font-weight:bold;">주사위 던지기</button></div>

<script>
    let currentX = 0;
    let currentY = 0;
    function rollDice() {
        const cube = document.getElementById('cube');
        // 90도의 배수로 회전시켜 숫자가 정방향으로 오게 함
        const randX = Math.floor(Math.random() * 4) * 90;
        const randY = Math.floor(Math.random() * 4) * 90;
        
        // 최소 3바퀴 이상 돌게 함 (1080도)
        currentX += 1080 + randX;
        currentY += 1080 + randY;
        
        cube.style.transform = `rotateX(${currentX}deg) rotateY(${currentY}deg)`;
    }
</script>
"""
components.html(html_code, height=400)
