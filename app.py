from fastapi import FastAPI, UploadFile, Request
import uvicorn
import logging
from model import Model
import pandas as pd
import argparse
from logging_file import setup_logging

app = FastAPI()

setup_logging()
logger = logging.getLogger(__name__)

model = Model(model_pipeline_path="model_pipeline.pkl")


@app.get("/health")
def health():
    return {"status":"OK!"}

@app.post("/predict")
def predict(file: UploadFile):

    logger.info(f"Получен файл: {file.filename}")

    data = pd.read_csv(file.file)

    logger.info(f"Размер входных данных: {data.shape}")

    y_pred = model.pred_target(data)
    

    result = pd.concat([data["id"], pd.Series(y_pred)], axis=1)
    result.columns = ["id", "prediction"]


    return result.to_dict(orient="records")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8999)
    parser.add_argument("--host", type=str, default="0.0.0.0")
    args = vars(parser.parse_args())

    uvicorn.run(app, **args)




