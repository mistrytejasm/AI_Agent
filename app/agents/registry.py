from app.agents.calculator_agent import CalculatorAgent

class AgentRegistry:
    def __init__(self):
        self.agents = {
            "calculator_agent": CalculatorAgent(),
        }

    def get_agent(self, agent_name: str):
        agent = self.agents.get(agent_name)

        if not agent:
            raise ValueError(f"Agent '{agent_name}' Not Found")

        return agent

        