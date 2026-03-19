import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("intrusion_model.pkl")

st.title("Network Intrusion Detection System")

st.write("Enter network traffic parameters to detect intrusion.")

# Feature names
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

# Input fields
user_input = []

for feature in feature_names:
    value = st.number_input(feature, value=0.0)
    user_input.append(value)

# Predict button
if st.button("Detect Intrusion"):

    input_df = pd.DataFrame([user_input], columns=feature_names)

    prediction = model.predict(input_df)

    if prediction[0] == "attack":
        st.error("⚠️ Intrusion Detected!")
    else:
        st.success("✅ Normal Traffic")

# Feature Importance
st.subheader("Feature Importance")

importances = model.feature_importances_

fig, ax = plt.subplots()
ax.barh(feature_names[:15], importances[:15])

st.pyplot(fig)
