from fastapi import APIRouter

from app.schemas.calculator import CalculatorRequest
from app.services.agent_service import AgentService

router = APIRouter()

agent_service = AgentService()

@router.post("/agents/calculator")
async def calculator_agent(request: CalculatorRequest):
    return await agent_service.execute_agent(
        agent_name="calculator_agent",
        input_data={
            "task_type": "calculator",
            "operation": request.operation,
            "a": request.a,
            "b": request.b,
        },
    )