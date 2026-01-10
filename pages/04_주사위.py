import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 정방향 주사위")

html_code = """
<style>
    .scene { width: 100px; height: 100px; perspective: 1000px; margin: 100px auto; }
    .cube { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; transition: transform 1.5s cubic-bezier(0.2, 0.8, 0.3, 1.1); }
    .face { position: absolute; width: 100px; height: 100px; background: white; border: 4px solid #333; 
            line-height: 100px; font-size: 40px; text-align: center; border-radius: 12px; font-weight: bold; color: #333; backface-visibility: hidden; }
    
    /* 각 면의 위치 설정 */
    .f1 { transform: rotateY(0deg) translateZ(50px); }
    .f6 { transform: rotateY(180deg) translateZ(50px); }
    .f3 { transform: rotateY(90deg) translateZ(50px); }
    .f4 { transform: rotateY(-90deg) translateZ(50px); }
    .f2 { transform: rotateX(-90deg) translateZ(50px); }
    .f5 { transform: rotateX(90deg) translateZ(50px); }
</style>

<div class="scene">
    <div id="cube" class="cube">
        <div class="face f1">1</div>
        <div class="face f6">6</div>
        <div class="face f3">3</div>
        <div class="face f4">4</div>
        <div class="face f2">2</div>
        <div class="face f5">5</div>
    </div>
</div>

<div style="text-align:center; margin-top:50px;">
    <button onclick="rollDice()" style="padding:15px 35px; border-radius:12px; background:#4A90E2; color:white; border:none; cursor:pointer; font-size:18px; font-weight:bold; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">주사위 굴리기</button>
</div>

<script>
    let totalX = 0;
    let totalY = 0;

    function rollDice() {
        const cube = document.getElementById('cube');
        // 1~6 사이의 결과 결정
        const result = Math.floor(Math.random() * 6) + 1;
        
        // 각 결과에 따른 정확한 회전 각도 (정방향 유지)
        const rotations = {
            1: {x: 0, y: 0},
            6: {x: 0, y: 180},
            3: {x: 0, y: -90},
            4: {x: 0, y: 90},
            2: {x: 90, y: 0},
            5: {x: -90, y: 0}
        };

        const target = rotations[result];
        
        // 회전 애니메이션을 위해 여러 바퀴(1080도)를 더해줌
        totalX = (Math.floor(totalX/360) + 3) * 360 + target.x;
        totalY = (Math.floor(totalY/360) + 3) * 360 + target.y;

        cube.style.transform = `rotateX(${totalX}deg) rotateY(${totalY}deg)`;
    }
</script>
"""
components.html(html_code, height=450)
