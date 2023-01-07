from visualize_data import prepare_data, visualize_data
from datetime import datetime

combinations = [
    ['releasedDate','minInstalls'],
    ['releasedDate','ratings'],
    ['releasedDate','price'],
    ['price','ratings'],
    ['price','minInstalls'],
    ['price','ratings'],
]

monthNum = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}

def cleanData(df):
        df['releasedDate'] = df.apply(lambda row: f'{row["releasedDay"]}-{monthNum[row["releasedMonth"]]}-{row["releasedYear"]}', axis=1)
        df.drop(['releasedDay','releasedMonth','releasedYear'],axis=1,inplace=True)
        df['releasedDate'] = df['releasedDate'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y'))
        df = df.loc[df['price'] != 0.0]
        return df

if __name__ == '__main__':
    filename = './data/apps_and_games/googleplay.csv'
    useful_cols = ['developer', 'genre', 'minInstalls', 'price', 'ratings', 'releasedDay', 'releasedMonth', 'releasedYear']

    #dts={'selling_price': int, 'star_rating': float}
    df = prepare_data(filename,
                        cols=useful_cols,
                        clean_data=lambda df: cleanData(df)
                        )
    
    print(df.head())

    for comb in combinations:
        outpath=f'./visualizations/apps_and_games/{comb[0]}_vs_{comb[1]}.png'

        visualize_data(df,
                        x_variable=comb[0],
                        y_variable=comb[1],
                        x_is_date=True if comb[0] == 'releasedDate' else False,
                        savepath=outpath)
