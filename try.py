from random import choice
import streamlit as st
import pandas as pd
from PIL import Image


@st.cache_data
def open_data():
    df_sel = pd.read_csv("data/train.csv", usecols=['timestamp', 'full_sq', 'life_sq', 'floor',
                                                    'max_floor', 'build_year', 'num_room', 'kitch_sq',
                                                    'product_type', 'sub_area', 'metro_km_walk',
                                                    'price_doc'])  # 'id', 'state', 'material', 'metro_min_walk'

    return df_sel


st.set_page_config(
    page_title='Продажи жилья в Москве',
    page_icon=':bar_chart:',
    layout='wide',
    initial_sidebar_state="auto",
)

col1, col2, col3 = st.columns([5, 1, 15])

df = open_data()
sub_area_list = df['sub_area'].unique().tolist()
sub_area_list_sorted = sorted(sub_area_list)
rooms_list = df['num_room'].unique().tolist()
rooms_list_sorted = sorted(rooms_list)
price_doc_list = df['price_doc'].unique().tolist()

col3.title('Продажи жилья в Москве')
col3.markdown('Данные с августа 2011 по июнь 2015 года')

col1.image(Image.open(f'data/{choice(range(1, 7))}.jpg'))
col1.markdown('')
col1.markdown('Выбор параметров:')
sub_area_choice = col1.multiselect('Районы:', sub_area_list_sorted, default=None)
build_year_choice = col1.number_input('Год постройки от:', value=0, step=1)
rooms_list_choice = col1.multiselect('Количество комнат:', rooms_list_sorted, default=None)
floor_choice = col1.slider('Диапазон этажей:', value=[0, 77])
price_choice = col1.slider('Диапазон цен, руб.', value=[min(price_doc_list), max(price_doc_list)])

df = df.loc[
    (df['num_room'].isin(rooms_list_choice)) &
    (df['floor'] >= floor_choice[0]) &
    (df['floor'] <= floor_choice[1]) &
    (df['build_year'] >= build_year_choice) &
    (df['sub_area'].isin(sub_area_choice)) &
    (df['price_doc'] > price_choice[0]) &
    (df['price_doc'] < price_choice[1])
    ]

# with st.expander('Data preview'):
col3.dataframe(
    df,
    column_config={
        'build_year': st.column_config.NumberColumn(format="%d")
    },
)
