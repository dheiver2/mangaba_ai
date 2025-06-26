from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class AnalysisResult:
    """
    Representa o resultado de uma análise de conversa.
    """

    summary: str
    message_count: int
    participants: int
    processed_messages: List[Dict[str, Any]]
