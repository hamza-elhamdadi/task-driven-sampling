from visualize_data import prepare_data, visualize_data
from datetime import datetime

combinations = [
    ['date','amt'],
    ['date','city_pop'],
    ['city_pop','amt'],
    ['gender','amt'],
]

def cleanData(df):
    #df['date'] = df['trans_date_trans_time'].apply(lambda row: row.split(' ')[0])
    #df.drop('trans_date_trans_time',axis=1,inplace=True)
    #df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    df = df.drop(df[df['city_pop'] > 500000].index)
    return df

if __name__ == '__main__':
    filename = './data/credit_card_fraud/fraudTrain.csv'
    useful_cols = ['trans_date_trans_time','category','amt','gender','city_pop','is_fraud']

    df = prepare_data(filename,
                        cols=useful_cols,
                        clean_data=lambda df: cleanData(df)
                        )
    
    visualize_data(
        df,
        x_variable='city_pop',
        y_variable='amt',
        x_is_date=False,
        savepath='./visualizations/credit_card_fraud/city_pop_lessthan500000_vs_amt.png'
    )
"""
    for comb in combinations:
        outpath=f'./visualizations/credit_card_fraud/{comb[0]}_vs_{comb[1]}.png'

        visualize_data(
            df,
            x_variable=comb[0],
            y_variable=comb[1],
            x_is_date=comb[0] == 'date',
            savepath=outpath
        )"""