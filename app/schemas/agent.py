from typing import Dict, Any, Optional
from pydantic import BaseModel

class AgentState(BaseModel):
    agent_name: str
    input_data: Dict[str, Any]
    current_step: str = "initialized"
    status: str = "pending"
    metadata: Dict[str, Any] = {}

class AgentResponse(BaseModel):
    success: bool
    agent_name: str
    result: Any
    message: str
    execution_time: Optional[float] = None
    
