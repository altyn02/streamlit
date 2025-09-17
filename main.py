import streamlit as st

st.title("과제 1: 숫자 합계 및 선택 숫자까지 합산하기")

# --- 1단계: 두 숫자 입력받기 ---
st.header("두 숫자를 입력하세요")
A = st.number_input("숫자 A 입력:", value=0, step=1)
B = st.number_input("숫자 B 입력:", value=0, step=1)

# --- 2단계: A + B 합계 출력 ---
sum_ab = A + B
st.write(f"A + B의 합은 **{sum_ab}** 입니다.")

# --- 3단계: A, B 중 하나 선택 ---
st.header("A 또는 B 중 선택하세요")
choice = st.selectbox("합산할 숫자를 선택:", ("A", "B"))

# --- 4단계: 1부터 선택된 숫자까지 모두 더한 값 출력 ---
if choice == "A":
    total_sum = sum(range(1, int(A) + 1))
else:
    total_sum = sum(range(1, int(B) + 1))

st.write(f"1부터 {choice}까지의 합은 **{total_sum}** 입니다.")
