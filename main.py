import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('お試しPythonプログラム')
st.sidebar.write("こんにちは！")
name = st.sidebar.text_input("あなたのお名前を教えてください")

st.header("約数を計算します。")

if name != "":
    st.write(name+"さん")
n = st.text_input("整数を入力してください")

if n.isdecimal():
    n = int(n)

    yakusus = []
    for i in range(1, n+1):
        if n % i == 0:
            yakusus += [i]

    s = ' '.join([str(n) for n in yakusus])

    st.write(f'{n}の約数は{len(yakusus)}個あります。')
    st.write(s)
    total = np.sum(yakusus[0:-1])
    st.write(f'それ自身以外の約数の和は{total}です。')
    if total == n:
        st.write('完全数です！')


st.header("おもしろい図形を描画します。")

n = st.text_input("整数1を入力してください(例 201)") # 200
M = st.text_input("整数2を入力してください(例 4)") # 2

if n.isdecimal() and M.isdecimal():
    n = int(n)
    M = int(M)

    xx=[]
    yy=[]
    for i in range(n):
        th = 2 * np.pi / n * i
        th = - th + np.pi/2
        xx += [np.cos(th)]
        yy += [np.sin(th)]

    print(n, M)
    fig,ax = plt.subplots()

    for i in range(n):
        j = (i + 1) % n
        ax.plot([xx[i],xx[j]],[yy[i],yy[j]],c='black')

    for i in range(n):
        j = (i * M) % n
        ax.plot([xx[i],xx[j]],[yy[i],yy[j]],c='blue')

    ax.set_aspect('equal')
    st.pyplot(fig)

