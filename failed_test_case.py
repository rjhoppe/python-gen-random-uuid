import uuid
import pandas as pd

# Have new dataset that you would like to merge 
# with existing_data.csv
data = pd.DataFrame({
    "id": [1,2,3,4,5,6],
    "value": [40,20,10,20,30,30],
    'value2': [1,1,1,0,0,1]
})

data = data.set_index('id')

# print(data)

existing = pd.read_csv('existing_data.csv')
existing = existing.set_index('id')

combined = pd.concat([existing, data], verify_integrity=True)
# Receive error: "Indexes have overlapping values"
# Can manually change the conflicting ideas, but this
# is not scalable 
print(combined)



