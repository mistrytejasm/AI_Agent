from app.core.logging import logger
from app.schemas.agent import AgentResponse, AgentState

class AgentExecutor:
    async def run(self, agent, state: AgentState) -> AgentResponse:
        
        logger.info(
            "agent_execution_started", 
            agent=agent.name,
            )

        response = await agent.execute(state)

        logger.info(
            "agent_execution_completed",
            agent=agent.name,
        )

        return response


