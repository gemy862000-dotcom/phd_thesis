from data.loader import DatasetLoader
from data.preprocess import DataPreprocessor
from models.defect_prediction import DefectPredictionModel
from models.test_prioritization import TestPrioritizationModel
from models.self_healing import SelfHealingEngine
from models.test_generation import TestCaseGenerationEngine
from core.explainer import ExplainabilityEngine
from core.benchmark import BenchmarkEngine
from core.ci_cd import CICDIntegration


class IntegratedAITestAutomationFramework:
    def __init__(self, config):
        self.config = config
        self.loader = DatasetLoader()
        self.preprocessor = DataPreprocessor()
        self.defect_model = DefectPredictionModel(random_state=config.random_state)
        self.prioritizer = TestPrioritizationModel()
        self.self_healer = SelfHealingEngine()
        self.test_generator = TestCaseGenerationEngine()
        self.explainer = ExplainabilityEngine()
        self.benchmark = BenchmarkEngine()
        self.cicd = CICDIntegration()

    def run_defect_prediction(self, csv_path: str, target_col: str):
        df = self.loader.load_csv(csv_path)
        df = self.preprocessor.encode_categorical(df)

        X_train, X_test, y_train, y_test = self.preprocessor.split(
            df, target_col,
            test_size=self.config.test_size,
            random_state=self.config.random_state
        )

        self.defect_model.train(X_train, y_train)
        results = self.benchmark.evaluate_classification(
            self.defect_model, X_test, y_test
        )

        explanation_raw = self.explainer.explain_tabular_model(
            self.defect_model.model,
            X_test.head(3)
        )
        explanation_text = [
            self.explainer.tester_friendly_explanation(item)
            for item in explanation_raw
        ]

        return {
            "task": "defect_prediction",
            "metrics": results,
            "explanations": explanation_text
        }

    def run_test_prioritization(self, test_cases_df):
        prioritized = self.prioritizer.prioritize(test_cases_df)
        return {
            "task": "test_prioritization",
            "prioritized_tests": prioritized.to_dict(orient="records")
        }

    def run_self_healing(self, broken_locator: str, dom_candidates: list[str]):
        healed = self.self_healer.heal_locator(broken_locator, dom_candidates)
        return {
            "task": "self_healing",
            "result": healed
        }

    def run_test_generation(self, requirements: list[str]):
        tests = self.test_generator.generate_from_requirements(requirements)
        return {
            "task": "test_generation",
            "generated_tests": tests
        }

    def run_ci_cd_export(self, results: dict, output_path="ci_results.json"):
        self.cicd.export_results(results, output_path)
        return {
            "task": "ci_cd_export",
            "output_path": output_path
        }
