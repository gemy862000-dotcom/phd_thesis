from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class DataPreprocessor:
    def encode_categorical(self, df):
        df = df.copy()
        for col in df.select_dtypes(include=["object"]).columns:
            df[col] = LabelEncoder().fit_transform(df[col].astype(str))
        return df

    def split(self, df, target_col, test_size=0.2, random_state=42):
        X = df.drop(columns=[target_col])
        y = df[target_col]
        return train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )
