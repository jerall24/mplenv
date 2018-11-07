import numpy as np
import pandas as pd
from pandas import ExcelWriter

blah = np.array([[1,2],[3,4]])
blah_df = pd.DataFrame(data=blah)
writer = pd.ExcelWriter('blah_df_test.xlsx')
blah_df.to_excel(writer,'Sheet 1',index=True)
writer.close()
