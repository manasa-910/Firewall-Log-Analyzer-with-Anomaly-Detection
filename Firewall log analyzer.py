import time
import re
import pandas as pd
import requests
from sklearn.ensemble import IsolationForest

log_file_path = r"C:\Windows\System32\LogFiles\Firewall\pfirewall.log"

pattern = r"(?P<timestamp>[\d-]+\s[\d:]+)\s(?P<action>\w+)\s(?P<protocol>\w+)\s(?P<source_ip>[\d\.:a-fA-F]+)\s(?P<destination_ip>[\d\.:a-fA-F]+)\s(?P<source_port>\d+)\s(?P<destination_port>\d+)"

# Function to read all logs
def read_firewall_logs():
    with open(log_file_path, "r") as file:
        logs = file.readlines()
    
    log_data = []
    for log_entry in logs:
        match = re.search(pattern, log_entry)
        if match:
            log_data.append(match.groupdict()) 
    
    return pd.DataFrame(log_data) if log_data else pd.DataFrame()  

# Read all logs
df = read_firewall_logs()

if not df.empty:
    # Convert categorical data to numeric for Isolation Forest
    df['protocol'] = df['protocol'].astype('category').cat.codes  
    df['source_port'] = df['source_port'].astype(int)
    df['destination_port'] = df['destination_port'].astype(int)

    # Train Isolation Forest
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(df[['protocol', 'source_port', 'destination_port']])
    df.to_csv("firewall_anomalies.csv", index=False)

    print("Log analysis completed. Anomalies saved in 'firewall_anomalies.csv'")


# Function to send alerts
def send_alert(message):
    bot_token = "<your telegram bot token>"  
    chat_id = "<telegram chat id>"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, data=data)
send_alert("🚨 Firewall Alert! Suspicious activity detected.")
