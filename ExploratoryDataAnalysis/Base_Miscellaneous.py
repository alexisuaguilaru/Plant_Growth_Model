from matplotlib.colors import LinearSegmentedColormap
from re import sub

Color_Palette = ['lightgreen','darkgreen']
Color_Map = LinearSegmentedColormap.from_list("Color_Map",Color_Palette,N=20)

def GetFeatureName(Feature:str) -> str:
    """
        Function for getting feature's name 
        of a feature

        -- Feature : str :: Feature from which its name is obtained

        Return feature's name
    """
    return sub(r'_',' ',Feature)