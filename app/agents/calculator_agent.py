import time

from app.agents.base import BaseAgent
from app.schemas.agent import AgentState, AgentResponse

class CalculatorAgent(BaseAgent):
    name = "calculate_agent"

    async def execute(self, state: AgentState) -> AgentResponse:
        start_time = time.time()

        state.current_step = "processing"

        operation = state.input_data["operation"]
        a = state.input_data["a"]
        b = state.input_data["b"]

        result = None

        if operation == "add":
            result = a + b
        elif operation == "substract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                raise ValueError("Division by zero is not allowed")
            result = a / b
        else:
            raise ValueError("Unsupported Operation")

        state.status = "Completed"

        execution_time = round(time.time() - start_time, 4)

        return AgentResponse(
            success=True,
            agent_name=self.name,
            result=result,
            message="Calculation Complete Successfully",
            execution_time=execution_time,
        )


