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

con1 = st.container()
for col in con1.columns([1, 2, 3, 4], border=True):
    col.write("Hello World!")

con2 = st.container(height=100)
cc2_1, cc2_2, cc2_3, cc2_4 = con2.columns(4)
cc2_1.write("Column 5 @ Container 2")
cc2_2.write("Column 6 @ Container 2")
cc2_3.write("Column 7 @ Container 2")
cc2_4.write("Column 8 @ Container 2")