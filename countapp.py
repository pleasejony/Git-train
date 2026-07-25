import streamlit as st
if "count" not in st.session_state:
    st.session_state.count=0
if st.button("1追加"):
    st.session_state.count+=1
st.write(f"現在のカウント:{st.session_state.count}")