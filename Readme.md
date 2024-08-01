# How to use Python scripts

## Installing Python 3

follow the instructions on the Python documentation website

https://realpython.com/installing-python/

## What the scripts do

### attendance.py
The script gives you the attendance record of a student.
This script takes the directory of the folder containing CSV files, and the name of the student. (case insensitive)
The output is in the following format:

```
//If the student did not attend the seminar :
name of the seminar : Did not attend
//Otherwise :
duration of stay out of total seminar duration
```

### convert-to-xlsx.py
This script bulk converts CSV files to xlsx files.
The script takes the directory of the folder containing the parent folder of the CSV files, where the xlsx files would go once converted.

### convert-to-csv.py
This script bulk converts xlsx files to CSV files.
The script takes the directory of the folder containing the xlsx files.

### seminar_data_report.py
This script gives total attendance for each seminar.
The script takes the directory of the folder containing the csv files.
The output data is in the following format : 

| index  | seminar | date | students |
| -- | --------------- | -------------- | --------------------------- |
| 0  | seminar 1 name  | seminar 1 date | number of students attended |
| 1  | seminar 2 name  | seminar 2 date | number of students attended |

## Running the scripts

In terminal or command prompt, change directory to the folder containing the scripts.

For example in terminal or command prompt
```
cd /Volumes/as-prehealth/Python Scripts
```

Run the script using terminal.

For example, to run the attendance python script,
```
python3 attendance.py
```

When you see the folloring prompt in terminal/command prompt:

```
enter directory :
```

Enter the directory of the foler containing the desired CSV files.

For example, on MacOS, to review 2024 Spring PPAP 1000 files, you would copy and paste the following directory.

```
/Volumes/as-prehealth/Pre-Health Event Attendance/Zoom Attendance Data/2024/Spring 2024 Semester/PPAP 1000/CSV
```

When you press enter, you will see the following prompt:

```
enter student name :
```

Enter the name of the student. The script is case insensitive.