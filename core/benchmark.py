from utils.metrics import classification_metrics


class BenchmarkEngine:
    def evaluate_classification(self, model, X_test, y_test):
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)
        return classification_metrics(y_test, y_pred, y_prob)

    def compare_models(self, model_results: dict):
        return sorted(
            model_results.items(),
            key=lambda item: item[1].get("f1", 0),
            reverse=True
        )
