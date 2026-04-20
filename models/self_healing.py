import re


class SelfHealingEngine:
    def heal_locator(self, broken_locator: str, dom_candidates: list[str]) -> dict:
        for candidate in dom_candidates:
            if self._is_similar(broken_locator, candidate):
                return {
                    "original": broken_locator,
                    "healed": candidate,
                    "confidence": 0.85,
                    "reason": "Matched by token similarity heuristic"
                }

        return {
            "original": broken_locator,
            "healed": None,
            "confidence": 0.0,
            "reason": "No suitable replacement found"
        }

    def _is_similar(self, broken: str, candidate: str) -> bool:
        broken_tokens = set(re.findall(r"\w+", broken.lower()))
        candidate_tokens = set(re.findall(r"\w+", candidate.lower()))
        overlap = len(broken_tokens & candidate_tokens)
        return overlap >= 1
