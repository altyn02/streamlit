import streamlit as st

# --- Title / 제목 ---
st.title("Assignment 1 / 과제 1")

# --- Input numbers / 숫자 입력 ---
st.header("Enter two numbers / 두 숫자를 입력하세요")
A = st.text_input("Enter number A / 숫자 A 입력:", value=0, step=1)
B = st.text_input("Enter number B / 숫자 B 입력:", value=0, step=1)

# --- Sum of A + B / A+B 합계 ---
sum_ab = A + B
st.write(f"Sum of A and B is / A + B 의 합: **{sum_ab}**")

# --- Select which number / A, B 중 선택 ---
st.header("Choose a number to sum up to / 합산할 숫자 선택")
choice = st.selectbox("Select A or B / A 또는 B를 선택:", ("A", "B"))

# --- Sum from 1 to chosen number / 1부터 선택된 숫자까지의 합 ---
if choice == "A":
    total_sum = sum(range(1, int(A) + 1))
else:
    total_sum = sum(range(1, int(B) + 1))

st.write(f"Sum from 1 to {choice} is / 1부터 {choice}까지의 합: **{total_sum}**")
