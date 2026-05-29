import streamlit as st

st.title("🔢 구구단 대시보드")

mode = st.sidebar.radio("모드 선택", ["특정 단 보기", "전체 구구단 보기"])

if mode == "특정 단 보기":
    dan = st.selectbox("확인할 단을 선택하세요", list(range(2, 10)))
    st.subheader(f"▶ {dan}단")
    output = ""
    for j in range(1, 10):
        output += f"{dan} * {j} = {dan * j}\n"
    st.code(output, language="text")

else:
    st.subheader("▶ 전체 구구단")
    cols = st.columns(4)
    for i in range(2, 10):
        col_idx = (i - 2) % 4
        with cols[col_idx]:
            st.markdown(f"### {i}단")
            dan_output = ""
            for j in range(1, 10):
                dan_output += f"{i} * {j} = {i * j}\n"
            st.text(dan_output)