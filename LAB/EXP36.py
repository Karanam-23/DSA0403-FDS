import io
import pandas as pd

# 1. Sample stock CSV data
csv_data = """date,close_price
2026-01-02,150.00
2026-01-05,152.40
2026-01-06,149.80
2026-01-07,155.10
2026-01-08,154.20
2026-01-09,158.90
2026-01-12,157.00
2026-01-13,161.50
2026-01-14,159.20
2026-01-15,163.00
"""

df = pd.read_csv(io.StringIO(csv_data))
df["daily_return_pct"] = df["close_price"].pct_change() * 100

# 2. Variability metrics
mean_price = df["close_price"].mean()
std_price = df["close_price"].std()
variance_price = df["close_price"].var()
price_range = df["close_price"].max() - df["close_price"].min()
vol_pct = df["daily_return_pct"].std()
total_return_pct = ((df["close_price"].iloc[-1] - df["close_price"].iloc[0]) / df["close_price"].iloc[0]) * 100

print(f"Mean Closing Price:   ${mean_price:.2f}")
print(f"Price Std Deviation:  ${std_price:.2f}")
print(f"Price Variance:       {variance_price:.2f}")
print(f"Price Range (Max-Min):${price_range:.2f}")
print(f"Daily Return Std Dev: {vol_pct:.2f}%")
print(f"Period Return:        {total_return_pct:+.2f}%")
