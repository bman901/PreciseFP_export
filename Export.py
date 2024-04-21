import pygsheets
import pandas as pd
import ReadPDF2
import PreciseFP

#authorization
gc = pygsheets.authorize(service_file='precisefp-export-0fd576e4697f.json')

# Create empty dataframe
df = pd.DataFrame()

# Import from Illustration PDF
df['Loan Amount'] = [ReadPDF2.loan_amount()]

# Dataset keys
data_keys = ['76af54f2-74ce-4e4e-8920-f9722269915c','92f5d070-62c6-42bb-a40a-1f6b232af506']
# (Test data. Store the real keys in a text file as a dictionary and loop through)

# Loop in data from PreciseFP
PFPdata = PreciseFP.get_engagement_data()
for data in PFPdata:
    if data['dataset_id'] in data_keys:
        df[data['title']] = [data['value']]

#open the google spreadsheet (by key)
sh = gc.open_by_key('1K2LrDE25ObdEIiLXdmEN0KT9K08e019LdESoo9PxQ-M')

#select the first sheet
wks = sh[0]

#update the first sheet with df, starting at cell A1.
wks.set_dataframe(df,(1,1))

print('Data export complete')