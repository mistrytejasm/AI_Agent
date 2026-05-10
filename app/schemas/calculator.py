from pydantic import BaseModel

class CalculatorRequest(BaseModel):
    operation: str
    a: float
    b: float
