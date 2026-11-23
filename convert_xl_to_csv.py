import pandas as pd

# Read Excel file
excel_file = r"E:\flouride\Fluoride_Adsorption_FULL_RANGE_Experimental_Plan.xlsx"   # change file name
df = pd.read_excel(excel_file)

# Save as CSV
df.to_csv("output.csv", index=False)

print("Excel converted to CSV successfully!")
