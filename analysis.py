import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sample_data.csv")

# --- 1. Overall condition comparison ---
condition_mean = df.groupby("condition")["expression"].mean()

# --- 2. Age group comparison ---
age_mean = df.groupby("age_group")["expression"].mean()

# --- 3. Gene-wise comparison ---
gene_mean = df.groupby("gene")["expression"].mean()

# --- 4. Combined (age + condition) ---
combined = df.groupby(["age_group", "condition"])["expression"].mean().unstack()

# Print outputs
print("Condition Mean:\n", condition_mean)
print("\nAge Group Mean:\n", age_mean)
print("\nGene Mean:\n", gene_mean)
print("\nCombined:\n", combined)

# --- Plot 1: Condition ---
condition_mean.plot(kind="bar", color=["green", "red"])
plt.title("Expression by Condition")
plt.savefig("condition_plot.png")
plt.show()

# --- Plot 2: Age ---
age_mean.plot(kind="bar", color=["blue", "orange"])
plt.title("Expression by Age Group")
plt.savefig("age_plot.png")
plt.show()

# --- Plot 3: Gene ---
gene_mean.plot(kind="bar")
plt.title("Expression by Gene")
plt.savefig("gene_plot.png")
plt.show()

# --- Plot 4: Combined ---
combined.plot(kind="bar")
plt.title("Expression by Age and Condition")
plt.savefig("combined_plot.png")
plt.show()
