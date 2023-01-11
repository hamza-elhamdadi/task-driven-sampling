from visualize_data import prepare_data, visualize_data
from datetime import datetime

combinations = [
    ['date_stored','star_rating'],
    ['date_stored','selling_price'],
    ['selling_price','star_rating'],
    ['star_rating','selling_price'],
]

filename = './data/fashion/Fashion.csv'
useful_cols = ['title','brand','date_stored','selling_price','star_rating']
dts={'selling_price': int, 'star_rating': float}

def remove_outliers(df):
    df = df.loc[df['star_rating'].between(0,5,inclusive='both')]
    df['date_stored'] = df['date_stored'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y'))
    return df

if __name__ == '__main__':
    df = prepare_data(filename,
                        cols=useful_cols,
                        mixed_types=list(dts.keys()),
                        dtypes=dts,
                        clean_data=lambda df: remove_outliers(df))
    
    df.to_csv('./data/fashion/fashion_data.csv',index=False)
"""
    for comb in combinations:
        outpath=f'./visualizations/fashion/{comb[0]}_vs_{comb[1]}.png'

        visualize_data(df,
                        x_variable=comb[0],
                        y_variable=comb[1],
                        x_is_date=True if comb[0] == 'date_stored' else False,
                        savepath=outpath)
                    """