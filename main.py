from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("pedestrian_model_final (4).pkl")


class InputData(BaseModel):

    f1: float = Field(..., ge=0)
    f2: float = Field(..., ge=0)
    f3: float = Field(..., ge=0)
    f4: float = Field(..., ge=0)
    f5: float = Field(..., ge=0)
    f6: float = Field(..., ge=0)
    f7: float = Field(..., ge=0)
    f8: float = Field(..., ge=0)
    f9: float = Field(..., ge=0)
    f10: float = Field(..., ge=0)


@app.get("/")
def home():
    return {"message": "API is working"}


@app.post("/predict")
def predict(data: InputData):

    features = [
        data.f1, data.f2, data.f3, data.f4, data.f5,
        data.f6, data.f7, data.f8, data.f9, data.f10
    ]

    prediction = model.predict([features])

    return {
        "input": features,
        "prediction": float(prediction[0])
    }