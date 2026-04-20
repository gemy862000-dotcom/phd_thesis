import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)


class DatasetLoader:
    def load_csv(self, path: str) -> pd.DataFrame:
        logger.info(f"Loading dataset from {path}")
        return pd.read_csv(path)

    def validate_columns(self, df: pd.DataFrame, required_columns):
        missing = [c for c in required_columns if c not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        logger.info("Dataset validation passed.")
