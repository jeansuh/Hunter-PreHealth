import pandas as pd
import os
import glob
import datetime

def read_csv(path):
	if path == "" :
		path = os.getcwd()
	csv_files = glob.glob(os.path.join(path, "*.csv"))
	return csv_files

def appendDf(df, students, seminar, date):
	new_row = pd.Series({'Seminar': seminar, 'Date': date, 'Students': str(int(students))})
	df = pd.concat([new_row.to_frame().T], ignore_index=True,sort=False)
	return df

def find_data(csv_files, df1):
	for f in csv_files:
		df = pd.read_csv(f)
		df = df.drop(labels=1, axis=0) #for delete or insert for NAN error
		seminar = df.loc[0, ['Topic']].iloc[0]
		students = df.loc[0,['Participants']].iloc[0]
		date = df.loc[0,['Start Time']].iloc[0]
		date = pd.to_datetime(date, format='%m/%d/%Y %H:%M:%S %p').strftime('%m/%d/%Y')
		df1 = pd.concat([df1,appendDf(df1, students, seminar, date)], ignore_index=True)
		print(seminar + " - " + str(date) + " - " + str(int(students)) + " students attended.")
	df1.to_csv("data_report.csv")

path = input("enter directory :")
df1 = pd.DataFrame({'Seminar': [], 'Date' : [], 'Students' : []})
csv_files = read_csv(path)
find_data(csv_files, df1)