import pandas as pd
data = pd.read_csv('Seals.csv')

data = scaling(data, a = (0, 8), b = (10, 12), columnIndices = (0, 1))
data.to_csv('SealsScaled.csv')