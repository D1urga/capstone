import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.DataFrame({
    "Cancer_Type": np.random.choice(["Breast", "Lung", "Prostate", "Colorectal"], 100),
    "Year": np.random.choice(range(2000, 2021), 100),
    "New_Cases": np.random.randint(5000, 50000, 100),
    "Deaths": np.random.randint(1000, 20000, 100),
    "Survival_Rate": np.random.uniform(50, 90, 100) 
})

#/////////////////////////////////////////////////////////////////////////////


plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="New_Cases", y="Survival_Rate", hue="Cancer_Type", palette="cool", s=100, edgecolor="w", alpha=0.7)
plt.title("Survival Rate vs. New Cases by Cancer Type")
plt.xlabel("New Cancer Cases")
plt.ylabel("Survival Rate (%)")
plt.legend(title="Cancer Type")
plt.show()

#/////////////////////////////////////////////////////////////////////////
yearly_cases = data.groupby("Year")["New_Cases"].sum()

plt.figure(figsize=(12, 6))
plt.plot(yearly_cases.index, yearly_cases.values, marker='o', color='b', linewidth=2)
plt.title("Total New Cancer Cases Over Time (2000-2020)")
plt.xlabel("Year")
plt.ylabel("New Cancer Cases")
plt.grid(True)
plt.show()


# ///////////////////////////////////////////


avg_cases = data.groupby("Cancer_Type")["New_Cases"].mean().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_cases.index, y=avg_cases.values, palette="viridis")
plt.title("Average New Cancer Cases by Type (2000-2020)")
plt.xlabel("Cancer Type")
plt.ylabel("Average New Cases")
plt.show()

#///////////////////////////////////////////////////////////////////////////////////////////


# Pivot data for heatmap
heatmap_data = data.pivot_table(values="New_Cases", index="Year", columns="Cancer_Type", aggfunc="sum", fill_value=0)

plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt="d")
plt.title("Yearly Cancer Cases by Cancer Type (2000-2020)")
plt.xlabel("Cancer Type")
plt.ylabel("Year")
plt.show()
