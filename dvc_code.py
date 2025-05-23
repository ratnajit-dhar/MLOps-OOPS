import pandas as pd
import os
# Create a simple dataset
data = {
    "feature": [1, 2, 3, 4],
    "target": [2, 4, 6, 8]
}

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'data.csv')
# Save to CSV
df.to_csv(file_path, index=False)


