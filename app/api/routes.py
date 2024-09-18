from fastapi import APIRouter, HTTPException
from app.models.bmi_model import BMICalculatorInput


router = APIRouter()


@router.post("/calculate-bmi")
def calculate_bmi(data: BMICalculatorInput):

    weight = data.weight
    height = data.height / 100  ## Centimeters to meters conversion

    if height <= 0 or weight <= 0:
        raise HTTPException(status_code=400, detail="Invalid height or weight!!")
    
    bmi = weight / (height * height)
    message = ''

    if bmi < 18.5:
        message = 'Underweight'
    elif 18.5 <= bmi < 24.9:
        message = 'Normal weight'
    elif 25 <= bmi < 29.9:
        message = 'Overweight'
    else:
        message = 'Obese'
    
    return {"bmi": bmi, "message": message}
