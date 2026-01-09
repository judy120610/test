import streamlit as st
import streamlit.components.v1 as components

st.title("🪙 운명의 동전 던지기")

html_code = """
<style>
    .scene { width: 150px; height: 150px; perspective: 1000px; margin: 50px auto; }
    .coin { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; transition: transform 2s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
    .side { position: absolute; width: 100%; height: 100%; border-radius: 50%; backface-visibility: hidden; 
            display: flex; flex-direction: column; align-items: center; justify-content: center; 
            border: 6px solid #bdc3c7; box-shadow: inset 0 0 20px rgba(0,0,0,0.2); }
    .heads { background: linear-gradient(145deg, #e6e6e6, #cfcfcf); color: #2c3e50; }
    .tails { background: linear-gradient(145deg, #d4d4d4, #b0b0b0); transform: rotateX(180deg); color: #2c3e50; }
    .coin-val { font-size: 40px; font-weight: bold; }
    .coin-label { font-size: 14px; }
</style>
<div class="scene">
    <div id="coin" class="coin">
        <div class="side heads">
            <div class="coin-val">100</div>
            <div class="coin-label">한국은행</div>
        </div>
        <div class="side tails">
            <div class="coin-val">👤</div>
            <div class="coin-label">이순신장군</div>
        </div>
    </div>
</div>
<div style="text-align:center;">
    <button onclick="flip()" style="padding:15px 40px; background:#FFDAC1; border:none; border-radius:15px; cursor:pointer; font-size:20px;">동전 튕기기!</button>
    <h2 id="res" style="color:#555; margin-top:30px;"></h2>
</div>
<script>
    function flip() {
        const coin = document.getElementById('coin');
        const isHeads = Math.random() < 0.5;
        // 상하 회전 (rotateX)
        const rotation = isHeads ? 1440 : 1620; 
        coin.style.transform = `rotateX(${rotation}deg)`;
        document.getElementById('res').innerText = "결과는...?";
        setTimeout(() => {
            document.getElementById('res').innerText = isHeads ? "결과: 앞면 (100)" : "결과: 뒷면 (이순신)";
        }, 2000);
    }
</script>
"""
components.html(html_code, height=500)
