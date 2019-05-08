import numpy as np
import pandas as pd

def main():
	df = pd.read_csv('tieliikenneonnettomuudet_2017_onnettomuus.csv', sep=';', encoding='latin-1', low_memory=False)
	get_off_road(df)


def get_off_road(df):
	""" filters all the accidents where vehicle veered off the road """
	df_offroad = df.loc[(df['Ontyyppi'] <= 89) & (df['Ontyyppi'] >= 80)]


if __name__ == '__main__':
    main()
