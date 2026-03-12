import pandas as pd

def profile_dataset(file_path):
    df = pd.read_csv(file_path)
    metadata = {
        "columns": list(df.columns),
        "column_types": df.dtypes.astype(str).to_dict(),
        "summary": df.describe().to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
    }
    return metadata