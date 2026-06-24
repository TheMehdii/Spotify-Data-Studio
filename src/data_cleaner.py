from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer as SKLKNN

# manage missing data

class BaseImputer(ABC):
    @abstractmethod
    def impute(self, df: pd.DataFrame, columns : list) -> pd.DataFrame :  #using type hinting
        pass

class MeanImputer(BaseImputer) : #found missing data by using avarega method by subset from BaseImputer
    def impute(self, df : pd.DataFrame, columns : list) -> pd.DataFrame:
        df_copy = df.copy() # using a copy from dataframe not main dataframe
        for col in columns:
            if col in df_copy.columns:
                ava_value = df_copy[col].mean()
                df_copy[col] = df_copy[col].fillna(ava_value) # use ava_value for missing data
        return df_copy

class MedianImputer(BaseImputer) : #found missing data by using median
    def impute(self, df: pd.DataFrame, columns:list) -> pd.DataFrame:
        df_copy = df.copy()
        for col in columns:
            if col in df_copy.columns:
                med_value = df_copy[col].median()
                df_copy[col] = df_copy[col].fillna(med_value)
        return df_copy

class KNNImputer(BaseImputer): #found missing data by using KNN
    def __init__(self, n_neighbors : int = 5 ):
        self.n_neighbors = n_neighbors
    
    def impute(self, df: pd.DataFrame, columns:list) -> pd.DataFrame :
        df_copy = df.copy()
        
        valid_cols = [c for c in columns if c in df_copy and pd.api.types.is_numeric_dtype(df_copy[c])] #checkin valid col and type is number

        if valid_cols:
            imputer = SKLKNN(n_neighbors= self.n_neighbors)
            df_copy[valid_cols] = imputer.fit_transform(df_copy[valid_cols]) #fit data by same type and around five data 

        
        return df_copy


# manage outlier data 

class BaseOutlierHandler(ABC) : 
    @abstractmethod
    
    def handle(self, df:pd.DataFrame, columns: list) -> pd.DataFrame:
        pass


class IQROutllierHandler(BaseOutlierHandler):   #https://en.wikipedia.org/wiki/Interquartile_range

    def handle(self, df : pd.DataFrame, columns : list) -> pd.DataFrame :
        df_copy = df.copy()
        for col in columns:
            if col in df_copy.columns and pd.api.types.is_numeric_dtype(df_copy[col]):
                Q1 = df_copy[col].quantile(0.25) # first quarter : A number that is 25% of the numbers before it.
                Q3 = df_copy[col].quantile(0.75) # second quarter : A number that is 75% of the numbers before it.

                IQR = Q3 - Q1 #Interquartile range

                lower_b = Q1 - 1.5 * IQR
                upper_b = Q3 + 1.5 * IQR

                df_copy[col] = np.where(df_copy[col] < lower_b, lower_b, df_copy[col]) # Checking data with a lower bound
                df_copy[col] = np.where(df_copy[col] > upper_b, upper_b, df_copy[col]) # Checking data with a upper bound

        return df_copy

class ZScoreOutlierHandler(BaseOutlierHandler): # https://en.wikipedia.org/wiki/Standard_score 

    def __init__(self, bound: float = 3.0):
        self.bound = bound

    def handle(self, df: pd.DataFrame, columns: list) -> pd.DataFrame :
        df_copy = df.copy()

        for col in columns:
            if col in df_copy.columns and pd.api.types.is_numeric_dtype(df_copy[col]):

                ava = df_copy[col].mean()
                enh = df_copy[col].std()

                if enh == 0:
                    continue

                z_score = (df_copy[col] - ava) / enh 

                df_copy[col] = np.where(abs(z_score) > self.bound, ava, df_copy[col])
        
        return df_copy