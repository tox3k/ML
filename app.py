import streamlit as st
import pandas as pd
import numpy as np
from main import main
import time
import random
import services as db

container = st.container()
nii_input = container.file_uploader('Выберите файл МРТ снимка:', type=['nii'])
container.text('Если у вас уже есть уникальный код, обязательно введите его')
code_input = container.text_input('Код')

with st.sidebar:
    st.image('static/logo.png', width=150, output_format='PNG')
    st.write('\n')
    st.page_link('app.py', label='Анализ МРТ снимка')
    st.page_link('./pages/discover_results.py', label='Ваша история анализов')
    st.page_link('./pages/about_us.py', label='О сервисе')


def err():
    st.error("Ошибка файла. Убедитесь что загружаете корректный файл!")

def analyze():
    if code_input:
        if len(code_input) != 40:
            container.error('Код введён неверно! Проверьте правильность или очистите поле ввода.')
            return
        code = code_input
        
    else:
        code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=40))
        while db.is_code_in_db(code) != 0:
            code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=40))
        container.write('Ваш уникальный код: ' + code)
        
    try:
        with open('temp_file.nii', 'wb') as f:
            f.write(nii_input.read())
        
        main('temp_file.nii')
            
        col1, col2 = container.columns(2)
        liver = col1.image(['liver.png'], caption=['Печень'], use_column_width="always")
        tumor = col2.image(['tumor.png'], caption=['Опухоль'], use_column_width="always")

        
         
        db.add_results(code)
        container.write('Никогда не передавайте секретный код третьим лицам!')
    except Exception as e:
        print(e.with_traceback())
        err()
    





bt = container.button('Обработать снимок', on_click=analyze)

