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
    # df_indexed = index(df_off)
    df_w, df_s = filterby_month(df_off)

    drawgraph(df_w, df_s)

def filterby_month(df):
    df_winter = df.loc[(df['Kk'] >= 11) | (df['Kk'] <= 4 )]
    df_summer = df.loc[(df['Kk'] < 11) & (df['Kk'] > 4 )]
    return df_winter, df_summer

def index(df):
    df['Päivä'] = pd.to_datetime(df['Päivä'])
    # df.set_index("Päivä")
    return df
    # return df.resample("M", on='Päivä')

def get_off_road(df):
    """ filters all the accidents where vehicle veered off the road """
    return df.loc[(df['Ontyyppi'] <= 89) & (df['Ontyyppi'] >= 80)]

def drawgraph(df_w, df_s):
    plt.style.use('grayscale')
    plt.figure(figsize=(10,5))
    plt.xticks(rotation='horizontal')

    df_s['Vakavuusko'].value_counts().plot("bar")
    plt.title("Severity of the accidents during summer")
    plt.xticks(rotation='horizontal')
    print("{} vakavuusko 0 kesällä".format(df_s['Vakavuusko'].value_counts()[0]))
    print("{} vakavuusko 2 kesällä".format(df_s['Vakavuusko'].value_counts()[1]))
    print("{} vakavuusko 1 kesällä".format(df_s['Vakavuusko'].value_counts()[2]))
    plt.savefig('summer.png')

    df_w['Vakavuusko'].value_counts().plot("bar")
    plt.title('Severity of the accidents during Winter')
    plt.xticks(rotation='horizontal')
    print("{} vakavuusko 0 talvella".format(df_w['Vakavuusko'].value_counts()[0]))
    print("{} vakavuusko 2 talvella".format(df_w['Vakavuusko'].value_counts()[1]))
    print("{} vakavuusko 1 talvella".format(df_w['Vakavuusko'].value_counts()[2]))
    plt.savefig('winter.png')

    # df_s['Vakavuusko'].value_counts().plot("bar")
    # print(f_s['Vakavuusko'].value_counts()[0])
    # print(f_s['Vakavuusko'].value_counts()[1])
    # print(f_s['Vakavuusko'].value_counts()[2])
    # plt.savefig('summer.png')




if __name__ == '__main__':
    main()
