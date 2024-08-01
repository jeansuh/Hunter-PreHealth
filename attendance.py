import pandas as pd
import os
import glob

def read_csv(path):
	if path == "" :
		path = os.getcwd()
	csv_files = glob.glob(os.path.join(path, "*.csv"))
	return csv_files


def find_student(csv_files):
	name = input("enter student name :")
	for f in csv_files:
		df = pd.read_csv(f)
		df = df.drop(labels=1, axis=0) #for delete or insert for NAN error unless using Python3
		seminar = df.loc[0, ['Topic']].iloc[0]
		total = df.loc[0,['Duration (Minutes)']].iloc[0]
		df2 = df.loc[df['Meeting ID'].str.contains(name, case=False), 'Start Time']
		if df2.empty :
			print(seminar + ": Did not attend")
			continue
		duration = df2.iloc[0]
		print(seminar + " : " + duration + " minutes out of " + str(total) + " minutes")

path = input("enter directory :")
csv_files = read_csv(path)
find_student(csv_files)