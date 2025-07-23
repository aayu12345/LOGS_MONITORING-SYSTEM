# streamlit_app.py
# import streamlit as st
# import pandas as pd
# import requests

# st.title("Logs Classification System")

# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
# if uploaded_file is not None:
#     if st.button("Classify Logs"):
#         files = {"file": uploaded_file.getvalue()}
#         response = requests.post("http://localhost:8000/classify/", files={"file": uploaded_file})
#         if response.status_code == 200:
#             st.success("Classification Done! Click below to download:")
#             st.download_button("Download CSV", response.content, file_name="classified_logs.csv")
#         else:
#             st.error(response.json()["detail"])

import streamlit as st
import pandas as pd
from classify_logs import classify  # Ensure this is your function

st.title("Logs Classification System")

uploaded_file = st.file_uploader("Upload CSV file (with 'source' and 'log_message' columns)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if "source" not in df.columns or "log_message" not in df.columns:
        st.error("CSV must contain 'source' and 'log_message' columns.")
    else:
        if st.button("Classify Logs"):
            # Apply your classify function
            df['target_label'] = classify(list(zip(df['source'], df['log_message'])))
            st.success("Classification complete!")

            # Display results as table
            st.subheader("Classified Results")
            st.dataframe(df)

            # Prepare downloadable CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Classified Logs as CSV",
                data=csv,
                file_name="classified_logs.csv",
                mime="text/csv"
            )
