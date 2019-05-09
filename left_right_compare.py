import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

def main():
	path = r'./Data/'
	all_files = glob.glob(os.path.join(path, "*.csv"))
	df_from_each_file = (pd.read_csv(f, sep=';', encoding='latin-1', low_memory=False) for f in all_files)
	df = pd.concat(df_from_each_file, ignore_index=True)
	df = index(df)
	offroad = get_off_road(df)

	left_offroad = get_left_off_road(offroad)
	right_offroad = get_right_off_road(offroad)

	left_injured = get_severity_injury(left_offroad)
	left_dead = get_severity_death(left_offroad)

	right_injured = get_severity_injury(right_offroad)
	right_dead = get_severity_death(right_offroad)

	draw_graph_line(left_offroad, "Left side veerings")
	draw_graph_line(left_injured, "Left side veerings that resulted in one or more injured")
	draw_graph_line(left_dead, "Left side veerings that resulted in one or more dead")

	draw_graph_line(right_offroad, "Right side veerings")
	draw_graph_line(right_injured, "Right side veerings that resulted in one or more injured")
	draw_graph_line(right_dead, "Right side veerings that resulted in one or more dead")


def index(df):
	df = arrange_by_day(df)
	df['Päivä'] = pd.to_datetime(df['Päivä'])
	return df.set_index("Päivä")

def get_off_road(df):
	""" filters all the accidents where vehicle veered off the road """
	df_offroad = df.loc[(df['Ontyyppi'] <= 89) & (df['Ontyyppi'] >= 80)]
	return df_offroad

def draw_graph_bar(df):
	plt.style.use('grayscale')
	plt.figure(figsize=(10,5))
	plt.bar(df.index, height=df["Loukkaant"], width=10.0)
	plt.show()

def draw_graph_line(df, title):
	plt.style.use('grayscale')
	plt.figure(figsize=(10,5))
	plt.title(title)
	df['Kk'].value_counts(sort=False).plot("bar")
	plt.xticks(rotation='horizontal')
	plt.show()

def resample_month(df):
	df['Päivä'] = pd.to_datetime(df['Päivä'])
	return df.resample('M', on="Päivä").sum()

def resample_day(df):
	df['Päivä'] = pd.to_datetime(df['Päivä'])
	return df.resample('D', on="Päivä").sum()

def arrange_by_month(df):
	return df.sort_values(by=["Kk"])

def arrange_by_day(df):
	return df.sort_values(by=["Päivä"])

def get_left_off_road(df):
	""" filters all the accidents where the vehicle veered off to the left """
	return df.loc[(df['Ontyyppi'] == 81) | (df['Ontyyppi'] == 83) | (df['Ontyyppi'] == 85)]

def get_right_off_road(df):
	""" filters all the accidents where the vehicle veered off to the right """
	return df.loc[(df['Ontyyppi'] == 80) | (df['Ontyyppi'] == 82) | (df['Ontyyppi'] == 84)]

def get_severity_death(df):
	return df.loc[(df['Vakavuusko'] == 1)]
def get_severity_injury(df):
	return df.loc[(df['Vakavuusko'] == 2)]

def get_dead(df):
	return df.loc[(df['Kuolleet'] > 0)]

def get_injured(df):
	return df.loc[(df['Loukkaant'] > 0)]

if __name__ == '__main__':
    main()
