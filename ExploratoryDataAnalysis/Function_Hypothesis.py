import pandas as pd
import numpy as np
from scipy.stats import ks_2samp , chi2_contingency

def SameDistribution(Sample_1:pd.Series|np.ndarray,Sample_2:pd.Series|np.ndarray,Significance:float=0.05) -> str:
    """
        Function to prove it two samples 
        are drawn from the same distribution

        -- Sample_1 : pd.Series|np.ndarray :: Sample 1 for the test

        -- Sample_2 : pd.Series|np.ndarray :: Sample 2 for the test

        -- Significance : float :: Significance level for the test

        Return the result of the test
    """
    results_test = ks_2samp(Sample_1,Sample_2)
    if (p_value := results_test.pvalue) >= Significance:
        result = f'Both samples come from the same distribution with a p-value {p_value}'
    else:
        result = f'Both samples come from different distributions with a p-value {p_value}'
    return result

def AreIndependents(ContingencyTable:pd.DataFrame|np.ndarray,Significance:float=0.05) -> str:
    """
        Function to prove if two variables 
        are independents 

        -- ContingencyTable : pd.DataFrame|np.ndarray :: Contingency table of the two features

        -- Significance : float :: Significance level for the test

        Return the result of the test
    """
    result_test = chi2_contingency(ContingencyTable)
    if (p_value := result_test.pvalue) >= Significance:
        result = f'The two variables are independent with a p-value {p_value}'
    else:
        result = f'The two variables are dependent with a p-value {p_value}'
    return result

def StratifiedFeature(Dataset:pd.DataFrame,Feature:str,StratifyFeature:str,StrataValues:list) -> list[pd.DataFrame]:
    """
        Function to stratify a feature 
        based on another feature values

        -- Dataset : pd.DataFrame :: Dataset from which the values to be stratified are obtained

        -- Feature : str :: The feature that is stratified

        -- StratifyFeature : str :: The feature that is used for stratification

        -- StrataValues : list :: The values representing each stratum

        Return a list of stratified values
    """
    return [Dataset.query(f"`{StratifyFeature}` == @strata_value")[Feature] for strata_value in StrataValues]

def ContingencyTable(Dataset:pd.DataFrame,ValuesCount:str,FeatureIndex:str,FeatureColumns:str) -> pd.DataFrame:
    """
        Function to generate a contingency 
        table from a dataset using certain 
        features 

        -- Dataset : pd.DataFrame :: Dataset from which the contigency table is generated

        -- ValuesCount : str :: Values used to count instances

        -- FeatureIndex : str :: Attribute appearing in rows

        -- FeatureColumns : str :: Attribute appearing in the columns
        
        Return the generated contingency table 
    """
    return Dataset.pivot_table(values=ValuesCount,index=FeatureIndex,columns=FeatureColumns,aggfunc='count')