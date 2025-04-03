import pandas as pd
import numpy as np

# Load the data
df = pd.read_excel("oxygen.xlsx")

# Define parameters
N = 7  # Number of past days
t = 31  # Forecast day

# Ensure the "Day" column is used for correct indexing
df.set_index("Day", inplace=True)  # Set "Day" as the index

print(df.loc[t-N:t-1, "Demand"])

# Ensure sufficient data
if t > N:
    forecast = df.loc[t-N:t-1, "Demand"].mean()
    print(f"Forecast for day {t}: {np.round(forecast)}")
else:
    print("Not enough data to compute forecast.")
