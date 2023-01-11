from visualize_data import prepare_data, visualize_data
from datetime import datetime
import pandas as pd

combinations = [
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
    ['totalFare','seatsRemaining'],
]

def cleanData(df):
    df['flightDate'] = df['flightDate'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    #df = df.drop(df[df['baseFare'] > 500].index)
    #df = df.drop(df[df['totalFare'] > 500].index)
    return df

if __name__ == '__main__':
    filename = './data/flight_prices/itineraries.csv'
    useful_cols = ['flightDate', 'startingAirport', 'destinationAirport', 'travelDuration', 'baseFare', 'totalFare', 'seatsRemaining']

    df = prepare_data(filename,
                        cols=useful_cols,
                        clean_data=lambda df: cleanData(df)
                        )
    df.to_csv('./data/flight_prices/flight_prices.csv',index=False)
"""
    visualize_data(
            df,
            x_variable='baseFare',
            y_variable='totalFare',
            x_is_date=False,
            savepath='./visualizations/flight_prices/baseFare_under500_vs_totalFare_under500'
        )

    for comb in combinations:
        outpath=f'./visualizations/flight_prices/{comb[0]}_vs_{comb[1]}.png'

        visualize_data(
            df,
            x_variable=comb[0],
            y_variable=comb[1],
            x_is_date=comb[0] == 'flightDate',
            savepath=outpath
        )
        """