[In]:
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,10,100)
y = np.cos(x)
plt.plot(x,y,marker="x")

[out]: 会输出一个坐标轴，并且是在x轴上以cos图像显示出来的




[In]:
import pandas as pd
from IPython.display import display
data = {'Name':["John","Anna","Peter","Linda"],
         'Age':[24,13,53,33],
       'Location':["New York","Paris","Berlin","London"],
      }
data_pandas = pd.DataFrame(data)
display(data_pandas)

[Out]:  输出结果为一个表格




