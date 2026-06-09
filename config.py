import os
from dotenv import load_dotenv
load_dotenv()
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/services/YOUR_WEBHOOK_URL_HERE")
COST_SPIKE_THRESHOLD = 0.20
AVERAGE_MONTHLY_COST = 45.00
PROJECT_NAME = "GCP Cost Anomaly Detector"
VERSION = "1.0.0"
ALERT_ENABLED = True
LOG_FILE = "cost_check.log"
DEMO_MODE = True
DEMO_SPIKE = False
