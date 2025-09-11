import streamlit as st

st.title("title")
st.header("header")
st.markdown ("""
markdown
**markdown**
""")
st.write ("Hello, world!")

st.write ("Здесь была Алтынсара")
a=st.number_input("dO YOU KNOW HOW COOL I AM? RATE FROM 1 TO 10", step=1)
b=st.text_input("PLS, WRITE SOMETHING 제발")

for i in range(a):
  total+=i
  st.write((total)
