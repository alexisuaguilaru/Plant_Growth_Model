import pandas as pd
import matplotlib.pyplot as plt

from Base_Miscellaneous import GetFeatureName , Color_Palette

from typing import Callable

def PlotDistributionsByTarget(Dataset:pd.DataFrame,Features:list[str],Target:str,TypePlot:Callable,FeatureTypeName:str,AdditionalPlotArgs:dict={}) -> None:
    """
        Function to plott distribution of features 
        by value of target

        -- Dataset : pd.DataFrame :: Dataset whose values are plotted

        -- Features : list[str] :: Attributes from which plots are generated

        -- Target : str :: Attribute that generates the hue in the plots

        -- TypePlot : Callable :: Type of plot generated

        -- FeatureTypeName : str :: Name given to the features

        -- AdditionalPlotArgs : dict :: Additional arguments to generate the plot

    """
    mosaic_grid = "1122\n.33."
    fig , axes = plt.subplot_mosaic(mosaic_grid,figsize=(8,6),layout='tight')

    for index_axes , feature in enumerate(Features,1):
        axes_plot = axes[str(index_axes)]
        TypePlot(Dataset,x=feature,hue=Target,palette=Color_Palette,ax=axes_plot,legend=False,**AdditionalPlotArgs)
        
        axes_plot.set_xlabel(GetFeatureName(feature),size=12)

    fig.suptitle(f'Distribution of\n{FeatureTypeName} Features',size=18)
    fig.legend(title='Growth Milestone',labels=['No Milestone','Milestone'],loc=(0.05,0.33))