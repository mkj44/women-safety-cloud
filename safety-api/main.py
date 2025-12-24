from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SafetyInput(BaseModel):
    crime_score: float
    crowd_score: float
    time_score: float
    location_score: float

@app.get("/")
def root():
    return {"status": "Safety Prediction API running"}

@app.post("/predict")
def predict(data: SafetyInput):
    risk = (
        0.4 * data.crime_score +
        0.3 * data.crowd_score +
        0.2 * data.time_score +
        0.1 * data.location_score
    )

    safety_score = int(100 * (1 - risk))

    if safety_score < 40:
        level = "HIGH"
    elif safety_score < 70:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_score": round(risk, 2),
        "safety_score": safety_score,
        "risk_level": level
    }
