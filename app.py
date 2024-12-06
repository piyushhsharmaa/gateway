import streamlit as st
import pandas as pd
from func import GatewayAnalysis

st.title("Gateway Analysis Dashboard")

st.sidebar.title("Upload Files")
gateway_file = st.sidebar.file_uploader("Installed gateways details.csv", type="csv", key="gateway_file")
report_file = st.sidebar.file_uploader("devices.csv", type="csv", key="report_file")

if gateway_file and report_file:
    # Read uploaded files into DataFrames
    gateway_df = pd.read_csv(gateway_file)
    report_df = pd.read_csv(report_file)

    # Analyze data
    filtered_df = GatewayAnalysis.automate_gateway_analysis(gateway_df, report_df)

    # Display the filtered data
    st.subheader("Filtered Gateways")
    st.dataframe(filtered_df)

    # Option to download the filtered data
    download_path = st.sidebar.text_input("Enter file name for download (e.g., filtered_report.csv)",
                                          key="download_path")
    if st.sidebar.button("Download", key="download_button"):
        filtered_df.to_csv(download_path, index=False)
        st.sidebar.success(f"File saved as {download_path}")
else:
    st.info("Please upload both Gateway Details and Gateway Report CSV files to proceed.")