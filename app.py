from flask import Flask, render_template
import pandas as pd
import os
import time

app = Flask(__name__)
LOG_FILE = os.path.abspath("temperature_log.csv")

@app.route("/")
def index():
    if not os.path.exists(LOG_FILE):
        return "❌ No temperature log found."

    try:
        # Update the plot image before rendering
        os.system("python3 plot.py")

        data = pd.read_csv(LOG_FILE, names=["Time", "Temp"])
        data["Time"] = pd.to_datetime(data["Time"])

        current = data["Temp"].iloc[-1]
        max_temp = data["Temp"].max()
        min_temp = data["Temp"].min()
        avg_temp = round(data["Temp"].mean(), 2)

        logs = data.tail(10).to_records(index=False)

        return render_template("index.html",
                               current=current,
                               max_temp=max_temp,
                               min_temp=min_temp,
                               avg_temp=avg_temp,
                               logs=logs,
                               plot_path=f"/static/plot.png?{int(time.time())}")  # cache bust

    except Exception as e:
        return f"⚠️ Error reading file: {e}"

if __name__ == "__main__":
    app.run(debug=True)
