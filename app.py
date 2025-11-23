from fastapi import FastAPI
import joblib
import pandas as pd
from typing import Dict, List
from pydantic import BaseModel

app = FastAPI(title="Azure Demand Forecasting API")

# Load model + columns
MODEL_PATH = "artifacts/best_model_fixed.joblib"
COLUMNS_PATH = "artifacts/model_columns.joblib"

model = joblib.load(MODEL_PATH)
model_cols = joblib.load(COLUMNS_PATH)

class PredictRequest(BaseModel):
    rows: List[Dict]

@app.get("/")
def root():
    return {"message": "API Online", "model": MODEL_PATH}

@app.post("/predict")
def predict(req: PredictRequest):
    df = pd.DataFrame(req.rows)
    
    # fill missing columns
    for col in model_cols:
        if col not in df.columns:
            df[col] = 0.0

    df = df[model_cols].astype(float)

    preds = model.predict(df)

    return {
        "predictions": preds.tolist(),
        "count": len(preds)
    }
