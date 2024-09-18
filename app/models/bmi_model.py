from pydantic import BaseModel

class BMICalculatorInput(BaseModel):
    weight: float
    height: float
