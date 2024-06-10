import streamlit as st
import pandas as pd

# Title of the app
st.title("CSV File Uploader and Editor")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the editable dataframe
    st.write("Here's the data from the uploaded CSV file:")
    edited_df = st.experimental_data_editor(df, use_container_width=True)

    # Input for the new column name
    new_column_name = st.text_input("Enter the new column name")

    if new_column_name:
        # Input for default value for new column
        default_value = st.text_input("Enter the default value for the new column", key="default_value")

        if st.button("Add New Column"):
            # Add the new column with default values
            edited_df[new_column_name] = default_value

            # Display the updated dataframe
            st.write("Updated DataFrame with the new column:")
            st.experimental_data_editor(edited_df, use_container_width=True)

            # Convert updated dataframe to CSV for download
            csv = edited_df.to_csv(index=False).encode('utf-8')

            # Download button
            st.download_button(
                label="Download Updated CSV",
                data=csv,
                file_name='updated_data.csv',
                mime='text/csv',
            )
else:
    st.write("Please upload a CSV file to proceed.")
