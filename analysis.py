import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
print(df.columns)


df_selected = df[['Mortality rate, infant (per 1,000 live births)', 
                       'GDP per capita (constant 2010 US$)', 
                       'Country Name']]

plt.figure(figsize=(10, 6))
plt.scatter(df_selected['GDP per capita (constant 2010 US$)'], 
            df_selected['Mortality rate, infant (per 1,000 live births)'], 
            alpha=0.7)

plt.xlabel('GDP per capita (constant 2010 US$)')
plt.ylabel('Mortality rate, infant (per 1,000 live births)')
plt.title('Infant Mortality Rate vs. GDP per Capita (2015)')
plt.grid(True)


plt.show()

