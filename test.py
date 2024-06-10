import streamlit as st
import pandas as pd

def main():
    st.title("CSV Column Adder")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        st.write("Current DataFrame:")
        st.write(df)

        # Add new column
        new_column_name = st.text_input("Enter the name of the new column:")
        if new_column_name:
            default_value = st.text_input("Enter the default value for the new column:")

            if st.button("Add Column"):
                if new_column_name in df.columns:
                    st.warning("Column already exists!")
                else:
                    df[new_column_name] = default_value
                    st.success(f"Column '{new_column_name}' added!")
                    st.write("Updated DataFrame:")
                    st.write(df)

        # Download updated CSV
        st.download_button(
            label="Download updated CSV",
            data=df.to_csv(index=False),
            file_name='updated_data.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
