import streamlit as st
st.title("シンプルカウントツール")
if "count" not in st.session_state:
    st.session_state.count=0
if st.button("1追加"):
    st.session_state.count+=1
    st.write("カウントを1増やしました")
if st.button("1減少"):
    st.session_state.count-=1
    st.write("カウントを1減らしました")
if st.button("リセット"):
    st.session_state.count=0
    st.write("カウントを0にリセットしました")
st.write(f"現在の数値:{st.session_state.count}")