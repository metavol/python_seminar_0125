import streamlit as st
import numpy as np

st.title('答え合わせサイト')
st.sidebar.write("こんにちは！")
name = st.sidebar.text_input("（任意）あなたのお名前を教えてください")

if name != "":
    st.write(f"こんにちは、{name}さん！")

st.header("約数を計算します。")

n = st.text_input("整数を入力してください。")

if n == "":
    pass
elif n.isdecimal():
    n = int(n)

    yakusus = []
    for i in range(1, n+1):
        if n % i == 0:
            yakusus += [i]

    s = ' '.join([str(n) for n in yakusus])

    if len(yakusus)==2:
        st.write(f"{n}は素数です。")

    st.write(f'{n}の約数は{len(yakusus)}個あります。')
    st.write(s)
    total = np.sum(yakusus[0:-1])
    st.write(f'それ自身以外の約数の和は{total}です。')
    if total == n:
        st.write('完全数です！')

else:
    st.write("整数として認識できませんでした。")

st.header("英語の文字列を処理します。")

str = st.text_area("英文を入力してください。")

if str != "":

    ss = str.lower().replace(',','').replace(';','').replace('\n',' ').replace('\r','').split(' ')
    

    mlen = 0
    mlen_str = ""
    for s in ss:
        if mlen < len(s):
            mlen = len(s)
            mlen_str = s


    D = {}
    for s in ss:
        if s in D.keys():
            D[s] += 1
        else:
            D[s] = 1

    L = sorted(D.items(), key=lambda x:x[1], reverse=True)

    st.write(f"この文字列には{len(ss)}個の単語が含まれています。")
    st.write(f"登場する単語は{len(D)}種類です。")
    st.write(f"最長の単語は{mlen_str}で、{mlen}文字から成ります。")

    st.write("登場回数の多い順に単語を並べると、")

    for l in L:
        st.write(l[0],l[1])




