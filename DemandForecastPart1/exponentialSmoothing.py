import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Load the data
df = pd.read_excel("oxygen.xlsx")

# Define search range for alpha
alpha_values = np.linspace(0.01, 1.0, 100)
errors = []

# Loop over different alpha values to find the best one
for alpha in alpha_values:
    model = SimpleExpSmoothing(df["Demand"]).fit(smoothing_level=alpha, optimized=False)
    forecast = model.fittedvalues
    mse = np.mean((df["Demand"] - forecast) ** 2)
    errors.append(mse)

# Get the optimal alpha
optimal_alpha = alpha_values[np.argmin(errors)]
print(f"Optimal Alpha: {optimal_alpha}")

# Ensure the "Day" column is properly indexed
df.set_index("Day", inplace=True)

# Define parameters
alpha = optimal_alpha  
t = 31  # Forecast day

# Initialize y_t (first forecast) as the first demand value
y_t_minus_1 = df.loc[1, "Demand"]

# Apply the formula iteratively
for day in range(2, t + 1):
    # Actual demand of the previous day
    D_t_minus_1 = df.loc[day - 1, "Demand"]
    y_t = alpha * D_t_minus_1 + (1 - alpha) * y_t_minus_1  # SES formula
    y_t_minus_1 = y_t  # Update for next iteration

# Print forecast for day 31
print(f"Forecast for day {t}: {np.round(y_t)}")