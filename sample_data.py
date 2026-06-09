"""
Sample cost data for testing
Simulates GCP billing data without needing real GCP account
"""

def get_sample_costs(simulate_spike=False):
    """
    Returns fake GCP cost data
    
    Args:
        simulate_spike: If True, returns costs with spike
        
    Returns:
        Dictionary with cost information
    """
    
    # Normal scenario (no spike)
    normal_costs = {
        "current_month": 45.23,
        "previous_month": 38.50,
        "daily_costs": [
            1.45, 1.52, 1.48, 1.55, 1.50,
            1.53, 1.49, 1.51, 1.54, 1.50,
            1.52, 1.48, 1.53, 1.49, 1.51,
        ],
        "services": {
            "Compute Engine": 28.50,
            "Cloud Storage": 12.30,
            "Cloud SQL": 4.43,
        },
        "timestamp": "2024-06-09T14:30:00Z"
    }
    
    # Spike scenario
    spike_costs = {
        "current_month": 48.50,
        "previous_month": 38.50,
        "daily_costs": [
            1.45, 1.52, 1.48, 1.55, 1.50,
            1.53, 1.49, 1.51, 1.54, 1.50,
            2.89, 3.15, 3.05, 3.10, 3.08,
        ],
        "services": {
            "Compute Engine": 28.50,
            "Cloud Storage": 18.50,
            "Cloud SQL": 1.50,
        },
        "timestamp": "2024-06-09T14:30:00Z"
    }
    
    if simulate_spike:
        return spike_costs
    else:
        return normal_costs


if __name__ == "__main__":
    print("Normal costs:")
    print(get_sample_costs(simulate_spike=False))
    
    print("\nSpiked costs:")
    print(get_sample_costs(simulate_spike=True))
