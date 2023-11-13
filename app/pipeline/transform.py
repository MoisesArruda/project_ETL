import pandas as pd
from typing import List 


def contact_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
 
    """
    Função para transformar uma lista de DF em um único DF
    """ 
    
    return pd.concat(data_frame_list, ignore_index=True)