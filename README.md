# **Firewall Log Analyzer with Anomaly Detection 🚀**  

## **Overview**  
This project analyzes Windows Firewall logs (`pfirewall.log`) to detect suspicious activities using **Isolation Forest**. It also provides a **real-time dashboard** to visualize log data and detected anomalies. Additionally, it sends alerts via **Telegram** when anomalies are detected.  

## **Features**  
- **Real-time Firewall Log Monitoring** – Reads logs from `pfirewall.log`.  
- **Anomaly Detection** – Uses **Isolation Forest** to flag suspicious activities.  
- **Interactive Dashboard** – Displays logs, anomaly trends, and visual insights.  
- **Telegram Alerts** – Notifies admins about detected anomalies.  

## **Installation**  
### **1️⃣ Install Dependencies**  
```sh
pip install flask pandas scikit-learn requests
```

### **2️⃣ Monitor the logs**  
```sh
python "monitor.py"  # Monitors logs and detects anomalies
```

### **3️⃣ Start the Dashboard**  
```sh
python "Dashboard.py"  # Launches the web dashboard
```
Visit **`http://127.0.0.1:5000/`** to view logs and anomalies. 

### **4️⃣ Save the monitored information in a file**  
```sh
python "Firewall log analyzer.py"  # Saves the monitored information
```

## **Usage**  
- **Monitor logs** for blocked/allowed traffic.  
- **Identify suspicious activity** via the anomaly detection model.  
- **Check the dashboard** for real-time log visualization.  
- **Receive alerts** on Telegram for critical anomalies.  

## **Dashboard Features**  
- **Log Table** – View recent firewall logs.  
- **Anomaly Trends** – Detect unusual patterns in network traffic.  
- **Geo-Location Mapping** – Identify source locations of flagged IPs.  

## **Contributing**  
Feel free to improve the project by adding features or optimizing the ML model.  

