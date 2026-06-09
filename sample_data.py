def get_sample_costs(simulate_spike=False):
    normal_costs = {"current_month": 45.23, "previous_month": 38.50, "daily_costs": [1.45, 1.52, 1.48, 1.55, 1.50, 1.53, 1.49, 1.51, 1.54, 1.50, 1.52, 1.48, 1.53, 1.49, 1.51], "services": {"Compute Engine": 28.50, "Cloud Storage": 12.30, "Cloud SQL": 4.43}, "timestamp": "2024-06-09T14:30:00Z"}
    spike_costs = {"current_month": 48.50, "previous_month": 38.50, "daily_costs": [1.45, 1.52, 1.48, 1.55, 1.50, 1.53, 1.49, 1.51, 1.54, 1.50, 2.89, 3.15, 3.05, 3.10, 3.08], "services": {"Compute Engine": 28.50, "Cloud Storage": 18.50, "Cloud SQL": 1.50}, "timestamp": "2024-06-09T14:30:00Z"}
    return spike_costs if simulate_spike else normal_costs
