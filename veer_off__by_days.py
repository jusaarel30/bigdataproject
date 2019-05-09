import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cycler
import matplotlib.ticker as ticker
from pandas.plotting import register_matplotlib_converters

def main():
    path = r'./Data/'
    all_files = glob.glob(os.path.join(path, "*.csv"))
    df_from_each_file = (pd.read_csv(f, sep=';', encoding='latin-1', low_memory=False) for f in all_files)
    df = pd.concat(df_from_each_file, ignore_index=True)
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
    df['Vkpv'].value_counts().plot('barh')
    plt.show()
if __name__ == '__main__':
    main()
