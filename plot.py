import pandas as pd
import matplotlib.pyplot as plt

log_file = "temperature_log.csv"
output_file = "static/plot.png"

try:
    data = pd.read_csv(log_file, names=["Time", "Temp"])
    data["Time"] = pd.to_datetime(data["Time"])

    plt.figure(figsize=(8, 4))
    plt.plot(data["Time"], data["Temp"], label="Temperature (°C)", color="red")
    plt.xlabel("Time")
    plt.ylabel("Temp (°C)")
    plt.title("Live Temperature Plot")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()
except Exception as e:
    print("Plot error:", e)
