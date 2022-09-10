import numpy as np
import pyarrow as pa

np_arr = np.arange(20, dtype='int16')
pa_arr = pa.array(np_arr)

print(f'The Arrow array looks like:\n{pa_arr}')

# Convert back to Numpy array
np_arr_new = pa_arr.to_numpy()

print(f'The converted Numpy array looks like:\n{np_arr_new}')
