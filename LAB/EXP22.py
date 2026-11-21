import io
from google.colab import files
import pandas as pd
from scipy import stats

# 1. Upload your Excel file directly into Colab
print("Please select your Excel file (.xlsx or .xls):")
uploaded = files.upload()

# Automatically grab the uploaded filename and read it into pandas
file_name = list(uploaded.keys())[0]
# Note: Add sheet_name='YourSheetName' inside read_excel() if your data isn't on the first tab
df = pd.read_excel(io.BytesIO(uploaded[file_name]))

# Preview the first few rows and exact column names to verify
print("\nColumns found in your Excel sheet:", df.columns.tolist())

# 2. Set your column names and target category (UPDATE THESE TO MATCH YOUR EXCEL SHEET)
category_col = 'product_category'  # Replace with your category column header
rating_col = 'rating'              # Replace with your rating column header
target_category = 'Electronics'    # Replace with the category you want to analyze

# 3. Filter data and clean missing/non-numeric values
category_ratings = pd.to_numeric(
    df[df[category_col] == target_category][rating_col], 
    errors='coerce'
).dropna()

# 4. Calculate sample statistics using pandas
n = len(category_ratings)
sample_mean = category_ratings.mean()
std_error = category_ratings.sem()

# 5. Compute the 95% Confidence Interval
confidence_level = 0.95
ci_low, ci_high = stats.t.interval(
    confidence=confidence_level,
    df=n - 1,
    loc=sample_mean,
    scale=std_error
)

# 6. Output Analyst Insights
print(f"\n--- Customer Satisfaction Analysis: {target_category} ---")
print(f"Total Valid Reviews (n): {n}")
print(f"Sample Average Rating: {sample_mean:.2f} / 5.00")
print(f"95% Confidence Interval: ({ci_low:.2f}, {ci_high:.2f})")
print(f"\nInsight: We are 95% confident that the true population mean rating for "
      f"'{target_category}' is between {ci_low:.2f} and {ci_high:.2f} stars.")
