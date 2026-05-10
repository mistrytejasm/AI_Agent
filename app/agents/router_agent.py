from multiprocessing.sharedctypes import Value

from app.agents.calculator_agent import CalculatorAgent
from app.schemas.agent import AgentState

class RouterAgent:
    def __init__(self):
        self.calculator_agent = CalculatorAgent()

    async def route(self, state: AgentState):
        task_type = state.input_data.get("task_type")

        if task_type == "calculator":
            return await self.calculator_agent.execute(state)

        raise ValueError("No Suitable agent Found")
