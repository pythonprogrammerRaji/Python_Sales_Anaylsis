import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the csv file 
attendance_df = pd.read_csv("attendance.csv")

# display first few rows
print(attendance_df.head())

# convert "Date" column to datetime formate
attendance_df['Date'] = pd.to_datetime(attendance_df['Date'])

#check for missing values
print("Missing values : \n", attendance_df.isnull().sum())

print(attendance_df.columns)

# calulcate total present and absent days per student
attendance_summary = attendance_df.groupby(['Student Name', 'Status']).size().unstack(fill_value=0)

#Calculate total and percentage
attendance_summary['Total'] = attendance_summary.sum(axis=1)
attendance_summary['Attendance %'] = (attendance_summary['Present'] / attendance_summary['Total']) * 100

print(attendance_summary)

# Plot total present days

attendance_summary['Present'].plot(kind='bar', color='green')
plt.title('Total Present Days Per Student')
plt.ylabel('Number of Days')
plt.xlabel('Student Name')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# filter students with less than 75% attendance
low_attendance = attendance_summary[attendance_summary['Attendance %'] < 75]
print("Students with attendance below 75%: \n", low_attendance)
