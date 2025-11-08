import pandas as pd
import json

# Read Excel file
df = pd.read_excel('Ceník NV 2025 FINAL.xlsx', header=None)

data = []
current_category = None

for idx, row in df.iterrows():
    # Check if this row has a category
    category_val = row[1]
    if pd.notna(category_val) and str(category_val) != 'Kategorie vozidla' and 'Unnamed' not in str(category_val):
        current_category = str(category_val)
    
    # Check if this row has vehicle data
    znacka_typ = row[4]
    cena_1_10 = row[17]
    cena_11_30 = row[18]
    
    if pd.notna(znacka_typ) and pd.notna(cena_1_10) and pd.notna(cena_11_30):
        try:
            data.append({
                'kategorie': current_category if current_category else '',
                'znacka_typ': str(znacka_typ).strip(),
                'cena_1_10_dni': int(cena_1_10),
                'cena_11_30_dni': int(cena_11_30)
            })
        except (ValueError, TypeError):
            pass

# Output as JavaScript array format
print('const ceníkData = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';')

