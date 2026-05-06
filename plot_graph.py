import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

log_file = "temperature_log.csv"

def animate(i):
    try:
        data = pd.read_csv(log_file, names=["Time", "Temp"])
        data["Time"] = pd.to_datetime(data["Time"])
        plt.cla()
        plt.plot(data["Time"], data["Temp"], label="Temperature (°C)", color="red")
        plt.xlabel("Time")
        plt.ylabel("Temp (°C)")
        plt.title("Live Temperature Readings")
        plt.xticks(rotation=45)
        plt.tight_layout()
    except Exception as e:
        print("Waiting for data...")

fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, interval=2000)
#plt.savefig("plot.png")
plt.show()
