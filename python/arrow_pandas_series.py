import pandas as pd
import pyarrow as pa
import numpy as np

# The most similar structure to a pandas Series is the Arrow Array.
# It is a vector that contains data of the same type as linear,
# contiguous, memory.
pd_ser = pd.Series([1, 1, 2, 3, 5, None, 8])
pa_arr = pa.array(pd_ser, from_pandas=True)

print(f'The Arrow array looks like:\n{pa_arr}')
