import io
from google.colab import files
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# 1. Upload your Excel file directly into Colab
print("Please select your clinical trial Excel file (.xlsx or .xls):")
uploaded = files.upload()

file_name = list(uploaded.keys())[0]
# Add sheet_name='YourSheetName' inside read_excel() if data is not on the first tab
df = pd.read_excel(io.BytesIO(uploaded[file_name]))

print("\nColumns found in your Excel sheet:", df.columns.tolist())

# 2. Configure your Excel column names and group labels (UPDATE THESE TO MATCH YOUR FILE)
group_col = 'Group'              # Column containing group assignments
outcome_col = 'Outcome_Score'    # Column containing numeric patient measurements
control_label = 'Placebo'        # Exact text label for the control group
treatment_label = 'Treatment'    # Exact text label for the new drug group

# 3. Filter and clean numeric data for both groups
control_group = pd.to_numeric(
    df[df[group_col] == control_label][outcome_col], errors='coerce'
).dropna()

treatment_group = pd.to_numeric(
    df[df[group_col] == treatment_label][outcome_col], errors='coerce'
).dropna()

# 4. Perform Independent Two-Sample T-Test (Welch's t-test)
t_stat, p_value = stats.ttest_ind(treatment_group, control_group, equal_var=False)

# 5. Print Statistical Summary
alpha = 0.05
print(f"\n--- Clinical Trial Hypothesis Test Results ---")
print(f"{control_label} (n={len(control_group)}) Mean: {control_group.mean():.2f} (SD: {control_group.std(ddof=1):.2f})")
print(f"{treatment_label} (n={len(treatment_group)}) Mean: {treatment_group.mean():.2f} (SD: {treatment_group.std(ddof=1):.2f})")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value:     {p_value:.4e}")

if p_value < alpha:
    print("\nConclusion: Reject the null hypothesis. Statistically significant effect detected (p < 0.05).")
else:
    print("\nConclusion: Fail to reject the null hypothesis. No statistically significant difference (p >= 0.05).")

# 6. Visualize Data & P-Value using Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))

box_data = [control_group, treatment_group]
bp = ax.boxplot(
    box_data,
    patch_artist=True,
    widths=0.4,
    labels=[f'Control ({control_label})', f'Treatment ({treatment_label})']
)

colors = ['#A0AEC0', '#3182CE']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.75)

# Overlay individual patient data points (jittered)
np.random.seed(42)
for i, group in enumerate(box_data, start=1):
    x_jitter = np.random.normal(i, 0.04, size=len(group))
    ax.scatter(x_jitter, group, color='#1A202C', alpha=0.6, s=25, zorder=3)

# Add Significance Bracket and P-Value Annotation
y_max = max(control_group.max(), treatment_group.max())
y_min = min(control_group.min(), treatment_group.min())
data_range = y_max - y_min if y_max != y_min else 1.0

y_bracket = y_max + (0.08 * data_range)
bracket_height = 0.04 * data_range

ax.plot([1, 1, 2, 2], [y_bracket, y_bracket + bracket_height, y_bracket + bracket_height, y_bracket], lw=1.5, c='black')

if p_value < 0.001:
    p_text = "p < 0.001 (***)"
elif p_value < 0.01:
    p_text = f"p = {p_value:.4f} (**)"
elif p_value < 0.05:
    p_text = f"p = {p_value:.4f} (*)"
else:
    p_text = f"p = {p_value:.4f} (ns)"

ax.text(1.5, y_bracket + bracket_height + (0.02 * data_range), p_text, ha='center', va='bottom', fontsize=11, fontweight='bold')

# Dynamic Y-axis padding so the bracket never clips at the top
ax.set_ylim(bottom=y_min - (0.08 * data_range), top=y_bracket + (0.20 * data_range))
ax.set_ylabel(outcome_col, fontsize=12)
ax.set_title(f'Clinical Trial Efficacy: {control_label} vs. {treatment_label}', fontsize=14, fontweight='bold', pad=15)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
