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
    return df

if __name__ == '__main__':
    filename = './data/flight_prices/itineraries.csv'
    useful_cols = ['flightDate', 'startingAirport', 'destinationAirport', 'travelDuration', 'baseFare', 'totalFare', 'seatsRemaining']

    df = prepare_data(filename,
                        cols=useful_cols,
                        clean_data=lambda df: cleanData(df)
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