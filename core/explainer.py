import pandas as pd
import shap


class ExplainabilityEngine:
    def explain_tabular_model(self, model, X_sample: pd.DataFrame):
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_sample)

        summary = []
        for idx in range(min(len(X_sample), 5)):
            feature_impact = {}
            if isinstance(shap_values, list):
                row_vals = shap_values[1][idx]
            else:
                row_vals = shap_values[idx]

            for col, val in zip(X_sample.columns, row_vals):
                feature_impact[col] = float(val)

            summary.append({
                "instance_index": idx,
                "feature_impacts": feature_impact
            })
        return summary

    def tester_friendly_explanation(self, explanation: dict) -> str:
        impacts = explanation.get("feature_impacts", {})
        top_features = sorted(
            impacts.items(), key=lambda x: abs(x[1]), reverse=True
        )[:3]
        reasons = ", ".join([f"{k} ({v:.3f})" for k, v in top_features])
        return f"The prediction was mainly influenced by: {reasons}."
