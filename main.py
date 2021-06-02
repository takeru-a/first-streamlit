import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
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




left, right = st.beta_columns(2)
btn = left.button("右に表示")
if btn==True:
    right.write("Yheeeee!")

expan = st.beta_expander('問い合わせ１：性欲を抑えるためにはどうしたいか？')
expan.write("avを見なさい")

#text = st.text_input("あなたの趣味は？")
#'あなたの趣味:',text
#sidebar->サイドバーで表示
#reco =st.slider("あなたの理解度は？",0, 100, 50)
#'理解度:', reco, '%'
if st.checkbox("岡田紗佳"):
    img3 = Image.open("okada_sayaka01.jpg")
    st.image(img3,caption="oppai", use_column_width=True)

option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)

'あなたの好きな数字は、',option ,'です。'

#img1 = Image.open('sano01.jpg')
#img2 = Image.open('sano02.jpg')
#st.image(img1, caption="佐野おっぱい", use_column_width=True)
#st.image(img2, caption="sanooppai", use_column_width=True)

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#    columns = ['lat', 'lon']
#)
#df
#st.map(df)
#st.area_chart(df)
#st.line_chart(df)
#st.dataframe(df.style.highlight_max(axis=0), width=150, height=200)
#st.table(df)
#st.markdown("**おっぱい**大好き")
"""
# 大
## 中
### 小
```python
import streamlit as st
import numpy as np
import pandas as pd

```

"""