import json
from utils.logger import get_logger

logger = get_logger(__name__)


class CICDIntegration:
    def export_results(self, results: dict, output_path: str = "ci_results.json"):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
        logger.info(f"CI/CD results exported to {output_path}")

    def should_fail_pipeline(self, benchmark_results: dict, min_f1: float = 0.70) -> bool:
        f1 = benchmark_results.get("f1", 0.0)
        logger.info(f"Evaluated F1 score: {f1}")
        return f1 < min_f1
