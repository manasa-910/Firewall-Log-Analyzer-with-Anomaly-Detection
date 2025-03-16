import time
import pandas as pd
# Monitor logs for anomalies
def monitor_logs():
    print("Monitoring logs for anomalies...")

    while True:
        try:
            df = pd.read_csv("firewall_anomalies.csv")  # Read latest logs
            time.sleep(10)  # Check logs every 10 seconds
        except Exception as e:
            print(f"❌ Error in monitoring logs: {e}")
            time.sleep(10)  # Wait before retrying

monitor_logs()  # Start monitoring after defining everything