import pandas as pd
import pyarrow as pa

# The equivalent to a pandas DataFrame is an Arrow Table. They both consist of 
# named columns of equal length. Pandas only support flat columns, however,
# the Arrow Table provides support for nested columns!
pd_df = pd.DataFrame({"Wilhelm": [98, 12, 12], "Tux": [96, 0, 0]})
pa_table = pa.Table.from_pandas(pd_df)

# Convert back to pandas DataFrame and infer the used schema.
pd_df_new = pa_table.to_pandas()
pa_schema = pa.Schema.from_pandas(pd_df)

print(pa_schema)
