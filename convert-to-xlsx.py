# -*- coding: utf-8 -*-
import pandas as pd
import datetime as dt
import os
import glob

def read_csv(path):
	if path == "":
		path = os.getcwd()
	csv_files = glob.glob(os.path.join(path+"/CSV", "*.csv"))
	return csv_files

def convert_xlsx(csv_files, path):
	for f in csv_files:
		df = pd.read_csv(f)
		seminar = df.loc[0,['Topic']].iloc[0].replace('/','')
		date = pd.to_datetime(df.loc[0,['Start Time']].iloc[0]).strftime("%Y-%m-%d")
		outname = date + "—" + seminar + ".xlsx"
		outpath = os.path.join(path, outname)
		print(outpath)
		df.iloc[2:]= df.iloc[2:].sort_values(by=['Meeting ID'])
		df.to_excel(outpath)

path = input("enter directory :")
csv_files = read_csv(path)
convert_xlsx(csv_files, path)