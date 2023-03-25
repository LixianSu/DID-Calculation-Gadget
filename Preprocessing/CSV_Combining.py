import pandas as pd
import csv
import os


def txttocsv(path):
    # get all the CSV files in the path
    all_files = os.listdir(path)
    print(all_files)
    for file in all_files:
        if file.endswith(".txt"):
            input_file = file
            output_file = file.replace(".txt", ".csv")

            with open(os.path.join(path, input_file), 'r') as in_file, open(os.path.join(path, output_file), 'w', newline='') as out_file:
                # Create a CSV writer object
                csv_writer = csv.writer(out_file)

                # Read each line of the input file
                for line in in_file:
                    # Split the line into fields using tabs as the delimiter
                    fields = line.strip().split('\t')

                    # Write the fields to the CSV file
                    csv_writer.writerow(fields)
                out_file.close()
            os.remove(os.path.join(path, file))

def combine(path):
    all_files = os.listdir(path)
    # create an empty dataframe to hold the merged data
    merged_data = pd.DataFrame()

    # iterate through each file and append its data to the merged_data dataframe
    for file in all_files:
        if file.endswith('.csv'):
            # read the CSV file into a dataframe
            df = pd.read_csv(os.path.join(path, file), low_memory=False)

            # append the data to the merged_data dataframe
            # merged_data = merged_data.append(df)
            merged_data = pd.concat([merged_data, df])
            os.remove(os.path.join(path, file))
        print("Running {0}th file...\n".format(str(all_files.index(file) + 1)))
    # save the merged data to a new CSV file
    merged_data.to_csv(os.path.join(path, "merged_data.csv"), index=False)
