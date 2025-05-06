import json
from datetime import datetime
import matplotlib
matplotlib.use("TkAgg")  # Only if needed for Pycharm GUI plotting
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


with open("../data/historical_weather.json", "r") as f:
    data = json.load(f)

cities = ["Amsterdam", "Berlin", "Prague", "Vienna", "Budapest"]


plt.figure(figsize=(12, 6))

# Plot each city
for city in cities:
    city_data = [entry for entry in data if entry["city"] == city]
    timestamps = [
        datetime.fromisoformat(entry["timestamp"]).strftime("%H:%M")
        for entry in city_data
    ]
    temperatures = [entry["temperature_c"] for entry in city_data]
    step = 10 # plot every 10th point only
    timestamps = timestamps[::step]
    temperatures = temperatures[::step]

    if timestamps and temperatures:
        plt.scatter(timestamps, temperatures, label=city)

# Style
plt.title("Temperature Comparison Over Cities")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=60, fontsize=8)


plt.legend(
    title="Cities",
    title_fontsize=12,
    fontsize=10,
    loc="upper right",
    frameon=True
)


plt.tight_layout()
plt.savefig("../data/temperature_comparison.png", dpi=300)
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%H:%M'))  # Adds newline for better spacing
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))  # Show tick every 2 hours

plt.show()
