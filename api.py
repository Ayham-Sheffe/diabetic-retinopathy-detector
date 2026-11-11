from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from diabetes_service import DiabetesService

app = FastAPI(title="Diabetes Prediction API")

service = DiabetesService()


class PatientData(BaseModel):
    HighBP: int
    HighChol: int
    CholCheck: int
    BMI: int
    Smoker: int
    Stroke: int
    HeartDiseaseorAttack: int
    PhysActivity: int
    Fruits: int
    Veggies: int
    HvyAlcoholConsump: int
    AnyHealthcare: int
    NoDocbcCost: int
    GenHlth: int
    MentHlth: int
    PhysHlth: int
    DiffWalk: int
    Sex: int
    Age: int


@app.post("/predict")
def predict(data: PatientData):
    try:
        result = service.predict(data.model_dump())
        return result

    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))