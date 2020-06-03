import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

            # importing covid19 dataset   

corona_dataset_csv = pd.read_csv('Datasets/covid19_Confirmed_dataset.csv')
corona_dataset_csv.head(10)

            #Let's check the shape of the dataframe

corona_dataset_csv.shape
           # Delete the useless columns
corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)
corona_dataset_csv.head(10)
           #  Aggregating the rows by the country
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.head(10)
corona_dataset_aggregated.shape
           # Visualizing data related to a country
corona_dataset_aggregated.loc['India'].plot()
corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['Italy'].plot()
corona_dataset_aggregated.loc['Spain'].plot()
plt.legend()
		   #Calculating a good measures
corona_dataset_aggregated.loc['India'].plot()		  
           # caculating the first derivative of the curve
corona_dataset_aggregated.loc['India'].diff().plot()
           # find maxmimum infection rate for India,Italy,China,et
corona_dataset_aggregated.loc['India'].diff().max()
corona_dataset_aggregated.loc['China'].diff().max()
corona_dataset_aggregated.loc['Italy'].diff().max()
corona_dataset_aggregated.loc['Spain'].diff().max()
            # find maximum infection rate for all of the countries.
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries :
	max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max infection rate'] = max_infection_rates
corona_dataset_aggregated.head()
		   # create a new dataframe with only needed column
corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])
corona_data.head()
		   #Importing the WorldHappinessReport.csv dataset
            # selecting needed columns for our analysis
             # join the datasets
              #calculate the correlations as the result of our analysis
      #importing the dataset
world_happiness_report = pd.read_csv("Datasets/worldwide_happiness_report.csv")
world_happiness_report.head()
world_happiness_report.shape
  
          # let's drop the useless columns
columns_to_dropped = ['Overall rank','Score','Generosity','Perceptions of corruption']
world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)
world_happiness_report.head()
          # changing the indices of the dataframe
world_happiness_report.set_index(['Country or region'],inplace=True)
world_happiness_report.head()
          # let's join two dataset we have prepared
corona_data.head()

world_happiness_report.head()		  
data = world_happiness_report.join(corona_data).copy()
data.head()
         # correlation matrix
data.corr()
         # Visualization of the results
data.head()
         # Plotting GDP vs maximum Infection rate
x = data['GDP per capita']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))


sns.regplot(x,np.log(y))
        
		 # Plotting Social support vs maximum Infection rate
x = data['Social support']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))


sns.regplot(x,np.log(y))

         # Plotting Healthy life expectancy vs maximum Infection rate
x = data['Healthy life expectancy']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))
	
          # Plotting Freedom to make life choices vs maximum Infection
x = data['Freedom to make life choices']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))	

sns.regplot(x,np.log(y))
	  



# devloped countries had a faster rate of covid19 cases





























		   
		   
		   