import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load the data
df = pd.read_excel("potting-soil.xlsx")
demand = df["Demand"].values

# Fit the Holt-Winters model (triple exponential smoothing)
model = ExponentialSmoothing(
    demand,
    trend="add",
    seasonal="add",
    seasonal_periods=12,  # karena data bulanan, diasumsikan musiman per 12 bulan
    initialization_method="estimated"
)
fit = model.fit(optimized=True)

# Ambil parameter optimal
best_alpha = fit.model.params["smoothing_level"]
best_beta = fit.model.params["smoothing_trend"]
best_gamma = fit.model.params["smoothing_seasonal"]

# Forecast untuk bulan ke-41
forecast_month_41 = fit.forecast(1)[0]

# Tampilkan hasil
print(f"Optimal alpha (level): {best_alpha}")
print(f"Optimal beta (trend): {best_beta}")
print(f"Optimal gamma (seasonal): {best_gamma}")
print(f"Forecast for month 41: {np.round(forecast_month_41, 2)}")
