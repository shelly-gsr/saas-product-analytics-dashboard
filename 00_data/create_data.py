import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n_users = 500

# Generate random signup dates within the last 2 years
signup_dates = pd.to_datetime(
    np.random.choice(pd.date_range(start='2021-01-01', end='2023-01-01'), n_users)
)

# Generate last active dates after signup
last_active_dates = [
    signup + timedelta(days=int(np.random.exponential(scale=90))) 
    for signup in signup_dates
]

# Other columns
plan_types = ['free', 'basic', 'premium']
regions = ['NA', 'EU', 'APAC']

data = pd.DataFrame({
    'user_id': range(1001, 1001 + n_users),
    'signup_date': signup_dates,
    'last_active_date': last_active_dates,
    'plan_type': np.random.choice(plan_types, n_users, p=[0.4, 0.4, 0.2]),
    'num_logins': np.random.poisson(lam=15, size=n_users),
    'num_features_used': np.random.randint(1, 11, n_users),
    'avg_session_length': np.round(np.random.normal(loc=10, scale=3, size=n_users), 1),
    'region': np.random.choice(regions, n_users, p=[0.5, 0.3, 0.2])
})

# Determine churn: if last active date is more than 60 days ago from today
today = pd.to_datetime('2023-03-01')
data['churned'] = data['last_active_date'] < (today - pd.Timedelta(days=60))

# Save to CSV
data.to_csv('synthetic_saas_user_data.csv', index=False)
print(data.head())