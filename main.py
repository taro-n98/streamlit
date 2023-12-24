import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('test')
st.write('Hello world')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

# データフレームを表示
st.write(df)
# st.dataframeだと、引数を指定することができる
st.dataframe(df, width = 100, height=100)
# axis=0のmaxをハイライトする
st.dataframe(df.style.highlight_max(axis=0))
# 静的なデータフレームを表示する
st.table(df)

'''
# 章
## 節
### 項

```python
import streamlit as st
import pandas as pd
import numpy as np
```

'''

df = pd.DataFrame(
    np.random.rand(20,3), #正規分布をもとにデータを作成
    columns = ['a','b','c']
)

st.dataframe(df)
# チャートをかく
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69 , 139.70], #正規分布をもとにデータを作成
    columns = ['lat','lon']
)

st.dataframe(df.head())
st.map(df)

# 画像の表示
st.write('Display Image')
img = Image.open('visualization-2.png')
st.image(img, caption='chart_line', use_column_width=True)

# チェックボックス
if st.checkbox('Show Image'): # チェックボックスをつけると画像を表示
    img = Image.open('visualization-2.png')
    st.image(img, caption='chart_line', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1,9))
)
st.write('あなたの好きな数字は',option,'です')

# テキストinput
option = st.text_input('あなたの趣味を教えて下さい')
'あなたの趣味', option

text = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', text

# サイドバー
name = st.sidebar.text_input('あなたの名前は？')
age = st.sidebar.slider('あなたの年齢は？', 0, 100, 10)

'私の名前は', name, 'です。'
'私の年齢は', age, '歳です。'