import json
from datetime import datetime
import matplotlib
matplotlib.use("TkAgg")  # ✅ FIX for PyCharm GUI backend
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Load historical data
with open("../data/historical_weather.json", "r") as f:
    data = json.load(f)

# Extract unique cities and dates
cities = sorted(set(entry["city"] for entry in data))
dates = sorted(set(datetime.fromisoformat(entry["timestamp"]).date().isoformat() for entry in data))

# --------- GUI Starts ----------
root = tk.Tk()
root.title("Weather Visualizer")

# City Dropdown
tk.Label(root, text="Select City:").pack()
city_var = tk.StringVar()
city_dropdown = ttk.Combobox(root, textvariable=city_var, values=cities, state="readonly")
city_dropdown.pack()

# Date Dropdown
tk.Label(root, text="Select Date:").pack()
date_var = tk.StringVar()
date_dropdown = ttk.Combobox(root, textvariable=date_var, values=dates, state="readonly")
date_dropdown.pack()

# Plotting Function
def plot_weather():
    selected_city = city_var.get()
    selected_date = date_var.get()

    if not selected_city or not selected_date:
        print("Please select both a city and a date.")
        return

    # Filter data
    filtered_data = [
        entry for entry in data
        if entry["city"] == selected_city and entry["timestamp"].startswith(selected_date)
    ]

    if not filtered_data:
        print("No data found for this city and date.")
        return

    # Extract timestamps and temperatures
    times = [
        datetime.fromisoformat(entry["timestamp"]).strftime("%H:%M")
        for entry in filtered_data
    ]
    temps = [entry["temperature_c"] for entry in filtered_data]

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker="o", linestyle="-", color="blue", label=selected_city)
    plt.title(f"Temperature Trend on {selected_date} in {selected_city}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    plt.show()

# Button
tk.Button(root, text="Plot Weather", command=plot_weather).pack(pady=10)

root.mainloop()
