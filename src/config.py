import numpy as np

# Given retention metrics
days_known = np.array([1, 3, 7, 14]) #Given days in the case

retention_a_known = np.array([0.53, 0.27, 0.17, 0.06]) #Retention rates for given days
retention_b_known = np.array([0.48, 0.25, 0.19, 0.09]) 

# Player Count Metric
daily_installs = 20000

# Monetization Metrics
arppu = 10.0  # Assumption, average purchase amount, dollars

purchase_rate_a = 0.0305  # %3.05
ecpm_a = 9.80             #dollars
ad_imp_per_dau_a = 2.3

purchase_rate_b = 0.0315  # %3.15
ecpm_b = 10.80            #dollars
ad_imp_per_dau_b = 1.6

# E CASE: New Parameters
params_a_new_source = [0.58, 0.12] # Variant A New: Retention = 0.58 * e^(-0.12 * (x-1))
params_b_new_source = [0.52, 0.10] # Variant B New: Retention = 0.52 * e^(-0.10 * (x-1))