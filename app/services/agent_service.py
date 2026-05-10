from app.agents.registry import AgentRegistry
from app.engine.executor import AgentExecutor
from app.schemas.agent import AgentState

class AgentService:
    def __init__(self):
        self.registry = AgentRegistry()
        self.executor = AgentExecutor()

    async def execute_agent(self, agent_name: str, input_data: dict):
        state = AgentState(
            agent_name=agent_name,
            input_data=input_data,
        )

        agent = self.registry.get_agent(agent_name)

        response = await self.executor.run(agent=agent, state=state)

        return response