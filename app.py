# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z9byPMzrrblqrmqO4d-_xA6NyG2o6IE3
"""

import streamlit as st
import random

st.set_page_config(layout="wide")
st.title('Test Streamlit')

with st.container():
    st.write("MMMMMMM")

container = st.container(border=True)
container.write("NNNNNNN")
container.write("TUI")

container = st.container(border=True)
container.write("NATTHAKORN")