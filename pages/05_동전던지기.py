import streamlit as st
import streamlit.components.v1 as components

st.title("🪙 운명의 동전 던지기")

html_code = """
<style>
    .scene { width: 150px; height: 150px; perspective: 1000px; margin: 50px auto; }
    .coin { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; transition: transform 2s cubic-bezier(0.2, 0.8, 0.3, 1.1); }
    .side { position: absolute; width: 100%; height: 100%; border-radius: 50%; backface-visibility: hidden; 
            display: flex; flex-direction: column; align-items: center; justify-content: center; 
            border: 4px solid #bdc3c7; box-shadow: inset 0 0 20px rgba(0,0,0,0.1); }
    .heads { background: linear-gradient(145deg, #e6e6e6, #cfcfcf); color: #2c3e50; transform: translateZ(4px); }
    .tails { background: linear-gradient(145deg, #d4d4d4, #b0b0b0); transform: rotateY(180deg) translateZ(4px); color: #2c3e50; }
    /* 두께를 위한 테두리 */
    .coin::before { content: ''; position: absolute; width: 100%; height: 100%; border-radius: 50%; background: #95a5a6; transform: translateZ(0); }
    .coin-val { font-size: 40px; font-weight: bold; }
</style>
<div class="scene">
    <div id="coin" class="coin">
        <div class="side heads"><div class="coin-val">100</div><div>한국은행</div></div>
        <div class="side tails"><div class="coin-val">👤</div><div>이순신</div></div>
    </div>
</div>
<div style="text-align:center;">
    <button onclick="flipCoin()" style="padding:15px 40px; background:#FFDAC1; border:none; border-radius:15px; cursor:pointer; font-size:20px; font-weight:bold;">동전 튕기기!</button>
    <h2 id="resText" style="color:#555; margin-top:30px;">준비...</h2>
</div>
<script>
    let currentRot = 0;
    function flipCoin() {
        const coin = document.getElementById('coin');
        const isHeads = Math.random() < 0.5;
        const addRot = isHeads ? 1440 : 1620; 
        currentRot += addRot;
        
        coin.style.transform = `rotateY(${currentRot}deg)`;
        document.getElementById('resText').innerText = "결과는...?";
        
        setTimeout(() => {
            document.getElementById('resText').innerText = isHeads ? "결과: 앞면 (100)" : "결과: 뒷면 (이순신)";
        }, 2000);
    }
</script>
"""
components.html(html_code, height=500)
