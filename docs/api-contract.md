# Safety Prediction API – Contract

## Base URL
https://safety-prediction-api.azurewebsites.net

## Endpoint
POST /predict

## Request Body
{
  "crime_score": float (0–1),
  "crowd_score": float (0–1),
  "time_score": float (0–1),
  "location_score": float (0–1)
}

## Response
{
  "risk_score": float (0–1),
  "safety_score": int (0–100),
  "risk_level": "LOW | MEDIUM | HIGH"
}

## Usage
- Predict area safety
- Trigger alerts
- Assist safer route generation

