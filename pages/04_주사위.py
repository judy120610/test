import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 굴러가라 주사위")

html_code = """
<style>
    .scene { width: 100px; height: 100px; perspective: 600px; margin: 50px auto; }
    .cube { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; transition: transform 2s; }
    .face { position: absolute; width: 100px; height: 100px; background: white; border: 2px solid #ccc; line-height: 100px; font-size: 40px; text-align: center; font-weight: bold; }
    .front  { transform: rotateY(0deg) translateZ(50px); }
    .back   { transform: rotateY(180deg) translateZ(50px); }
    .right  { transform: rotateY(90deg) translateZ(50px); }
    .left   { transform: rotateY(-90deg) translateZ(50px); }
    .top    { transform: rotateX(90deg) translateZ(50px); }
    .bottom { transform: rotateX(-90deg) translateZ(50px); }
</style>
<div class="scene">
    <div id="cube" class="cube">
        <div class="face front">1</div>
        <div class="face back">6</div>
        <div class="face right">3</div>
        <div class="face left">4</div>
        <div class="face top">2</div>
        <div class="face bottom">5</div>
    </div>
</div>
<div style="text-align:center;">
    <button onclick="rollDice()" style="padding:10px 20px; font-size:20px;">던지기!</button>
</div>
<script>
    function rollDice() {
        const cube = document.getElementById('cube');
        const xRand = Math.floor(Math.random() * 4) * 90 + 720;
        const yRand = Math.floor(Math.random() * 4) * 90 + 720;
        cube.style.transform = `rotateX(${xRand}deg) rotateY(${yRand}deg)`;
    }
</script>
"""
components.html(html_code, height=400)
