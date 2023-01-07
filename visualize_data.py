import pandas as pd, numpy as np, matplotlib.pyplot as plt, matplotlib.dates as mdates
from datetime import datetime, date

pd.options.mode.chained_assignment = None

def remove_na(df,mixed_types,dtypes):
    for mtype in mixed_types:
        df[mtype] = pd.to_numeric(df[mtype],errors='coerce')
    df = df.dropna(subset=mixed_types)
    for mtype in mixed_types:
        df[mtype] = df[mtype].astype(dtypes[mtype])
    return df

def validate_col_type(df,colname,dtype):
    return df.loc[df[colname].map(type) != dtype].empty

def prepare_data(filename, 
                            cols=None, 
                            mixed_types=None, 
                            dtypes=None,
                            clean_data=None,
                            ):
    if mixed_types != None and dtypes == None:
        print('please specify the dtypes for the columns of mixed types')
        return
        
    df = pd.read_csv(filename, usecols=cols)
    if mixed_types != None:
        df = remove_na(df,mixed_types,dtypes)

    if clean_data != None:
        df = clean_data(df)

    return df

     

def visualize_data(df,
                            x_variable=None, 
                            y_variable=None,
                            x_is_date=False,
                            y_is_date=False,
                            savepath=None):

    fig, ax = plt.subplots()

    ax.scatter(df[x_variable],df[y_variable],s=1)
    if x_is_date:
        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
        fig.autofmt_xdate()
    if y_is_date:
        ax.yaxis_date()
        ax.yaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
        fig.autofmt_ydate()
    if savepath == None:
        plt.show()
    else:
        plt.savefig(savepath)
