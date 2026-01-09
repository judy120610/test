import streamlit as st
import random

st.set_page_config(page_title="즐거운 사다리 타기")
st.title("🪜 즐거운 사다리 타기")

names_input = st.text_input("참가자 이름을 쉼표(,)로 구분해 입력하세요", "영수,철수,미애")
results_input = st.text_input("결과 항목을 쉼표(,)로 구분해 입력하세요 (개수 일치)", "당첨,꽝,꽝")

names = [n.strip() for n in names_input.split(',') if n.strip()]
results = [r.strip() for r in results_input.split(',') if r.strip()]

if len(names) != len(results):
    st.error("이름과 결과의 개수가 같아야 합니다!")
else:
    if 'ladder_map' not in st.session_state or st.button("사다리 재구성"):
        shuffled_results = random.sample(results, len(results))
        st.session_state.ladder_map = dict(zip(names, shuffled_results))
        st.session_state.revealed = set()

    st.write("### 이름을 클릭해 결과를 확인하세요")
    cols = st.columns(len(names))
    for i, name in enumerate(names):
        if cols[i].button(name):
            st.session_state.revealed.add(name)
    
    # 개별 결과 표시
    for name in st.session_state.revealed:
        st.write(f"📍 {name} : {st.session_state.ladder_map[name]}")

    st.divider()
    if st.button("결과 한눈에 보기"):
        st.write("### 🎊 전체 결과")
        st.table(st.session_state.ladder_map)
