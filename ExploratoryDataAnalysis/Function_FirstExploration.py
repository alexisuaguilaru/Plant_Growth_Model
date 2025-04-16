import pandas as pd
import numpy as np

def SplittingFeaturesBasedDataType(Dataset:pd.DataFrame,Features:list[str]) -> tuple[list[str]]:
    """
        Function to split features of a dataset based 
        on their data types

        -- Dataset : pd.DataFrame :: Dataset where feature splitting is applied

        -- Features : list[str] :: Feature to be splitted

        Return a list of categorical, discrete numerical 
        and continuous numerical features
    """
    categorical_features , numerical_features = [] , []

    for feature in Features:
        if Dataset[feature].dtype == 'object':
            categorical_features.append(feature)
        else:
            numerical_features.append(feature)

    return categorical_features , numerical_features

def Standardization(Values:np.ndarray) -> np.ndarray:
    """
        Function to standardize an 
        array of values

        -- Values : np.ndarray :: Values to be standardized

        Return an array of 
        standardized values
    """
    return (Values - np.mean(Values))/np.std(Values,ddof=1)

def CategoricalDescription(Dataset:pd.DataFrame,CategoricalFeature:str) -> pd.Series:
    """
        Function to generate a minimal 
        description of a categorical 
        feature in a dataset

        -- Dataset : pd.DataFrame :: Dataset from which attribute values are taken

        -- CategoricalFeature : str :: Feature from which description is generated

    """    
    return Dataset[CategoricalFeature].value_counts()