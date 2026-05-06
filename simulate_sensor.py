import time
import random
from datetime import datetime

log_file = "temperature_log.csv"

while True:
    # Generate random temp between 20 and 45°C
    temp = round(random.uniform(20.0, 45.0), 2)
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create log line
    line = f"{timestamp},{temp}\n"
    
    # Write to file
    with open(log_file, "a") as f:
        f.write(line)
    
    print(f"Logged: {line.strip()}")
    
    # Wait 5 seconds before next reading
    time.sleep(5)
