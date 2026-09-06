from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="student-ml-api")

class PredictionInput(BaseModel):
    value: float

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": "1.1.0",
        "model_version": "model-1"
    }

@app.post("/predict")
def predict(data: PredictionInput):
    if data.value is None:
        raise HTTPException(status_code=400, detail="Missing input")
    
    prediction_val = data.value * 2
    return {
        "input": data.value,
        "prediction": prediction_val
    }
