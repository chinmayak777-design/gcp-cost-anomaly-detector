import requests, json
from datetime import datetime
import config, sample_data

class CostAnomalyDetector:
    def __init__(self):
        self.webhook_url = config.SLACK_WEBHOOK_URL
        self.threshold = config.COST_SPIKE_THRESHOLD
    def get_costs(self):
        return sample_data.get_sample_costs(simulate_spike=config.DEMO_SPIKE)
    def detect_anomaly(self, costs):
        current, previous = costs["current_month"], costs["previous_month"]
        pct = ((current - previous) / previous) * 100 if previous else 0
        is_anomaly = pct > (self.threshold * 100)
        return is_anomaly, pct, current - previous
    def send_slack_alert(self, costs, spike_pct, spike_amt):
        msg = {"text": "🚨 Cost Spike!", "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": f"*Cost Alert*\nPrev: ${costs['previous_month']}\nCurr: ${costs['current_month']}\nSpike: {spike_pct:.1f}%"}}]}
        try:
            requests.post(self.webhook_url, json=msg, timeout=10)
            print("✅ Alert sent!")
        except: print("❌ Error")
    def log_result(self, costs, is_anomaly, pct):
        try:
            with open(config.LOG_FILE, "a") as f:
                f.write(json.dumps({"timestamp": datetime.now().isoformat(), "current": costs["current_month"], "previous": costs["previous_month"], "spike_pct": pct, "anomaly": is_anomaly}) + "\n")
        except: pass
    def run(self):
        print("\n🔍 GCP Cost Detector\n")
        costs = self.get_costs()
        is_anomaly, pct, amt = self.detect_anomaly(costs)
        print(f"Previous: ${costs['previous_month']}\nCurrent: ${costs['current_month']}\nSpike: {pct:.1f}%\nStatus: {'🚨 ANOMALY' if is_anomaly else '✅ Normal'}\n")
        if is_anomaly: self.send_slack_alert(costs, pct, amt)
        self.log_result(costs, is_anomaly, pct)

if __name__ == "__main__":
    CostAnomalyDetector().run()
