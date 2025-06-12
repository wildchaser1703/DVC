import pandas as pd
import os


# Create a sample dataframe with the columns below
data = {"Name" : ["Kevin", "Jim", "Dwight"],
        "Age" : [20, 30, 21],
        "City" : ["Baltimore", "Houston", "Boston"]}

df = pd.DataFrame(data)

# Add a new row to the df
# new_row_loc = {"Name" : "V1", "Age" : 20, "City" : "Bangalore"}
# df.loc[len(df.index)] = new_row_loc

## Add a new row to df for V3
# new_row_loc2 = {"Name" : "V3", "Age" : 40, "City" : "Bangalore"}
# df.loc[len(df.index)] = new_row_loc2

# Ensure that the data exists at the root level
data_dir = "data"
os.makedirs(data_dir, exist_ok = True)

# Define the file path
file_path = os.path.join(data_dir, "sampledata.csv")

# Save the dataframe to a CSV file, including column names
df.to_csv(file_path, index = False)

print(f"File saved to specified path")