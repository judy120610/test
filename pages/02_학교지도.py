import streamlit as st

st.set_page_config(page_title="학교 위치")

st.title("📍 찾아오시는 길")

# 주소 정보
address = "서울특별시 양천구 목동서로 300 (목동)"
st.info(f"**주소**: {address}")

# 구글 지도 임베드 (iframe 방식)
# 실제 목일중학교 위치의 구글 지도 공유 코드를 넣으면 좋습니다.
map_html = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d3164.123456789!2d126.871234567!3d37.521234567!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357c9e94364958f3%3A0xb7a646c05a11e031!2z66qp7J287KSR7ZWZ6rWQ!5e0!3m2!1sko!2skr!4v1710000000000" 
width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
"""
st.components.v1.html(map_html, height=450)

st.markdown("""
### 교통편 안내
- **지하철**: 5호선 오목교역 하차 후 도보 약 15분
- **버스**: 목일중학교 앞 정류장 (6624, 6625 등)
""")
