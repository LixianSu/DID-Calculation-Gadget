import os
import pandas as pd

def merge_csv_files(folder_path, output_file):
    # Get a list of all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Initialize an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    # Iterate through each CSV file and merge it with the existing data
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        data = pd.read_csv(file_path)
        merged_data = merged_data.append(data)

    # Write the merged data to the output file
    merged_data.to_csv(output_file, index=False)
    print("CSV files merged successfully!")

# Provide the folder path containing CSV files and the output file name
folder_path = 'B:/1'
output_file = 'B:/1/denmarkk.csv'

# Call the function to merge CSV files
merge_csv_files(folder_path, output_file)