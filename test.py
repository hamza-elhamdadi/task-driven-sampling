import pandas as pd, numpy as np, os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, date

filemap = {
    'CO': './data/pollution/pairwise/carbon',
    'NO2': './data/pollution/pairwise/nitrogen',
    'SO2': './data/pollution/pairwise/sulfur',
    'O3': './data/pollution/pairwise/ozone',
}
pollutants = ['CO','NO2','SO2','O3']

if __name__ == '__main__':
    df = pd.read_csv('./data/pollution/pollution.csv')
    df = df.loc[df['City']== 'New York']
    #df = df.loc[df['Date Local'].str.startswith('2000')]
    df['Date Local'] = df['Date Local'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

    fig, ax = plt.subplots()

    plt.xticks(rotation=90)
    ax.scatter(df['Date Local'],df['O3 Mean'],s=1)
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
    fig.autofmt_xdate()
    ax.set_xlim([date(1999, 6, 1), date(2016, 12, 31)])
    plt.show()

    #pop = pd.read_csv('./data/population.csv')
    #pop['Population'] = pop['Population'].replace(',','')

    #print(pop['Population'].replace(',',''))

    #print(pop.head())

    #nydf = df.loc[df['State'] == 'New York']
    #nypop = pop.loc[pop['Name'] == 'New York'].loc[pop['Year'] == 2010]['Population']
    #print(nypop.tolist()[0])

    #v2000 = 100
    #v2010 = 1000
    #inc = (v2010 - v2000)/11

    #print(v2000)
    #for i in range(2001,2010):
    #    print((i-2000)*inc+v2000)
    #print(v2010)

    #for i in range(2011,2020):
    #    pass
        #print(i)

    #new_pop = pop.loc[pop['Year'] >= 2000][['Name','Year','Resident Population']]
    #new_pop.to_csv('./data/population.csv',index=False)



    #df['population'] = df.apply(lambda row: pop.loc[pop['Name'] == row['State'] and pop['Year'] == 2010]['Resident Population'], axis=1)

    #print(df.head())

    #df['population'] = df.apply(lambda row: row[], axis=1)

    #print(df.head())

if __name__ == '__main__2':

    for file in os.listdir('./data/pollution/cities'):
        df = pd.read_csv(f'./data/pollution/cities/{file}')
    
        df['Date Local'] = df['Date Local'].apply(lambda x: [int(l) for l in x.split('-')])
        df['Date Local'] = df['Date Local'].apply(lambda x: x[0]*10000 + x[1]*100 + x[2])

        x = df['Date Local'].to_numpy()
        x = x.reshape(x.shape[0],1)

        for p in pollutants:
            y = df[f'{p} Mean'].to_numpy()
            y = y.reshape(y.shape[0],1)

            

            a = np.power(x - x.transpose(),2)
            b = np.power(y - y.transpose(),2)

            dist = np.sqrt(a+b)

            np.savetxt(f'{filemap[p]}/{file[:-4]}_mat.txt',dist,delimiter=',')

    #print(dist)


    #print(df.head())

    #for city in df['City'].unique():
        #formatted_city = city.replace(' ','_').replace('.','').replace('-','_').lower()
        #df.loc[df['City'] == city].to_csv(f'./data/pollution/{formatted_city}.csv',index=False)
        #if city != 'Not in a city' and city != 'New York' and df.loc[df["City"] == city].shape[0] > maxnum:
        #    maxnum = df.loc[df["City"] == city].shape[0]
        #    maxcity = city
    
    #print(maxcity, maxnum)
    