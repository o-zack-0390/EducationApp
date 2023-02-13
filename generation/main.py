import streamlit as st
import importlib
import write_tfidf
import sort_tfidf
import bsg
import generate

st.markdown("## 空欄補充問題作成アプリ")

option = st.selectbox\
         ("空欄対象プログラムを選択",\
         [ "2-1.c" , "2-2.c" , "2-3.c",           \
           "3-2.c" , "3-3.c" ,                    \
           "4-1.c" , "4-2.c" , "4-3.c" ,          \
           "5-1.c" , "5-2.c" , "5-3.c" ,          \
           "6-1.c" , "6-2.c" , "6-3.c" ,          \
           "7-1.c" , "7-3.c" , "7-4.c" , "7-5.c", \
           "8-1.c" , "8-2.c" , "8-3.c" ,          \
           "9-1.c" , "9-2.c" , "9-3.c" ,          \
           "10-1.c", "10-2.c", "10-3.c",          \
           "11-1.c", "11-2.c", "11-3.c",          \
           "12-1.c", "12-2.c", "12-3.c",          \
           "13-1.c", "13-2.c", "13-3.c"           \
         ]
         )

path1 = "result/tf-idf1.txt"
path2 = "result/tf-idf2.txt"
path3 = "result/generate_note.txt"
path4 = "result/uid.txt"

if st.button("空欄補充問題を生成"):

  write_tfidf.write_tfidf(path1, path2, path3, path4, option + "\n")
  sort_tfidf.sort_tfidf(path3)

  path1 = "result/bsg1.txt"
  path2 = "result/bsg2.txt"
  path3 = "result/generate_note.txt"

  bsg.bsg(path1, path2, path3)

  path1 = "result/bsg1.txt"
  path2 = "result/bsg2.txt"
  path3 = "result/prob.c"
  path4 = "data/" + option

  generate.generate(path4, path3, path1, path2)

  importlib.reload(write_tfidf)
  importlib.reload(sort_tfidf)
  importlib.reload(bsg)
  importlib.reload(generate)