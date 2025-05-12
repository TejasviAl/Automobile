import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# univariant
sns.set(color_codes = True)
auto = pd.read_csv('Automobile (1).csv')
print(auto.head())
sns.distplot(auto['normalized_losses'])
plt.show()
sns.distplot(auto['normalized_losses'], kde=False, rug=True)
plt.show()
# bi-variant 
sns.jointplot(x='engine_size', y='horsepower', data= auto)
plt.show()
#  hexplot - concentration of hexagons
sns.jointplot(x='engine_size', y='horsepower', data = auto, kind= 'hex')
plt.show()
# multi-variate analysis
sns.pairplot(auto[['normalized_losses', 'engine_size', 'horsepower']])
plt.show()
# categorical and continuous variable- we are using stripplot for this 
sns.stripplot(x= "fuel_type", y = "horsepower", data = auto)
plt.show() 
# ordered scatter plot
# swarmplot, we havbe no overlapping
sns.swarmplot(x='fuel_type', y='horsepower', data= auto)
plt.show()
# boxplot
sns.boxplot(x='number_of_doors', y='horsepower', data= auto)
plt.show()
sns.boxplot(x='body_style', y='horsepower', hue='engine_location', data=auto)
plt.show()
sns.countplot(x='body_style', data=auto, hue='engine_location')
plt.show()
# linear regression plot
sns.lmplot(x='horsepower', y='peak_rpm', data=auto)
plt.show()


# using pandas 
import pandas as pd
auto = pd.read_csv('Automobile (1).csv')
print(auto.head())
print(auto.info())
print(auto['price'].mean())
print(auto['price'].max())
print(auto[auto['price'] == auto['price'].max()])
print(auto[auto['price']==auto['price'].min()])
print(auto[auto['horsepower']>100].count())
print(auto[auto['body_style']=='hatchback'].info())
# print(auto['make'].unique())
print(auto['make'].value_counts().head(3))
print(auto[auto['price']==7099]['make'])
print(auto[auto['price']>40000])
print(auto[(auto['body_style']=='sedan') & (auto['price']<7000)])