import joblib
import pandas as pd

# Load trained model
model = joblib.load("intrusion_model.pkl")

print("Intrusion Detection System Ready")

# Feature names used during training (41 features)
feature_names = [
'duration','protocol_type','service','flag','src_bytes','dst_bytes',
'land','wrong_fragment','urgent','hot','num_failed_logins','logged_in',
'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
'num_shells','num_access_files','num_outbound_cmds','is_host_login',
'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
'dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate',
'dst_host_rerror_rate','dst_host_srv_rerror_rate'
]

# Example input data
sample_values = [[
0,1,24,5,181,5450,0,0,0,0,
0,1,0,0,0,0,0,0,0,0,
0,0,9,9,0,0,0,0,1,0,
0,9,9,1,0,0,0,0,0,0,0
]]

# Create dataframe with correct column names
sample_data = pd.DataFrame(sample_values, columns=feature_names)

# Predict
prediction = model.predict(sample_data)

print("\nPrediction:", prediction[0])
