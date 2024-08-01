import pandas as pd
import os
import glob

def read_xlsx(path):
	if path == "" :
		path = os.getcwd()
	xlsx_files = glob.glob(os.path.join(path, "*.xlsx"))
	return xlsx_files

def convert_xlsx(xlsx_files, path):
	for f in xlsx_files:
		read_file = pd.read_excel(f)
		read_file.to_csv(f+".csv", index=None, header=True)

path = input("enter directory :")
xlsx_files = read_xlsx(path)
convert_xlsx(xlsx_files, path)