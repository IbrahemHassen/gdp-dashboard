import streamlit as st
import pickle
import pandas as pd
import math
from pathlib import Path

st.title('car co2 emssion')
f1=st.number_input('feature 1',min_value=1,max_value=10)
f2=st.number_input('feature 2',min_value=1,max_value=10)
f3=st.number_input('feature 3',min_value=1,max_value=100)

with open('model.pkl','rb')as file:
  model=pickle.load(file)


