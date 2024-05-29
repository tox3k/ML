import streamlit as st

with st.sidebar:
    st.image('static/logo.png', width=150, output_format='PNG')
    st.write('\n')
    st.page_link('app.py', label='Анализ МРТ снимка')
    st.page_link('./pages/discover_results.py', label='Ваша история анализов')
    st.page_link('./pages/about_us.py', label='О сервисе')