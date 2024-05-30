import pandas as pd

df = pd.read_csv("data/train.csv", usecols=['id', 'timestamp', 'full_sq', 'life_sq', 'floor', 'max_floor',
                                            'material', 'build_year', 'num_room', 'kitch_sq', 'state', 'product_type',
                                            'sub_area', 'metro_min_walk', 'metro_km_walk', 'price_doc'])


dfm = pd.read_csv("data/macro.csv", usecols=['timestamp', 'oil_urals', 'cpi', 'ppi', 'gdp_deflator',
                                             'usdrub', 'eurrub', 'brent', 'rts', 'micex', 'deposits_rate',
                                             'mortgage_rate','salary', 'salary_growth', 'fixed_basket', 'unemployment',
                                             'employment', 'water_pipes_share', 'baths_share', 'sewerage_share',
                                             'gas_share', 'hot_water_share', 'electric_stove_share', 'heating_share'])

# dfm

print(df, dfm)
