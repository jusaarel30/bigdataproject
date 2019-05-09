import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cycler
import matplotlib.ticker as ticker
from pandas.plotting import register_matplotlib_converters

def main():
    df = pd.read_csv('tieliikenneonnettomuudet_2017_onnettomuus.csv', sep=';', encoding='latin-1', low_memory=False)
    df_off = get_off_road(df)
    df_indexed = index(df_off)
    drawgraph(df_off)


def index(df):
    df['Päivä'] = pd.to_datetime(df['Päivä'])
    df.set_index("Päivä")
    return df
    # return df.resample("24H", on='Päivä')

def get_off_road(df):
    """ filters all the accidents where vehicle veered off the road """
    return df.loc[(df['Ontyyppi'] <= 89) & (df['Ontyyppi'] >= 80)]

def drawgraph(df):
    plt.style.use('grayscale')
    plt.figure(figsize=(10,5))
    df['Vkpv'].value_counts().plot('bar')
    plt.xticks(rotation='horizontal')
    plt.show()
    
if __name__ == '__main__':
    main()
