import pandas as pd
class GatewayAnalysis:
    @staticmethod
    def automate_gateway_analysis(gateway_df, gateway_report_df):
        """
        Automates the task of merging two files and filtering based on conditions.

        Parameters:
        - gateway_df (pd.DataFrame): DataFrame containing Gateway details.
        - gateway_report_df (pd.DataFrame): DataFrame containing Gateway reports.

        Returns:
        - pd.DataFrame: The filtered DataFrame.
        """
        # Select necessary columns
        columns_to_keep = ['Gateway No.', 'Subdivision']
        gateway = gateway_df[columns_to_keep]

        # Merge the data
        merged_df = pd.merge(gateway, gateway_report_df, how='inner', left_on='Gateway No.', right_on='Name')

        # Filter the data based on conditions
        filtered_df = merged_df[
            (merged_df["device_uptime(--_value)"] < 90) |
            (merged_df["network_uptime(--_value)"] < 90)
            ]

        return filtered_df

