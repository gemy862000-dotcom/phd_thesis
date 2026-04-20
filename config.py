from dataclasses import dataclass, field
from typing import List


@dataclass
class FrameworkConfig:
    random_state: int = 42
    test_size: float = 0.2
    benchmark_metrics: List[str] = field(default_factory=lambda: [
        "accuracy", "precision", "recall", "f1", "auc"
    ])
    supported_tasks: List[str] = field(default_factory=lambda: [
        "defect_prediction",
        "test_prioritization",
        "self_healing",
        "test_generation",
    ])
