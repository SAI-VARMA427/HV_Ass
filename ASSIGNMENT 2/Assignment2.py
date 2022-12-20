import pandas as pd
values1 = pd.Series([10,20,30,40,50])
values2 = pd.Series([100,150,250,300,350])
print(values1)
print(values2)
values = values1 + values2
print(values)
values = values1 - values2
print(values)
values = values1 * values2
print(values)
values = values1 / values2
print(values)
values = values1 % values2
print(values)