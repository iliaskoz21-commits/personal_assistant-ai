import operator
from typing import Annotated, List, TypedDict

class AgentState(TypedDict):
    """
    The state of the agentic graph.
    'messages' uses operator.add to append new messages to the history.
    """
    messages: Annotated[List[dict], operator.add]
    city: str