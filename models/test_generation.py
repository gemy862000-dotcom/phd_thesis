class TestCaseGenerationEngine:
    def generate_from_requirements(self, requirements: list[str]) -> list[dict]:
        test_cases = []
        for i, req in enumerate(requirements, start=1):
            test_cases.append({
                "test_id": f"TC_{i:03}",
                "title": f"Validate requirement {i}",
                "steps": [
                    "Open application",
                    f"Execute scenario for: {req}",
                    "Verify expected result"
                ],
                "expected_result": f"System satisfies: {req}"
            })
        return test_cases
