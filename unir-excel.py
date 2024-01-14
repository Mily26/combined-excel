import pandas as pd

# Read the first Excel file and sheet
df1 = pd.read_excel('cantidades.xlsx', 'Hoja1')

# Read the second Excel file and sheet
df2 = pd.read_excel('errores.xlsx', 'Sheet1')

# Concatenate the two DataFrames
df_unido = pd.concat([df1, df2])

# Create an ExcelWriter object
with pd.ExcelWriter('combined_excel.xlsx') as writer:
    # Write each DataFrame to a different sheet
    df1.to_excel(writer, sheet_name='Cantidades', index=False)
    df2.to_excel(writer, sheet_name='Errores', index=False)