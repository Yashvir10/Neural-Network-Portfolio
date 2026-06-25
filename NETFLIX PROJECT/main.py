from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import pickle
import pandas as pd

with open("model.pkl", "rb") as f:
    model = pickle.load(f)



app = FastAPI(
    title="Netflix Churn Prediction API",
    description="Advanced Netflix Customer Churn Prediction API",
    version="2.0.0"
)


# Pydantic Input Model
class CustomerData(BaseModel):
    gender: Annotated[
        Literal["Male", "Female"],
        Field(json_schema_extra={"example": "Male"})
    ]

    seniorCitizen: Annotated[
        int,
        Field(ge=0, le=1, json_schema_extra={"example": 0})
    ]

    partner: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "Yes"})
    ]

    dependents: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "No"})
    ]

    tenure: Annotated[
        int,
        Field(ge=0, json_schema_extra={"example": 12})
    ]

    phoneService: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "Yes"})
    ]

    multipleLines: Annotated[
        Literal["Yes", "No", "No phone service"],
        Field(json_schema_extra={"example": "No"})
    ]

    internetService: Annotated[
        Literal["DSL", "Fiber optic", "No"],
        Field(json_schema_extra={"example": "Fiber optic"})
    ]

    onlineSecurity: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "No"})
    ]

    onlineBackup: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "Yes"})
    ]

    deviceProtection: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "No"})
    ]

    techSupport: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "No"})
    ]

    streamingTV: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "Yes"})
    ]

    streamingMovies: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "Yes"})
    ]

    contract: Annotated[
        Literal["Month-to-month", "One year", "Two year"],
        Field(json_schema_extra={"example": "Month-to-month"})
    ]

    paperlessBilling: Annotated[
        Literal["Yes", "No"],
        Field(json_schema_extra={"example": "Yes"})
    ]

    paymentMethod: Annotated[
        Literal[
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ],
        Field(json_schema_extra={"example": "Electronic check"})
    ]

    monthlyCharges: Annotated[
        float,
        Field(gt=0, json_schema_extra={"example": 89.5})
    ]

    totalCharges: Annotated[
        float,
        Field(gt=0, json_schema_extra={"example": 1050.5})
    ]


@app.get("/")
def home():
    return {"message": "Netflix Churn Prediction API Running"}


@app.get("/customer/{customer_id}")
def get_customer(
    customer_id: Annotated[int, Path(gt=0, description="Customer ID")],
    detail: Annotated[bool, Query(description="Detailed customer info")] = False
):
    return {
        "customer_id": customer_id,
        "detail": detail
    }


@app.post("/predict")
def predict(data: CustomerData):
    try:
        df = pd.DataFrame([data.model_dump()])
        prediction = model.predict(df)[0]

        result = "Churn" if prediction == 1 else "No Churn"

        return {
            "prediction": int(prediction),
            "result": result
        }

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid input format"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )