# Ames Housing Data

---
### Problem statement

As part of a property listing and pricing platform that connects home buyers and sellers, we were tasked to predict sale prices of the properties, as well as determine the features that makes a property valuable and therefore sell at a higher price. 


---
### Executive Summary

When it comes to owning a home, homeowners want know the value of their house and potential homeowners want to know what to expect. This is apparent since they would want to get the best price out of the sale. For homeowners, they want to know what features to focus on when selling their house, and what features should be highlighted in order to make it outstanding from other properties. On the other hand, buyers would want to get a house at a best value, and not end up paying too much for it.

Hence, we want to create a model that is able to predict prices of properties based on features of the property from past data.


#### Methodology

In this analysis, we will be using the Ames Housing Data Set which contains information from the Ames Assessor’s Office used in computing the value of individual residential properties sold in Ames, Iowa from 2006 to 2010. The Ames Housing dataset was compiled by Dean De Cock for use in data science education.

The data set contains 2930 observations and 82 variables consisting of 23 nominal, 23 ordinal, 14 discrete and 20 continuous variables which can be found here: [data dictionary.](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)


Of these variables, property size evidently affects sale price; other factors commonly associated with sale price included access to amenities, location, number of rooms, age and condition of the property.

Exploratory data anlysis will be carried out: explore the data, read the data dictionary, know the variables, generate an idea of what relationships exists, identify unusual data points.

We then clean the data: data collected are unlikely to be perfect, there may be missing values, values input incorrectly, values out of the ordinary, and we clean it in a way to make our data science process easier. In the cleaning process, we will determine how to handle any unusual, missing or outlier data. We can also manipulate our data to create any interaction terms based on the potential relationship with the target (SalePrice) variable.

Through plotting of charts such as histograms, barcharts, boxplots, and scatterplots etc., we are able to better visualise the relationships between the variables, and determine which relationships to target. We can include these features into our modelling process.

By regularising regression models, we can start on the process to select features for our model.
"Feature selection" will be automatically performed using the Lasso model since it forces the coefficients to be zero.

Afterwhich, we determine the best model to select by comparing the Coefficient of Determination,  "𝑅2 score". The closer it gets to 1, the better the model explains the variablity of the response data around its mean.

We then select the best model to perform regression, and predict our target variable.

In carrying out the data science process(from obtaining data to modelling), we observe a few features that best explains the variability of prices in the model.

Not surprising, the size (bigger) and quality (better) of the property ranks top, followed by other features such as:
location of neighborhood: Stone Brook, Northridge Heights, and Northridge, 
proximity to amenities: near or adjacent positive off-site features, and 
style and materials used in house exterior: Wooden, Hip roof style, and Imitation Stucco and Cement Board Exterior.


#### Notebooks:
- [01 EDA and Preprocessing](./code/01_EDA_and_Preprocessing.ipynb)
- [02 Modelling](./code/02_Modelling.ipynb  )
- [03 Recommendations](./code/03_Recommendations.ipynb)




---
### Conclusion & Recommendation
Based on past trends in sale prices, we were able to determine certain factors that contributes to a higher sale price of property. This means that homeowners can leverage on the model to predict the price of their property, and be able to determine a good selling price if they are selling their property but do not know where to start.
On the other hand, new and potential homeowners are able to determine if a property is worth its value, and get some knowledge of property prices with or without certain features.

Based on our analysis we have a few recommendations for homeowners and potential homeowners:
1. Area and Quality are key features that add value to houses
In our lasso model, we have determined features that positively affects the sale price in the modelling. Living Area was the strongest feature, followed by other features (Overall, Exterior and Kitchen Quality) determining the quality of the home.

2. Improve Exterior of house and choose the right materials
Homeowners can improve the exterior of their house (roof style, material, Exterior material). Ames, Iowa has a four-season climate and temperature varies a lot during climate changes. Choosing a material strong enough to withstand the climate changes is typically more desirable.

3. Invest in the right neighborhood
Generally, Stone Brook, Northridge Heights, and Northridge have a higher mean selling price.

4. Brag about your accessibility to certain amenities
Data has shown that properties near or adjacent positive off-site features such as park, or other amenities generally has a higher average selling price.

Generally, the trend in property prices are in line with features they are exclusive to. But this does not mean that the model is applicable to other cities where it is an entirely different population, land resources, and priorities of homeowners are different. We are also reminded that higher demand with a limited supply means higher prices. There are other factors that may affect these demands/supply which will likely influence the prediction of prices if we were to use the same features in the prediction model.
