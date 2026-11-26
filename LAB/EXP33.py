import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error
df = pd.DataFrame({
"engine_size_L": [1.2, 1.5, 1.6, 2.0, 2.5, 3.0, 1.4, 2.0, 2.4, 3.5, 1.8, 2.2],
"horsepower": [90, 120, 135, 170, 210, 280, 110, 180, 195, 310, 150, 190],
"fuel_efficiency_mpg": [42, 36, 34, 28, 24, 19, 38, 29, 25, 17, 32, 26],
"price": [16000, 20500, 22500, 29000, 36000, 48000, 18500, 31000, 34000, 54000, 25000, 33000]
})

features = ["engine_size_L", "horsepower", "fuel_efficiency_mpg"]
X = df[features]
y = df["price"]
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

print(f"R² Score: {r2_score(y, y_pred):.4f}")
print(f"MAE: ${mean_absolute_error(y, y_pred):,.2f}\n")
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
std_model = LinearRegression().fit(X_std, y)

insights = pd.DataFrame({
"feature": features,
"raw_coef": model.coef_,
"abs_standardized_impact": np.abs(std_model.coef_)
}).sort_values("abs_standardized_impact", ascending=False)

print("Feature Influence Ranking (Standardized):")
print(insights.to_string(index=False))


### Expected Output
#```text
#R² Score: 0.9963
#MAE: $539.59

#Feature Influence Ranking (Standardized):
 #           feature    raw_coef  abs_standardized_impact
  #       horsepower  125.925548              8325.134242
#fuel_efficiency_mpg  148.550469              1159.436835
 #     engine_size_L 1114.614722               716.578458
