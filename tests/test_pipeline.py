import pandas as pd
from app.pipeline.transform import contact_data_frames

df_1 = pd.DataFrame({'col1':[1,2],'col2': [3,4]})
df_2 = pd.DataFrame({'col1':[5,6],'col2': [7,8]})

def testar_a_concatenacao_da_lista_de_df():
    """
    Use o arrange act e asset para testar a função concact_data_frames
    """
    # arrange
    data_frame_list = [df_1,df_2]
    arrange = pd.concat(data_frame_list, ignore_index=True)

    # act
    df = contact_data_frames(data_frame_list)

    # assert
    assert df.shape == (4,2)
    assert data_frame.equals(df)