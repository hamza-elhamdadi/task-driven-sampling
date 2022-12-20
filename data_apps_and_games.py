from visualize_data import visualize_data
import pandas as pd

combinations = [
    ['date_stored','star_rating'],
    ['date_stored','selling_price'],
    ['selling_price','star_rating'],
    ['star_rating','selling_price'],
]

def remove_outliers(df):
        df = df.loc[df['star_rating'].between(0,5,inclusive='both')]
        return df

if __name__ == '__main__':
    filename = './data/apps_and_games/googleplay.csv'
    useful_cols = ['developer', 'genre', 'minInstalls', 'price', 'ratings', 'releasedDay', 'releasedMonth', 'releasedYear']

    #dts={'selling_price': int, 'star_rating': float}
    df = pd.read_csv(filename,usecols=useful_cols)

    
"""
    for comb in combinations:
        outpath=f'./visualizations/fashion/{comb[0]}_vs_{comb[1]}.png'

        
        visualize_data(filename,
                        cols=useful_cols,
                        mixed_types=list(dts.keys()),
                        dtypes=dts,
                        clean_data=lambda df: remove_outliers(df),
                        x_variable=comb[0],
                        y_variable=comb[1],
                        x_date_format='%d-%m-%Y',
                        x_is_date=True if comb[0] == 'date_stored' else False,
                        savepath=outpath)
"""