import streamlit as st
from PIL import Image
from streamlit.logger import update_formatter

st.title('顔画像解析アプリ')


uploaded_file = st.file_uploader("Choose an image...", type="jpeg")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Echigawa Yuki',use_column_width=True)
    st.write()