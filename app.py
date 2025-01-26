# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z9byPMzrrblqrmqO4d-_xA6NyG2o6IE3
"""

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title('Test Streamlit')

result1 = st.button("click me1!")
if result1:
    st.write('you click on 1')

result2 = st.button("click me2!", type="tertiary")
if result1 & result2:
    st.write('you click both')

st.button("Reset", type="primary")