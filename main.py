from visualize_data import prepare_data
from datetime import datetime
import pandas as pd, numpy as np

datasets = ['apps_and_games', 'credit_card_fraud', 'fashion', 'flight_prices']

combinations = {
    'fashion': [
        ['date_stored','star_rating'],
        ['date_stored','selling_price'],
        ['star_rating','selling_price']
    ],
    'flight_prices': [
        ['flightDate','travelDuration'],
        ['flightDate','baseFare'],
        ['flightDate','totalFare'],
        ['flightDate','seatsRemaining'],
        ['startingAirport','baseFare'],
        ['startingAirport','totalFare'],
        ['startingAirport','travelDuration'],
        ['startingAirport','seatsRemaining'],
        ['destinationAirport','travelDuration'],
        ['destinationAirport','baseFare'],
        ['destinationAirport','totalFare'],
        ['destinationAirport','seatsRemaining'],
        ['baseFare','totalFare'],
        ['baseFare','seatsRemaining'],
        ['totalFare','seatsRemaining']
    ],
    'apps_and_games': [
        ['releasedDate','minInstalls'],
        ['releasedDate','ratings'],
        ['releasedDate','price'],
        ['price','ratings'],
        ['price','minInstalls']
    ],
    'credit_card_fraud': [
        ['date','amt'],
        ['date','city_pop'],
        ['city_pop','amt']
    ]
}

def clean(df, dataset):
    if(dataset == 'fashion'):
        df['date_stored'] = df['date_stored'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    elif(dataset == 'apps_and_games'):
        df['releasedDate'] = df['releasedDate'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
        df = df.drop(df[df['price'] > 20].index)
    elif(dataset == 'credit_card_fraud'):
        df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    elif(dataset == 'flight_prices'):
        df['flightDate'] = df['flightDate'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    return df

def dfile(dset):
    return f'./data/{dataset}/{dataset}.csv'

if __name__ == '__main__':
    dataset = datasets[1]
    df = prepare_data(dfile(dataset), clean_data=lambda df: clean(df,dataset))
    print(df.head())

if __name__ == '__main__2':
    #for f in dataset_files:
    dataset, xvy, correlations = 'apps_and_games', [], []
    dfs = []
    i = 1
    #for chunk in pd.read_csv('./data/flight_prices/flight_prices.csv',chunksize=10**6):
    #    dfs.append(chunk)
    #    print(f'chunk {i} finished')
    #    i += 1
    #df = pd.concat(dfs)
    df = prepare_data(f'./data/{dataset}/{dataset}.csv',clean_data=lambda df: clean(df,dataset))
    print('data loaded')
    for column in df:
        if 'date' in column.lower():
            df[column] = pd.to_datetime(df[column]).astype(int)
    print('dates fixed')
    for x,y in combinations[dataset]:
        xvy.append(f'{x}_vs_{y}')
        correlations.append(np.corrcoef(df[x],df[y])[0,1])
        print(x,y)
    stats_df = pd.DataFrame({'x_vs_y': xvy, 'correlation': correlations})
    stats_df.to_csv(f'./stats/{dataset}/stats3.csv',index=False)
    #print(list(map(lambda x: x.split('/')[2],dataset_files)))