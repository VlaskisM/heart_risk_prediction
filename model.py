import pandas as pd
import joblib
from preprocessor import Preprocessor
import logging


logger = logging.getLogger(__name__)

class Model:
    

    def __init__(self, model_pipeline_path:str):
        self.model = joblib.load(model_pipeline_path)
        self.preprocessor = Preprocessor()


    def pred_target(self, data: pd.DataFrame):

        data_transform = self.preprocessor.transform(data)

        logger.info(f"Данные преобразованы: {data_transform.shape}")
        logger.info(f"Столбцы: {data_transform.columns}" )

        y_pred = self.model.predict(data_transform)

        logger.info("Предсказания получены")

        return y_pred
