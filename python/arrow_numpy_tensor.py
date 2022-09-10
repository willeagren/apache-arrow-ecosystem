import numpy as np
import pyarrow as pa

# Arrow arrays only support one dimensional data, as such,
# we have to resort to using the Tensor struct to store our
# numpy ndarray. Furthermore, this could represent a usual
# ndarray found in deep learning scenarios and I then we can 
# specify the dimension names as to what they represent in the data.
np_arr = np.random.uniform(-1.0, 1.0, size=(128, 3, 256, 256))
dim_names = [
    'batch_size',
    'convolution_depth',
    'image_width',
    'image_height'
]
pa_t = pa.Tensor.from_numpy(np_arr, dim_names=dim_names)

print(f'The Arrow tensor looks like:\n{pa_t}')
print(f'and has dimension names:\n{dim_names}')

# Convert back to Numpy ndarray
np_arr_new = pa_t.to_numpy()
print(f'The converted Tensor has ndarray shape:\n{np_arr_new.shape}')
