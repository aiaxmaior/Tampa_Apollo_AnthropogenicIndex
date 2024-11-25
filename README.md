
## Overview: Case Study: Apollo Beach Commercial Pier
## Formation of an anthropogenic weighted aggregate index and evaluation in local coastal environments based on data from 1990 – present.
This project utilizes standard Data Science practices and machine learning to inform decisions about mitigating human-induced ecosystem degradation through the implementation of a novel weight aggregate index of negative human influence on coastal marine ecosystems.

## 1) Project Description
This project is associated with an ongoing effort to build a commercial dock in Apollo Beach, Florida, a coastal community located in 'Middle Tampa Bay'. Coastal construction of any kind significantly impacts the health of local ecosystems, introducing harmful chemicals, causing physical damage, and a range of other factors that disrupt the local ecosystem.
The construction of a new dock will inevitably damage local habitats, impacting species diversity and reducing the ecosystem's resilience. There are numerous unique characteristics of any ecosystem that are of significance, however this research focuses on 3 primary environments – open water, seafloor & human coastal communities. 

To combat this, this study employs data science techniques to inform relationships between target features through multivariate variate analysis and the construction of 3 models of varying complexity. This research necessitates investigation of 3 environments: the open water, 

The first is a baseline Linear Regression in combination with PCA or CCA. The second is a SARIMAX time-series forecasting model. Finally, this project will employ Recurrent Neural Networks, LSTMs, with the intent of uncovering the more complex relationship in the data and between all the features targeted in this study. 
These models are intended to leverage a diverse approach to ecosystem health, further enabling complex predictive models and promoting progressive and front facing approaches to conservation. 
The final objective of this case study is to demonstrate the power of data science, analytics and machine learning and its ability to affect positive change in society and the management of our coastal ecosystems and the benefits they provide. 

## 2) Current Status
Majority of Exploratory Data Analysis (EDA) has been completed. Higher level tests for correlation and multi/collinearity during the creation of these models.
Minor processing is required for land development statistics. The current subset data set is robust enough to create baseline models; the additional data will increase the dataset threefold and should serve to reinforce any relationships identified. These are being delivered gathered by a secondary source. Information can be found in the references at the end of the page.
2 phases of models are required for the execution of this project. This is required because these indices represent 3 different environments. The first phase will involve validating relationships and their predictive power; secondly, these calculated features will be evaluated with or against each other to examine pressures found in benthic, pelagic and anthropogenic habitats. 
Present work includes creation of Linear, Lasso, Ridge regression models for the evaluation of organism sampling and environmental data in predicting the SDI (Shannon Diversity Index) for the pelagic and benthic habitats over time. Hyperparameters and dimension reduction techniques have been applied and are discussed below. There has been success with basic Linear regressions on other phase 1 models. Additionally, other more complex tests for correlation are to begin, such as CCA and a time series analysis.
Missing Data: real estate records for coastal properties. This data is being available but is being processed. It is being delivered at regular intervals - however, it is not complete. It should not present an issue when building baseline models; however, the data set will increase threefold from its current length. Cleaning and EDA processes are established for efficient processing of the data.
Specific Progress Markers since last update:
Regression Models:
-	Scaled Standard Linear Regression
-	Scaled Lasso and Ridge with hyperparameter tuning
-	Scaled population growth (univariate)

Advanced EDA techniques:
-	PCA reduction & plotting
-	Time series decomposition
-	
General EDA:
-	Evaluation of seasonality
-	Population growth metrics
-	Engineered Coastal Development metrics

Data Processing:
-	Processing real estate construction, human population dynamics data
-	Acquired GeoSpatial and aerial photography. This data may not be included in this study due to time restraints and lack of proficiency with freely available software.

## Existing Research:

The final models for consideration will evaluate 4 target index features. TBEP, a conservation research group, has been at the forefront of scientific research for the Tampa Bay ecosystem with multiple affiliations to national, academic and local government institutions.

TBEP (Tampa Bay Estuarine Program) has developed 2 novel indices to represent the health of (A) Benthic (seafloor) ecosystems and (B) the semi-pelagic or open water ecosystem.
The 3rd index is a calculated feature: the Shannon Diversity Index - a weighted measurement that balances species richness and abundance. 
- Species richness is the number of species in a given area
- Species abundance is the number of individuals within a given species or taxonomical grouping.

The most common approach is to examine past relationships to inform concepts and relationships within a complex environment, utilizing descriptive statistics to answer current problem. This approach is most common because, at the resolution of local ecosystems, accounting for the multitude of associated features can make the construction of an accurate and precise forecasting model a difficult.

## Description of Work: Changes in Scope of Study
	After Sprint 1, it became clear that the scope of my project as initially designed was beyond the scope of this course. The number of natural habitats were reduced from 4 to 2 with the emphasis now on the 2 fundamental environments that describe coastal ecosystem health: nekton/pelagic (free swimming) and benthic (seafloor). The original object, the employment of ML and statistical models in the evaluation of successful environmental mitigation tools in coastal construction would take a large additional dataset along with high amounts of geospatial data.
The project still matinains the objectigve of creating a final calculated feature, represented as the weighted aggregate of factors that exert influence. This framework uses an adapted form of Passche’s Price index which would enable tracking the weight or influence on any given human induced selective pressure on ecosystem health. This proposed index has a lose conceptual tie to the HII index: the Human Influence Index, which describes human impact on terrestrial ecosystems. 
	An adapted form of Passche’s price index will be the framework for a weighted aggregate index of human selective pressures on the environment 

### Preliminary Analysis Methodologies

No significant regression analysis has been performed on the processed data yet. Given the differences in scale of independent variables, normalized regression methods will be required to accurately represent continuous data.

The reduction of features in the data, implementation of dummy variables, and examination of collinearity and multicollinearity are ongoing. Multicollinearity is present in the data, as expected. Measurements, such as temperature at the top vs. the sea floor, can have relatively little variation; however, they remain important.

Estuarine systems comprise a portion of the data – these systems are highly stratified by salinity and temperature, necessitating their inclusion in the EDA. This will be especially relevant when the data starts to account for sampling in overlapping environments, such as seagrass beds, which requires segmentation of those data.

### Advanced EDA
Nekton/Benthic Diversity Index: 170 columns / independent (secondary) features
-	Examination of the pelagic and benthic biodiversity index scores through traditional forms of correlation analysis proved difficult.
-	Correlation heatmaps did not demonstrate significant correlation between independent variables.
-	VIF analysis provided little evidence of multicollinearity, the exception to which was 2 species with low sample quantities. 	 

## Description of Data
. This will be relative to the key features that are used to describe human influences:
1.	Nitrate and Phosphate concentrations: Gross quantities and ratios of organic to inorganic forms of these compounds are strong indicators of human influence
2.	Coastal Development rate  

Data has been acquired from various sources in multiple formats. Development is measured by proxy as the number of new homes or buildings built per year. Anthropogenic data describes coastal construction, maritime activity, and artificial nitrogen loading from local agriculture, residential communities, and commercial sites.
A list of the current datasets can be found in the references at the end of this document.

## Target Features: Indices and Supplementary Data of Interest

### Shannon-Weiner Diversity Index

A proxy measurement of overall ecosystem health and complexity.

Calculation of this index is calculated as:

```
s
H’ = - Σ pi ln pi
i =1
```

Where H’ is the Species Diversity Index (SDI), s is the number of species, and pi is the proportion of individuals of each species belonging to the ith species of the total number of individuals.

### Tampa Bay Benthic Index (TBBI)

TBBI is an ecosystem-specific index formulated by the Tampa Bay Estuary Program to describe ecosystem health. This value is calculated by a series of transformations of environmental and biological values, including linear regression, linear discriminant analysis, and normalization. The description of this transformation can be found in the referenced literature at the end of this document.

## Results

### _Updated_ EDA Summary (in italics)

EDA has revealed some key aspects about the data:
* Measurements for benthic habitat is problematic due to the sample design. Interval between measurements is 2 years and only during the summer months. This will make any time of time series analysis difficult; however, if nekton and benthic sampling months are lined up, they are both follow the same overall structure and display the same type of seasonality within the data.
* Species Richness should closely relate to SDI but the relationship isn’t that strong indicating that there is another factor impacting this relationship.
*   Species Richness and SDI have become weaker in recent years. Richness has trended upwards while Diversity has decreased since 2015.
p

## Detailed Description of EDA Analysis

So far, a subset of benthic ecosystem data has been cleaned and used for a preliminary EDA. This subset focuses on the geographic region surrounding the case study construction site. The raw data describes sediment toxicology, standard practice sampling information (GPS, temperature, salinity, dates), and species collection.

As this dataset was explored, the need for a standardized measurement of ecosystem health became apparent. Due to its wide applicability in any given environment, it was determined that the Shannon-Weiner Diversity Index (SDI) could potentially represent a normalized value. This would allow for measurements and comparisons among ecosystems. Ultimately, with supplementary data, it can be used to create a composite, weighted index to represent the overall health of Tampa Bay.

Plotting the overall datasets demonstrates sampling in various habitats throughout the bay and nearby coastal systems. The dataset is comprehensive and will be sufficient, in complement with other datasets, for the overall goals of this study.

In a healthy ecosystem, SDI is expected to have a close relationship with Species Richness. It is surprising that the correlation between the two isn’t as strong over time as expected in the data. This could be due to the distribution of sampling over time or indicate stress on the ecosystem from outside pressures. In this case, species richness has trended upwards while diversity has returned to original levels from when data collection began.

## Future Work

* Explore second model - SARIMAX, CCA and Passche Index Framework
* Further tune Linear models to improve scoring

## References

Aarnio, K., Mattila, J., Törnroos, A., Bonsdorff, E., 2011. Zoobenthos as an environmental quality element: the ecological significance of sampling design and functional traits. 
Airoldi, L., Beck, M.W., 2007. Loss, status and trends for coastal marine habitats of Europe. 
Allan, J.D. 2004. Landscapes and riverscapes: The influence of land use on stream ecosystems. Allen, D., S. Haertel-Borer, B. Milan, D. Bushek, and R. Dame. 2007. Geomorphological determinants of nekton use of intertidal salt marsh creeks. 
Allaire, J. J., Gandrud, C., Russell, K., and Yetman, C. (2017). networkD3: D3 JavaScript network graphs from R. Available at: https://CRAN.R-project.org/package-networkD3. 
Anderson, M.J., Walsh, D.C.I., 2013. PERMANOVA, ANOSIM, and the Mantel test in the face of heterogeneous dispersions: what null hypothesis are you testing? 
Andersen, K.H., Berge, T., Gonçalves, R.J., Hartvig, M., Heuschele, J., Hylander, S., Jacobsen, N.S., Lindemann, C., Martens, E.A., Neuheimer, A.B., Olsson, K., Palacz, A., Prowe, A.E.F., Sainmont, J., Traving, S.J., Visser, A.W., Wadhwa, N., Kiørboe, T., 2016. Characteristic sizes of life in the oceans, from bacteria to whales. 
Appelberg, M., Berger, H.-M., Hesthagen, T., Kleiven, E., Kurkilahti, M., Raitaniemi, J., Rask, M., 1995. Development and intercalibration of methods in nordic freshwater fish monitoring. 
Arnold Jr., C.L., and C.J. Gibbons. 1996. Impervious surface coverage: The emergence of a key environmental indicator. 
Ash, T., and Runnels, R. (2005). Hard bottom habitats: an overview of mapping and monitoring needs on epibenthic communities in Tampa Bay, Florida. 
Ávila-García, D., Morató, J., Pérez-Maussán, A. I., Santillán-Carvantes, P., and Alvarado, J. (2020). Impacts of alternative land-use policies on water ecosystem services in the Rio Grande de Comitan-Lagos de Montebello watershed. 
Bauer, R.K., 2018. Oceanmap: A Plotting Toolbox for 2D Oceanographic Data. 
Beauchard, O., Veríssimo, H., Queirós, A.M., Herman, P.M.J., 2017. The use of multiple biological traits in marine community ecology and its potential in ecological indicator development.
Beck, M. W., Raulerson, G. E., and Sherwood, E. T. (2022). Tbep-tech/hmpu-workflow: v1.2.0. Zenodo.
Beck, M.W., K.L. Heck Jr., K.W. Able, D.L. Childers, D.B. Eggleston, B.M. Gillanders, B.
Halpern, C.G. Hays, L. Hoshino, T.



