print("My project is starting!")
import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")
subjects = ["Python", "Maths", "English"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = np.mean(df[subjects].values, axis=1)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

def get_result(row):
    for subject in subjects:
        if row[subject] < 40:
            return "Fail"
    return "Pass"

df["Grade"] = df["Average"].apply(get_grade)
df["Result"] = df.apply(get_result, axis=1)

print("\nSTUDENT PERFORMANCE ANALYTICS")
print(df.to_string(index=False))

print("\nCLASS SUMMARY")
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())

print("\nSUBJECT-WISE AVERAGES")
for subject in subjects:
    print(subject, ":", round(df[subject].mean(), 2))

print("\nTOP 3 PERFORMERS")
print(df.nlargest(3, "Average")[["Name", "Average"]])