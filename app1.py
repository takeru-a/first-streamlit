import streamlit as st
import time

st.title("プレグレスバー")

st.sidebar.write("サイドバー")

'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'loading:{i+1}%')
    bar.progress(i+1)
    time.sleep(0.03)

'Done!!'

expan = st.beta_expander('問い合わせ１：授業中眠くなるのはどうしたらいいか？')
expan.write("寝なさい")
option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)

'あなたの好きな数字は、',option ,'です。'


"""
# コード
```python
import streamlit as st
import time

st.title("プレグレスバー")

st.sidebar.write("サイドバー")

'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'loading:{i+1}%')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!'

expan = st.beta_expander('問い合わせ１：授業中眠くなるのはどうしたらいいか？')
expan.write("寝なさい")
option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)

'あなたの好きな数字は、',option ,'です。'


```

"""