from abc import ABC
from abc import abstractmethod

from app.schemas.agent import AgentResponse
from app.schemas.agent import AgentState

class BaseAgent(ABC):
    name: str="base_agent"

    @abstractmethod
    async def execute(self, state: AgentState) -> AgentResponse:
        pass