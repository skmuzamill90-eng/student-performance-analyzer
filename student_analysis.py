import pandas as pd
import numpy as np

# Create dataset
data = {
    "Name": ["Ali","Sara","John","Mike","Anu"],
    "Math": [78, 90, 85, 60, 88],
    "Science": [82, 95, 80, 65, 92],
    "English": [75, 88, 78, 70, 85]
}

df = pd.DataFrame(data)

# Step 1: Calculate Total Marks (row-wise)
df["Total"] = df[["Math","Science","English"]].sum(axis=1)

# Step 2: Calculate Average Marks (row-wise)
df["Average"] = np.mean(df[["Math","Science","English"]], axis=1)

# Step 3: Display full dataset
print("Full Data:\n", df)

# Step 4: Find Top Student
top_student = df[df["Total"] == df["Total"].max()]
print("\nTop Student:\n", top_student)

# Step 5: Students with Average > 80
high_scorers = df[df["Average"] > 80]
print("\nStudents with Average > 80:\n", high_scorers)

# Step 6: Convert subject marks to NumPy array 
X = df[["Math","Science","English"]].values
print("\nNumPy Array Shape:", X.shape)
print("NumPy Array:\n", X)