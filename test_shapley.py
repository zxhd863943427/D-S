import Shapley.Shapley as sh
import pandas as pd
df = pd.read_csv('1.csv',' ')
newSh = sh.Shapley(df,3)
print(newSh.getAllShapley())