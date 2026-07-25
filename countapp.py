import streamlit as st
st.title("シンプルカウントツール")
if "count" not in st.session_state:
    st.session_state.count=0
if st.button("1追加"):
    st.session_state.count+=1
if st.button("1減少"):
    st.session_state.count-=1
if st.button("リセット"):
    st.session_state.count=0
st.write(f"現在のカウント:{st.session_state.count}")