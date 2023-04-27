# 以下を「app.py」に書き込み
import streamlit as st
import pandas as pd

st.title("Hello Streamlit!")

df = pd.DataFrame({"数学": [67, 76, 92, 81,57],
                   "英語": [45, 81, 93, 48, 77],
                   "理科": [65, 68, 77, 83, 91]})
st.dataframe(df)
     
