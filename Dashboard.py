from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def parse_firewall_log(filepath):
    """Reads `pfirewall.log`, extracts relevant fields, and marks anomalies."""
    with open(filepath, "r") as file:
        lines = file.readlines()

    data = []
    headers = None

    for line in lines:
        line = line.strip()
        
        if not line or line.startswith("#"):  
            continue  # Skip empty lines or comments
        
        if headers is None:
            headers = line.split(",")  # Extract column names
            headers.append("Anomaly")  # Add a new column for anomalies
        else:
            values = line.split(",")
            if len(values) == len(headers) - 1:  
                row = dict(zip(headers[:-1], values))  
                
                if row.get("Event") == "Blocked":  
                    row["Anomaly"] = "Yes"  # Mark as an anomaly
                else:
                    row["Anomaly"] = "No"   # Mark as normal
                
                data.append(row)  # Append row to data

    return data

@app.route('/')
def home():
    filepath = "firewall_anomalies.csv"  # Change as needed

    try:
        data = parse_firewall_log(filepath)  # Parse log file
        print("DEBUG DATA:", data[:5])  # Print first 5 rows for debugging
    except Exception as e:
        data = [{"Error": f"Failed to read log file: {e}"}]  # Show error in HTML

    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
