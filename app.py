import pandas as pd

from config import FrameworkConfig
from core.pipeline import IntegratedAITestAutomationFramework


def main():
    config = FrameworkConfig()
    framework = IntegratedAITestAutomationFramework(config)

    try:
        defect_results = framework.run_defect_prediction(
            csv_path="sample_defect_data.csv",
            target_col="buggy"
        )
        print("\n=== Defect Prediction Results ===")
        print(defect_results)
    except FileNotFoundError:
        print("sample_defect_data.csv not found. Add your dataset to run defect prediction.")

    test_cases_df = pd.DataFrame([
        {"test_id": "T1", "historical_failures": 5, "execution_time": 10, "changed_files": 3},
        {"test_id": "T2", "historical_failures": 1, "execution_time": 2, "changed_files": 1},
        {"test_id": "T3", "historical_failures": 4, "execution_time": 5, "changed_files": 4},
    ])

    prioritization_results = framework.run_test_prioritization(test_cases_df)
    print("\n=== Test Prioritization Results ===")
    print(prioritization_results)

    self_healing_results = framework.run_self_healing(
        broken_locator="//button[@id='login-btn']",
        dom_candidates=[
            "//button[@id='submit-login']",
            "//input[@name='username']",
            "//button[@class='login-btn']"
        ]
    )
    print("\n=== Self-Healing Results ===")
    print(self_healing_results)

    generated_tests = framework.run_test_generation([
        "User should be able to log in with valid credentials",
        "User should receive an error for invalid password",
        "System should lock account after five failed attempts"
    ])
    print("\n=== Test Generation Results ===")
    print(generated_tests)

    all_results = {
        "prioritization": prioritization_results,
        "self_healing": self_healing_results,
        "test_generation": generated_tests
    }
    export_result = framework.run_ci_cd_export(all_results)
    print("\n=== CI/CD Export ===")
    print(export_result)


if __name__ == "__main__":
    main()
