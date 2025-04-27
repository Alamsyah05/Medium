import numpy as np
import plotly.graph_objects as go

# Parameters
p = 0.0007
q = 0.2422
m = 46365287

# Simulation settings
T = 31  # number of years
steps_per_year = 1  # yearly steps
t = np.arange(0, T, 1/steps_per_year)

# Arrays to store results
adopters = np.zeros(len(t))
cumulative_adopters = np.zeros(len(t))

# Initial conditions
cumulative_adopters[0] = 0

# Bass Diffusion Model
for i in range(1, len(t)):
    adoption_rate = (p + q * (cumulative_adopters[i-1] / m)) * (m - cumulative_adopters[i-1])
    adopters[i] = adoption_rate
    cumulative_adopters[i] = cumulative_adopters[i-1] + adopters[i]

# Find peak demand
demand_peak_idx = np.argmax(adopters)
demand_peak_time = t[demand_peak_idx]
demand_peak_value = adopters[demand_peak_idx]
cumulative_demand_at_peak = cumulative_adopters[demand_peak_idx]

print(f"Peak demand occurs at year: {demand_peak_time:.2f}")
print(f"Peak demand rate (number of adopters in that year): {demand_peak_value:.0f}")
print(f"Cumulative demand at peak: {cumulative_demand_at_peak:.0f}")

# Plotly plot
fig = go.Figure()

# Add Demand Rate trace
fig.add_trace(go.Scatter(
    x=t,
    y=adopters,
    mode='lines',
    name='Demand Rate',
    line=dict(color='royalblue', width=4),
))

# Add Cumulative Demand trace
fig.add_trace(go.Scatter(
    x=t,
    y=cumulative_adopters,
    mode='lines',
    name='Cumulative Demand',
    line=dict(color='darkorange', width=4),
))

# Mark peak demand with a vertical line
fig.add_trace(go.Scatter(
    x=[demand_peak_time, demand_peak_time],
    y=[0, demand_peak_value],
    mode='lines',
    name='Peak Demand',
    line=dict(color='red', dash='dash', width=3),
))

# Add annotations for peak demand
fig.add_annotation(
    x=demand_peak_time,
    y=demand_peak_value,
    text=f'Peak Demand at {demand_peak_time:.2f} years\n{demand_peak_value:.0f} Adopters',
    showarrow=True,
    arrowhead=2,
    ax=20,
    ay=-40,
    font=dict(size=14, color="red"),
    arrowcolor='red'
)

# Update layout with centered title, larger font sizes, and bigger plot area
fig.update_layout(
    title={
        'text': 'Bass Diffusion Model Simulation (Yearly)',
        'x': 0.5,  # center title
        'xanchor': 'center',
        'yanchor': 'top',
        'y': 0.95,
        'font': dict(size=18)
    },
    xaxis_title='Years',
    yaxis_title='Number of Adopters',
    template='plotly',
    showlegend=True,
    plot_bgcolor='white',
    hovermode='closest',
    margin=dict(l=70, r=70, t=70, b=70),
    font=dict(size=14),
    xaxis=dict(
        zeroline=True,  # add horizontal axis line
        zerolinecolor='black',  # line color
        zerolinewidth=1  # line width
    ),
    yaxis=dict(
        zeroline=True,  # add vertical axis line
        zerolinecolor='black',  # line color
        zerolinewidth=1  # line width
    ),
    height=800,  # Increase height of the plot
    width=1000,  # Increase width of the plot
)

fig.show()