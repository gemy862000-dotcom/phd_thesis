import pandas as pd


class TestPrioritizationModel:
    def prioritize(self, test_cases: pd.DataFrame) -> pd.DataFrame:
        required = ["test_id", "historical_failures", "execution_time", "changed_files"]
        missing = [c for c in required if c not in test_cases.columns]
        if missing:
            raise ValueError(f"Missing columns for prioritization: {missing}")

        df = test_cases.copy()
        df["priority_score"] = (
            (df["historical_failures"] * 0.5) +
            (df["changed_files"] * 0.4) -
            (df["execution_time"] * 0.1)
        )
        return df.sort_values(by="priority_score", ascending=False)
