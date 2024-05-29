import services as db
import streamlit as st
#p0OCv8ahUPd0wWF7dHGfZU7d7XDg7ZbmfPbEi0CT

container = st.container()

with st.sidebar:
    st.image('static/logo.png', width=150, output_format='PNG')
    st.write('\n')
    st.page_link('app.py', label='Анализ МРТ снимка')
    st.page_link('./pages/discover_results.py', label='Ваша история анализов')
    st.page_link('./pages/about_us.py', label='О сервисе')

def show_results(code):
    res = db.get_results(code)
    if res:
        for item in res:
            container.text(f'Дата анализа: {item[2]}')
            col1, col2 = container.columns(2)
            col1.image([item[0]], caption=['Печень'], use_column_width="always")
            col2.image([item[1]], caption=['Опухоль'], use_column_width="always")
    else:
        container.info('Пользователя с таким уникальным ключом не существует, проверьте правильность введения')

with container.form('my_form'):
    st.write('Введите свой уникальный ключ')
    code = st.text_input('Ключ')
    submitted = st.form_submit_button('Найти', on_click=show_results(code))
