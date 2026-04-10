# ----------------------------------------
# Task 4: Visualization (TrendPulse)
# ----------------------------------------

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# ----------------------------------------
# Step 1: Load Data
# ----------------------------------------

# Load CSV from Task 3
df = pd.read_csv("data/trends_analysed.csv")

print("Data loaded successfully!")

# ----------------------------------------
# Step 2: Create outputs folder
# ----------------------------------------

if not os.path.exists("outputs"):
    os.makedirs("outputs")

# ----------------------------------------
# Chart 1: Top 10 Stories by Score
# ----------------------------------------

# Sort and get top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles
top10["title"] = top10["title"].apply(
    lambda x: x[:45] + "..." if len(x) > 45 else x
)

# Create chart
plt.figure(figsize=(16, 10))

plt.barh(top10["title"], top10["score"])

plt.xlabel("Score", fontsize=16, labelpad=10)
plt.ylabel("Story Title", fontsize=16, labelpad=10)
plt.title("Top 10 Stories by Score", fontsize=18, pad=15)

plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.gca().invert_yaxis()
plt.margins(y=0.1)

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png", dpi=400)
plt.close()

print("Chart 1 saved!")

# ----------------------------------------
# Chart 2: Stories per Category
# ----------------------------------------

# Count categories
category_counts = df["category"].value_counts()

plt.figure(figsize=(12, 7))

plt.bar(category_counts.index, category_counts.values)

plt.xlabel("Category", fontsize=14)
plt.ylabel("Number of Stories", fontsize=14)
plt.title("Stories per Category", fontsize=16)

plt.xticks(rotation=30, fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png", dpi=400)
plt.close()

print("Chart 2 saved!")

# ----------------------------------------
# Chart 3: Score vs Comments (Scatter)
# ----------------------------------------

# Split data
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(12, 7))

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score", fontsize=14)
plt.ylabel("Number of Comments", fontsize=14)
plt.title("Score vs Comments", fontsize=16)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend(fontsize=12)

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png", dpi=400)
plt.close()

print("Chart 3 saved!")

# ----------------------------------------
# Bonus: Dashboard
# ----------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# Chart 1 in dashboard
axes[0].barh(top10["title"], top10["score"])
axes[0].set_title("Top Stories")
axes[0].invert_yaxis()

# Chart 2 in dashboard
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")
axes[1].tick_params(axis='x', rotation=30)

# Chart 3 in dashboard
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

plt.suptitle("TrendPulse Dashboard", fontsize=18)

plt.tight_layout()
plt.savefig("outputs/dashboard.png", dpi=400)
plt.close()

print("Dashboard saved!")

# ----------------------------------------
# Done
# ----------------------------------------

print("All charts saved in outputs folder!")