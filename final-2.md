# Anthropogenic-Based Ecosystem Pressure Evaluation Index Metric: A Case Study of the Northern Tampa Bay Estuary

## Table of Contents

1.  [Introduction](#introduction)
2.  [Project Description](#project-description)
3.  [Current Status](#current-status)
4.  [Progress History](#progress-history)
5.  [Data Description](#data-description)
6.  [Model Design](#model-design)
7.  [EDA and Preprocessing](#eda-and-preprocessing)
8.  [Baseline Models](#baseline-models)
9.  [Results](#results)
10. [Changes to Scope of Study](#changes-to-scope-of-study)
11. [Conclusions](#conclusions)
12. [References](#references)
13. [Acknowledgements](#acknowledgements)
14. [License](#license)

## 1. Introduction

<br>
<!-- *Insert picture here* -->
<br>

![Coast_changeanimate.gif](./notebooks/images/)
<br>

![Coast_changeanimate.gif](./notebooks/images/coast_changeanimated.gif)
<br>
[Context](#context)

[Research Review](#research-review)

## 2\. Project Description

[Objectives Defined](#objectives-defined)

## 3\. Current Status

Majority of Exploratory Data Analysis (EDA) has been completed.

Higher level tests for correlation and multi/collinearity during the creation of these models.

Minor processing is required for land development statistics. The current subset data set is robust enough to create baseline models;

the additional data will increase the dataset threefold and should serve to reinforce any relationships identified.

These are being delivered gathered by a secondary source. Information can be found in the references at the end of the page.

## 4\. Progress History

2 phases of models are required for the execution of this project.

This is required because these indices represent 3 different environments.

The first phase will involve validating relationships and their predictive power;

secondly, these calculated features will be evaluated with or against each other to examine pressures found in benthic, pelagic and anthropogenic habitats.

Present work includes creation of Linear, Lasso, Ridge regression models for the evaluation of organism sampling and environmental data in predicting the SDI (Shannon Diversity Index) for the pelagic and benthic habitats over time.

Hyperparameters and dimension reduction techniques have been applied and are discussed below.

There has been success with basic Linear regressions on other phase 1 models.

Additionally, other more complex tests for correlation are to begin, such as CCA and a time series analysis.

## 5\. Data Description, Methodologies, EDA Results, Data Preparation for Final Model:

[Data Description](#data-description)

[Model Design](#model-design)

[EDA, Pre-Processing](#processing-eda-findings)

[Baseline Models](#baseline-models)

## 6\. Results

[Results of Environmental Data Modelling](#results)

[Results of Anthropogenic Modelling](#results)

[Formation of a New Index](#formation-of-a-new-index)

## 7\. Changes to Scope of Study

[Changes to Scope of Study](#changes-to-scope-of-study)

## 8\. Conclusions

[Conclusions](#conclusions)

## 9\. References

[References](#references)

## 10\. Acknowledgements

[Acknowledgements](#acknowledgements)

## 11\. License

[License](#license)

# Content

## 1\. Introduction

### a. Context

### b. Research Review

## 2\. Project Description

### Obectives:

## 3\. Current Status

## 4\. Progress History

## 5\. Data Description, Methodologies, EDA Results, Data Preparation for Final Model

### a. data Description

### b. Model Design

### c. Processing & EDA Findings

### d. Baseline Models: Establishing Feature Representation

## 6\. Results

### a. Results of Environmental Data Modelling

### b. Results of Anthropogenic Modelling

### c. Formation of a New Index

## 7\. Changes to Scope of Study

## 8\. Conclusions

## 9\. References

## 10\. Acknowledgements

## 11\. License

## Existing Research:

The final models for consideration will evaluate 4 target index features.

TBEP, a conservation research group, has been at the forefront of scientific research for the Tampa Bay ecosystem with multiple affiliations to national, academic and local government institutions.

TBEP (Tampa Bay Estuarine Program) has developed 2 novel indices to represent the health of (A) Benthic (seafloor) ecosystems and (B) the semi-pelagic or open water ecosystem.

The 3rd index is a calculated feature: the Shannon Diversity Index - a weighted measurement that balances species richness and abundance.

  - Species richness is the number of species in a given area

  - Species abundance is the number of individuals within a given species or taxonomical grouping.

The most common approach is to examine past relationships to inform concepts and relationships within a complex environment, utilizing descriptive statistics to answer current problem.

This approach is most common because, at the resolution of local ecosystems, accounting for the multitude of associated features can make the construction of an accurate and precise forecasting model a difficult.

## Description of Work: Changes in Scope of Study

After Sprint 1, it became clear that the scope of my project as initially designed was beyond the scope of this course.

The number of natural habitats were reduced from 4 to 2 with the emphasis now on the 2 fundamental environments that describe coastal ecosystem health: nekton/pelagic (free swimming) and benthic (seafloor).

The original object, the employment of ML and statistical models in the evaluation of successful environmental mitigation tools in coastal construction would take a large additional dataset along with high amounts of geospatial data.

The project still matinains the objectigve of creating a final calculated feature, represented as the weighted aggregate of factors that exert influence.

This framework uses an adapted form of Passche’s Price index which would enable tracking the weight or influence on any given human induced selective pressure on ecosystem health.

This proposed index has a lose conceptual tie to the HII index: the Human Influence Index, which describes human impact on terrestrial ecosystems.

An adapted form of Passche’s price index will be the framework for a weighted aggregate index of human selective pressures on the environment

### Preliminary Analysis Methodologies

No significant regression analysis has been performed on the processed data yet.

Given the differences in scale of independent variables, normalized regression methods will be required to accurately represent continuous data.

The reduction of features in the data, implementation of dummy variables, and examination of collinearity and multicollinearity are ongoing.

Multicollinearity is present in the data, as expected. Measurements, such as temperature at the top vs. the sea floor, can have relatively little variation;

however, they remain important.

Estuarine systems comprise a portion of the data – these systems are highly stratified by salinity and temperature, necessitating their inclusion in the EDA.

This will be especially relevant when the data starts to account for sampling in overlapping environments, such as seagrass beds, which requires segmentation of those data.

### Advanced EDA

Nekton/Benthic Diversity Index: 170 columns / independent (secondary) features

  - Examination of the pelagic and benthic biodiversity index scores through traditional forms of correlation analysis proved difficult.

  - Correlation heatmaps did not demonstrate significant correlation between independent variables.

  - VIF analysis provided little evidence of multicollinearity, the exception to which was 2 species with low sample quantities.

## Description of Data

. This will be relative to the key features that are used to describe human influences:

1.  Nitrate and Phosphate concentrations: Gross quantities and ratios of organic to inorganic forms of these compounds are strong indicators of human influence

2.  Coastal Development rate

Data has been acquired from various sources in multiple formats.

Development is measured by proxy as the number of new homes or buildings built per year.

Anthropogenic data describes coastal construction, maritime activity, and artificial nitrogen loading from local agriculture, residential communities, and commercial sites.

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

TBBI is an ecosystem-specific index formulated by the Tampa Bay Estuary Program to describe ecosystem health.

This value is calculated by a series of transformations of environmental and biological values, including linear regression, linear discriminant analysis, and normalization.

The description of this transformation can be found in the referenced literature at the end of this document.

## Results

### *Updated* EDA Summary (in italics)

EDA has revealed some key aspects about the data:

  * Measurements for benthic habitat is problematic due to the sample design.

Interval between measurements is 2 years and only during the summer months.

This will make any time of time series analysis difficult;

however, if nekton and benthic sampling months are lined up, they are both follow the same overall structure and display the same type of seasonality within the data.

  * Species Richness should closely relate to SDI but the relationship isn’t that strong indicating that there is another factor impacting this relationship.

  * Species Richness and SDI have become weaker in recent years.

Richness has trended upwards while Diversity has decreased since 2015.

p

## Detailed Description of EDA Analysis

So far, a subset of benthic ecosystem data has been cleaned and used for a preliminary EDA.

This subset focuses on the geographic region surrounding the case study construction site.

The raw data describes sediment toxicology, standard practice sampling information (GPS, temperature, salinity, dates), and species collection.

As this dataset was explored, the need for a standardized measurement of ecosystem health became apparent.

Due to its wide applicability in any given environment, it was determined that the Shannon-Weiner Diversity Index (SDI) could potentially represent a normalized value.

This would allow for measurements and comparisons among ecosystems. Ultimately, with supplementary data, it can be used to create a composite, weighted index to represent the overall health of Tampa Bay.

Plotting the overall datasets demonstrates sampling in various habitats throughout the bay and nearby coastal systems.

The dataset is comprehensive and will be sufficient, in complement with other datasets, for the overall goals of this study.

In a healthy ecosystem, SDI is expected to have a close relationship with Species Richness.

It is surprising that the correlation between the two isn’t as strong over time as expected in the data.

This could be due to the distribution of sampling over time or indicate stress on the ecosystem from outside pressures.

In this case, species richness has trended upwards while diversity has returned to original levels from when data collection began.

## Future Work

  * Explore second model - SARIMAX, CCA and Passche Index Framework

  * Further tune Linear models to improve scoring

## Dependencies

  * List the specific software packages and libraries required to run