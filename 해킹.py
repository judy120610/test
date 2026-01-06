import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정 (제목 및 레이아웃)
st.set_page_config(page_title="System Security Check", layout="wide")

# Streamlit의 기본 UI 요소들을 숨기기 위한 CSS
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body {background-color: black;}
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

# 메인 애니메이션 및 로직을 담은 HTML/JS/CSS
hacking_script = """
<style>
    body { margin: 0; overflow: hidden; background: black; font-family: 'Courier New', Courier, monospace; }
    canvas { display: block; }
    
    /* 에러 메시지 스타일 */
    #error-overlay {
        position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background-color: rgba(255, 0, 0, 0.9); color: white;
        padding: 50px; border: 5px solid white; font-size: 30px; font-weight: bold;
        text-align: center; display: none; z-index: 100; box-shadow: 0 0 20px red;
    }

    /* 구글 알림창 스타일 */
    #google-alert {
        position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
        width: 400px; background: white; border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5); display: none; z-index: 101;
        font-family: 'Roboto', Arial, sans-serif; overflow: hidden;
    }
    .google-header { padding: 20px; color: #4285F4; font-size: 24px; font-weight: bold; border-bottom: 1px solid #eee; }
    .google-body { padding: 20px; color: #333; font-size: 18px; }
    .google-footer { padding: 10px; text-align: right; background: #f8f8f8; }
    .btn { color: #4285F4; font-weight: bold; cursor: pointer; margin-left: 15px; }
</style>

<canvas id="matrix"></canvas>
<div id="error-overlay">CRITICAL ERROR:<br>SYSTEM COMPROMISED</div>
<div id="google-alert">
    <div class="google-header">Google 보안 경고</div>
    <div class="google-body">
        사용자의 기기가 위험에 처해 있습니다!<br><br>
        <span style="color: red; font-weight: bold;">'해킹당하고 있습니다!'</span>
    </div>
    <div class="google-footer">
        <span class="btn">세부정보 보기</span>
        <span class="btn">확인</span>
    </div>
</div>

<script>
    const canvas = document.getElementById('matrix');
    const ctx = canvas.getContext('2d');
    const errorOverlay = document.getElementById('error-overlay');
    const googleAlert = document.getElementById('google-alert');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const fontSize = 16;
    const columns = canvas.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);

    function drawMatrix() {
        ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "#0F0";
        ctx.font = fontSize + "px monospace";

        for (let i = 0; i < drops.length; i++) {
            const text = chars[Math.floor(Math.random() * chars.length)];
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }

    let interval = setInterval(drawMatrix, 35);

    // 시나리오 제어
    setTimeout(() => {
        // 1. 5초 후 에러 메시지 등장
        errorOverlay.style.display = 'block';
        setTimeout(() => {
            // 2. 5초 후 에러 메시지 사라짐
            errorOverlay.style.display = 'none';
        }, 5000);
    }, 5000);

    setTimeout(() => {
        // 3. 15초 후 (숫자 다시 내려오다) 구글 알림창 등장
        googleAlert.style.display = 'block';
        setTimeout(() => {
            // 4. 5초 후 알림창 사라짐
            googleAlert.style.display = 'none';
        }, 5000);
    }, 15000);

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
</script>
"""

# HTML 컴포넌트 실행
components.html(hacking_script, height=1000, scrolling=False)
