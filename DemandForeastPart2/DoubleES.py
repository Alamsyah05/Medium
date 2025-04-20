import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load the data
df = pd.read_excel("dog-food.xlsx")
demand = df["Demand"].values

# Fit the Holt's linear trend model (double exponential smoothing)
model = ExponentialSmoothing(demand, trend="add", seasonal=None, initialization_method="estimated")
fit = model.fit(optimized=True)

# Get optimized parameters
best_alpha = fit.model.params["smoothing_level"]
best_beta = fit.model.params["smoothing_trend"]

# Forecast week 27
forecast_week_27 = fit.forecast(1)[0]

# Print results
print(f"Optimal alpha: {best_alpha}")
print(f"Optimal beta: {best_beta}")
print(f"Forecast for week 27: {np.round(forecast_week_27)}")