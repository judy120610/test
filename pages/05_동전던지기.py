import streamlit as st
import streamlit.components.v1 as components

st.title("🪙 운명의 동전 던지기")

html_code = """
<style>
    .coin { width: 150px; height: 150px; position: relative; transform-style: preserve-3d; margin: 50px auto; transition: transform 2s; }
    .side { position: absolute; width: 100%; height: 100%; border-radius: 50%; backface-visibility: hidden; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: bold; border: 5px solid #aaa; }
    .heads { background: #ddd; transform: rotateY(0deg); } /* 앞면 */
    .tails { background: #bbb; transform: rotateY(180deg); } /* 뒷면 */
    .coin-img { width: 130px; border-radius: 50%; }
</style>
<div id="coin" class="coin">
    <div class="side heads">
        <img src="https://upload.wikimedia.org/wikipedia/ko/c/c7/100_won_coin_obverse.png" class="coin-img">
    </div>
    <div class="side tails">
        <img src="https://upload.wikimedia.org/wikipedia/ko/e/e0/100_won_coin_reverse.png" class="coin-img">
    </div>
</div>
<div style="text-align:center;">
    <button onclick="flipCoin()" style="padding:10px 20px; font-size:20px;">던지기!</button>
    <h2 id="coinRes"></h2>
</div>
<script>
    function flipCoin() {
        const coin = document.getElementById('coin');
        const isHeads = Math.random() < 0.5;
        const rotate = isHeads ? 1800 : 1980; // 360 * 5 + (0 or 180)
        coin.style.transform = `rotateY(${rotate}deg)`;
        setTimeout(() => {
            document.getElementById('coinRes').innerText = isHeads ? "앞면입니다!" : "뒷면입니다!";
        }, 2000);
    }
</script>
"""
components.html(html_code, height=500)
