import numpy as np
import pandas as pd
from src.models import exponential_decay

def calculate_daily_revenue(dau, day, purchase_rate, arppu, ad_imp, ecpm):
    purchase_rev = dau * purchase_rate * arppu # In-App Purchase revenue
    ad_rev = dau * ad_imp * (ecpm / 1000) # Ad revenue
    return purchase_rev + ad_rev

def simulate_scenario(params, daily_installs, 
                      purchase_rate, arppu, ad_imp, ecpm, 
                      duration_days=30, apply_sale=False): 
    
    a, b = params
    history_days = np.arange(1, duration_days + 1) # Create an array till desired day
    history_dau = [] # Collect DAU till desired day
    history_revenue = [] # Collect revenue

    for day in history_days:
        # DAU calculation
        if day == 1:
            dau = daily_installs # First day, no player retention
        else:
            prev_days = np.arange(1, day)
            retention_rates = exponential_decay(prev_days, a, b)
            dau = daily_installs * (1 + np.sum(retention_rates))
        
        current_purchase_rate = purchase_rate

        if apply_sale and 15 <= day < 25: # Deployed when sales are issued
            current_purchase_rate = purchase_rate + 0.01
            
        daily_rev = calculate_daily_revenue(dau, day, current_purchase_rate, arppu, ad_imp, ecpm)
        
        history_dau.append(int(dau))
        history_revenue.append(daily_rev)

    df = pd.DataFrame({
        'Day': history_days,
        'DAU': history_dau,
        'Daily_Revenue': history_revenue })
    
    df['Total_Revenue'] = df['Daily_Revenue'].cumsum()
    
    return df