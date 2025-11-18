import pandas as pd
import logging


logger = logging.getLogger(__name__)

class Preprocessor:

    def transform(self, data: pd.DataFrame):

        #df = data.copy()
        
        df = data.fillna(0)

        
        #df["Gender"] = df["Gender"].str.replace("Male","1.0").str.replace("Female","0.0")
        #df = df.query('Gender != "1.0" and Gender != "0.0"')

        df[[
            "Medication Use",
            "Previous Heart Problems",
            "Diet",
            "Alcohol Consumption",
            "Obesity",
            "Smoking",
            "Family History",
            "Diabetes"
            ]] = df[[
                    "Medication Use",
                    "Previous Heart Problems",
                    "Diet",
                    "Alcohol Consumption",
                    "Obesity",
                    "Smoking",
                    "Family History",
                    "Diabetes"]].astype("str")

        df = df.drop(columns=["CK-MB","Troponin"])
        df = df.drop(columns=["Unnamed: 0","id"])

        logger.info("Трансформация сделана")

        return df


        

