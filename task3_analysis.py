# Task 3 - Analysis with Pandas & NumPy

import pandas as pd
import numpy as np

# Step 1: Load the cleaned CSV file
df = pd.read_csv("data/trends_clean.csv")

# Step 2: Basic exploration
print("Loaded data:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

# Step 3: Average values
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score   :", avg_score)
print("Average comments:", avg_comments)

# Step 4: NumPy analysis
scores = df["score"].values

print("\n--- NumPy Stats ---")
print("Mean score   :", np.mean(scores))
print("Median score :", np.median(scores))
print("Std deviation:", np.std(scores))
print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))

# Step 5: Category with most stories
top_category = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category} ({count} stories)")

# Step 6: Most commented story
max_comments_row = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:")
print(max_comments_row["title"], "—", max_comments_row["num_comments"], "comments")

# Step 7: Add new columns

# Engagement column
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular column
df["is_popular"] = df["score"] > avg_score

# Step 8: Save new CSV
df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved to data/trends_analysed.csv")