from sklearn.ensemble import RandomForestClassifier
from models.base_model import BaseModel


class DefectPredictionModel(BaseModel):
    def __init__(self, random_state=42):
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=random_state,
            class_weight="balanced"
        )

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def predict_proba(self, X_test):
        if hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(X_test)[:, 1]
        return None
