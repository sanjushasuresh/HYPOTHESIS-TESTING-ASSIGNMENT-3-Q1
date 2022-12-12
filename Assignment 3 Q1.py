# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:54:31 2022

@author: LENOVO
"""

import scipy as stats
import pandas as pd
df = pd.read_csv("Cutlets.csv")
df.head
df.size
df['Unit A'].mean()
df['Unit B'].mean()
df['Unit A'].std()
df['Unit B'].std()
X = df.iloc[:,0]
X
Y = df.iloc[:,1]
Y
from scipy import stats
zcal, p_val = stats.ttest_ind(df['Unit A'], df['Unit B'])
print("Z Calculated value is ", zcal.round(4))
print("P-value is ", p_val.round(4))
# H0 = There is no significant difference in the diameter of the cutlet b/w 2 units
# H1 = There is a significant difference in the diameter of the cutlet b/w 2 units
if p_val<0.05:
    print("H0 is rejected, H1 is accepted")
else:
    print("H1 is rejected, H0 is accepted")
# Since H1 is rejected and H0 is accepted, we can conclude that there is
# no significant difference in the diameter of the cutlet b/w 2 units