import pandas as pd
import os

# Directory containing the Excel files
folder_path = 'TT_TN'
all_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.xlsx') or file.endswith('.xls')]

# List to hold dataframes
df_list = []

# Read each Excel file and append to the list
for file in all_files:
    df_list.append(pd.read_excel(file))

# Concatenate all dataframes in the list
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined dataframe to an output Excel file
output_file = 'dataset_tn_tt.xlsx'
combined_df.to_excel(output_file, index=False)

print(f"Combined dataset saved to {output_file}")