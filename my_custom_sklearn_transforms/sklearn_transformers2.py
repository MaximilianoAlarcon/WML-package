from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd


# Un transformador para remover columnas indeseadas
class Transform_data(BaseEstimator, TransformerMixin):
    def __init__(self, formato, dummies_transformar,PAYMENT_TERM_transformer,LOAN_AMOUNT_transformer,CHECKING_BALANCE_transformer,EXISTING_SAVINGS_transformer,AGE_transformer,EMPLOYMENT_DURATION_transformer):
        self.formato = formato
        self.dummies_transformar = dummies_transformar
        self.PAYMENT_TERM_transformer = PAYMENT_TERM_transformer
        self.LOAN_AMOUNT_transformer = LOAN_AMOUNT_transformer
        self.CHECKING_BALANCE_transformer = CHECKING_BALANCE_transformer
        self.EXISTING_SAVINGS_transformer = EXISTING_SAVINGS_transformer
        self.AGE_transformer = AGE_transformer
        self.EMPLOYMENT_DURATION_transformer = EMPLOYMENT_DURATION_transformer

    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        
        
        def powertransformer(dataframe,col,transformers):
            c = dataframe[col].copy()
            c = np.array(c).reshape(-1,1)
            c = transformers["1"].transform(c)
            c = transformers["2"].transform(c)
            c = transformers["3"].transform(c)
            c = np.float32(c)
            dataframe[col] = c
            
        def powertransformer_sqrt(dataframe,col,transformers):
            c = dataframe[col].copy()
            c = np.sqrt(c)
            c = np.array(c).reshape(-1,1)
            c = transformers["1"].transform(c)
            c = transformers["2"].transform(c)
            c = transformers["3"].transform(c)
            c = np.float32(c)
            dataframe[col] = c
            
        def powertransformer_log(dataframe,col,transformers):
            c = dataframe[col].copy()
            c = np.log(c)
            c = np.float32(c)
            c = np.array(c).reshape(-1,1)
            c = transformers["1"].transform(c)
            c = transformers["2"].transform(c)
            c = transformers["3"].transform(c)
            c = np.float32(c)
            dataframe[col] = c        
        
        
        data = X.copy()
        
        data = data[self.formato].copy()
        
        powertransformer_log(data,"PAYMENT_TERM",self.PAYMENT_TERM_transformer)
        powertransformer_log(data,"LOAN_AMOUNT",self.LOAN_AMOUNT_transformer)
        powertransformer(data,"CHECKING_BALANCE",self.CHECKING_BALANCE_transformer)
        powertransformer_sqrt(data,"EXISTING_SAVINGS",self.EXISTING_SAVINGS_transformer)
        powertransformer_sqrt(data,"AGE",self.AGE_transformer)
        powertransformer(data,"EMPLOYMENT_DURATION",self.EMPLOYMENT_DURATION_transformer)
        
        data = self.dummies_transformar.transform(data)
        
        if "ALLOW" in data.columns:
            data.drop(labels=["ALLOW"], axis='columns',inplace=True)
            
        formato = ['PAYMENT_TERM', 'INSTALLMENT_PERCENT', 'LOAN_AMOUNT',
       'CHECKING_BALANCE', 'EXISTING_SAVINGS', 'EXISTING_CREDITS_COUNT', 'AGE',
       'TELEPHONE', 'EMPLOYMENT_DURATION', 'CURRENT_RESIDENCE_DURATION',
       'SEX_F', 'SEX_M', 'PROPERTY_CAR_OTHER', 'PROPERTY_REAL_ESTATE',
       'PROPERTY_SAVINGS_INSURANCE', 'PROPERTY_UNKNOWN', 'HOUSING_FREE',
       'HOUSING_OWN', 'HOUSING_RENT']
        data = data[formato].copy()
        
        # Retornamos um nuevo dataframe sin las colunmas indeseadas
        return data