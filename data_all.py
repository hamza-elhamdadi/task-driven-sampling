from visualize_data import prepare_data
from datetime import datetime
import os, pandas as pd

datapath = './data/'
dataset_dirs = [os.path.join(datapath,e) for e in os.listdir(datapath) if e not in ['.DS_Store','pollution','raw_data','credit_card_fraud']]
dataset_files = list(sorted([os.path.join(e, os.listdir(e)[0]) for e in dataset_dirs]))

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
        ['price','minInstalls'],
        ['price','ratings']
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
    elif(dataset == 'credit_card_fraud'):
        df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    elif(dataset == 'flight_prices'):
        df['flightDate'] = df['flightDate'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    return df

if __name__ == '__main__':
    #for f in dataset_files:
    dataset, xvy, correlations = 'flight_prices', [], []
    df = prepare_data('./data/raw_data/itineraries.csv',clean_data=lambda df: clean(df,dataset))
    print('data loaded')
    for column in df:
        if 'date' in column.lower():
            df[column] = pd.to_datetime(df[column]).astype(int)
    print('dates fixed')
    for x,y in combinations[dataset]:
        xvy.append(f'{x}_vs_{y}')
        correlations.append(df[x].corr(df[y]))
        print(x,y)
    stats_df = pd.DataFrame({'x_vs_y': xvy, 'correlation': correlations})
    stats_df.to_csv(f'./stats/{dataset}/stats.csv',index=False)
    #print(list(map(lambda x: x.split('/')[2],dataset_files)))