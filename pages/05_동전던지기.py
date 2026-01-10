import streamlit as st
import streamlit.components.v1 as components

st.title("🪙 운명의 동전 던지기")

html_code = """
<style>
    .scene { width: 120px; height: 120px; perspective: 1200px; margin: 100px auto; position: relative; }
    .coin { 
        width: 100%; height: 100%; position: absolute; 
        transform-style: preserve-3d; 
        transition: transform 1.5s cubic-bezier(0.1, 0.5, 0.2, 1); 
    }
    .side { 
        position: absolute; width: 100%; height: 100%; border-radius: 50%; 
        backface-visibility: hidden; display: flex; align-items: center; justify-content: center; 
        font-size: 30px; font-weight: bold; border: 4px solid #7f8c8d;
    }
    /* 회색 금속 느낌의 동전 디자인 */
    .heads { background: radial-gradient(circle, #bdc3c7, #95a5a6); color: #2c3e50; transform: translateZ(5px); }
    .tails { background: radial-gradient(circle, #ecf0f1, #bdc3c7); color: #2c3e50; transform: rotateX(180deg) translateZ(5px); }
    
    /* 옆면 두께 구현 (회전 시 직사각형처럼 보임) */
    .edge {
        position: absolute; width: 100%; height: 100%; border-radius: 50%;
        background: #7f8c8d; transform: translateZ(0);
    }

    @keyframes tossUp {
        0% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-200px) scale(1.3); }
        100% { transform: translateY(0) scale(1); }
    }
    .tossing { animation: tossUp 1.5s ease-in-out; }
</style>

<div class="scene" id="scene">
    <div id="coin" class="coin">
        <div class="edge"></div>
        <div class="side heads">앞</div>
        <div class="side tails">뒤</div>
    </div>
</div>

<div style="text-align:center; margin-top:120px;">
    <button onclick="flipCoin()" style="padding:15px 40px; background:#34495e; color:white; border:none; border-radius:15px; cursor:pointer; font-size:20px; font-weight:bold; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">동전 튕기기!</button>
    <h2 id="res" style="color:#2c3e50; margin-top:30px; font-family:sans-serif;">결과는?</h2>
</div>

<script>
    let currentRot = 0;
    function flipCoin() {
        const coin = document.getElementById('coin');
        const scene = document.getElementById('scene');
        const isHeads = Math.random() < 0.5;
        
        // 1. 물리적인 위아래 튕기기 애니메이션 적용
        scene.classList.remove('tossing');
        void scene.offsetWidth; 
        scene.classList.add('tossing');
        
        // 2. 수직(X축)으로 빠르게 회전 (타원과 직사각형 형태가 보이게 됨)
        // 최소 5바퀴 이상 회전
        const extraRot = isHeads ? 1800 : 1980; 
        currentRot += extraRot;
        
        coin.style.transform = `rotateX(${currentRot}deg)`;
        
        document.getElementById('res').innerText = "결과를 기다리는 중...";
        
        setTimeout(() => {
            document.getElementById('res').innerText = isHeads ? "결과: 앞면" : "결과: 뒷면";
        }, 1500);
    }
</script>
"""
components.html(html_code, height=600)
