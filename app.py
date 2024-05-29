import streamlit as st
import pandas as pd
import numpy as np
from main import main

nii_input = st.file_uploader('Выберите файл МРТ снимка:', type=['nii'])

def analyze():
    with open('temp_file.nii', 'wb') as f:
        f.write(nii_input.read())
    
    main('liver_102.nii')
    
    st.image(['liver.png', 'tumor.png'], caption=['Печень', 'Опухоль'])



bt = st.button('Обработать снимок', on_click=analyze)

