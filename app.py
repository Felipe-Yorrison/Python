import streamlit as st 

import streamlit as st 
#Exibição de dados

import pandas as pd 
import numpy as np 

df =pd.DataFrame(
np.random.rand(10, 4),
columns=['Preço', 'Taxa de ocupação', 'Taxa de inadimplência', 'Pessoas por casa']
)

st.line_chart(df)

