import pandas as pd
import plotly.express as px


df = pd.read_csv("data/train.csv", usecols=['id', 'timestamp', 'full_sq', 'life_sq', 'floor', 'max_floor',
                                            'material', 'build_year', 'num_room', 'kitch_sq', 'state', 'product_type',
                                            'sub_area', 'metro_min_walk', 'metro_km_walk', 'price_doc'])


# dfm = pd.read_csv("data/macro.csv", usecols=['timestamp', 'oil_urals', 'cpi', 'ppi', 'gdp_deflator',
#                                              'usdrub', 'eurrub', 'brent', 'rts', 'micex', 'deposits_rate',
#                                              'mortgage_rate','salary', 'salary_growth', 'fixed_basket', 'unemployment',
#                                              'employment', 'water_pipes_share', 'baths_share', 'sewerage_share',
#                                              'gas_share', 'hot_water_share', 'electric_stove_share', 'heating_share'])

# # dfm

# print(df, dfm)

df = df.loc[
    (df['num_room'].isin([2, 3])) &
    (df['floor'] >= 3) &
    (df['floor'] <= 8) &
    (df['build_year'] >= 1990) &
    # (df['sub_area'].isin(sub_area_choice)) &
    (df['price_doc'] > 0) &
    (df['price_doc'] < 30_000_000)
    ]

fig = px.scatter(x=df['timestamp'], y=df['price_doc'])
fig.show()
