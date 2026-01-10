import streamlit as st
import streamlit.components.v1 as components

st.title("🪙 운명의 동전 던지기")

html_code = """
<style>
    .scene { width: 120px; height: 120px; perspective: 1000px; margin: 80px auto; }
    .coin { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; transition: transform 1.5s ease-out; }
    .side { position: absolute; width: 100%; height: 100%; border-radius: 50%; backface-visibility: hidden; 
            display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: bold;
            border: 5px solid #d4af37; box-shadow: inset 0 0 15px rgba(0,0,0,0.2); }
    .heads { background: #ffd700; color: #784a06; transform: translateZ(3px); }
    .tails { background: #daa520; color: #784a06; transform: rotateX(180deg) translateZ(3px); }
    /* 동전 던지기 높이 애니메이션 */
    @keyframes toss {
        0% { bottom: 0; }
        50% { bottom: 150px; transform: scale(1.2); }
        100% { bottom: 0; }
    }
    .toss-animation { position: relative; animation: toss 1.5s ease-in-out; }
</style>
<div class="scene">
    <div id="coin-container">
        <div id="coin" class="coin">
            <div class="side heads">앞</div>
            <div class="side tails">뒤</div>
        </div>
    </div>
</div>
<div style="text-align:center;">
    <button onclick="flip()" style="padding:15px 40px; background:#FFDAC1; border:none; border-radius:15px; cursor:pointer; font-size:20px; font-weight:bold;">동전 던지기!</button>
    <h2 id="res" style="color:#555; margin-top:30px;">결과는?</h2>
</div>

<script>
    let currentRotation = 0;
    function flip() {
        const coin = document.getElementById('coin');
        const container = document.getElementById('coin-container');
        const isHeads = Math.random() < 0.5;
        
        // 애니메이션 초기화 및 재실행
        container.classList.remove('toss-animation');
        void container.offsetWidth; // reflow
        container.classList.add('toss-animation');
        
        // X축(위아래) 회전 누적
        const rotateAdd = isHeads ? 1440 : 1620;
        currentRotation += rotateAdd;
        coin.style.transform = `rotateX(${currentRotation}deg)`;
        
        document.getElementById('res').innerText = "공중에서 회전 중...";
        setTimeout(() => {
            document.getElementById('res').innerText = isHeads ? "결과: 앞면" : "결과: 뒷면";
        }, 1500);
    }
</script>
"""
components.html(html_code, height=550)
