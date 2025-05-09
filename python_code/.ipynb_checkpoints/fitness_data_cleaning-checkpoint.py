# Data manipulation and analysis
import pandas as pd
import numpy as np
import openpyxl

# Date and time handling
from datetime import datetime

# Importing the dataset 
df = pd.read_excel("C:/Users/hp/OneDrive/Desktop/Fitness_health_analysis/data/raw_data/health_fitness_dataset.xlsx")


# Removing Null values 
null_rows = df[df.isnull().any(axis=1)]
print(f"Total rows with at least one null: {len(null_rows)}") 

null_removed_df= df.dropna()
print(f"Total rows left after removing null valaues : {len(null_removed_df)}") 

#Total rows with at least one null: 490275
#Total rows left after removing null valaues : 197426

# Strip whitespace from column names 
null_removed_df = null_removed_df.columns.str.strip()

# Export cleaned DataFrame to an Excel file
null_removed_df.to_excel("cleaned_health_fitness_data.xlsx", index=False)
