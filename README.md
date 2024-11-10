# Disease Incidence and Population Impact Analysis (2001-2022)

**Author:** Oluwatoba B. Adeyemi  
**Institution:** Northwest Missouri State University, Maryville MO 64468, USA  
**Email:** [S572876@nwmissouri.edu](mailto:S572876@nwmissouri.edu) | [adeyemioluwatoba25@gmail.com](mailto:adeyemioluwatoba25@gmail.com)

## Abstract

This project examines disease incidence trends across California counties from 2001 to 2022, focusing on gender disparities and geographical hotspots. Using data from the California Department of Public Health, it highlights patterns in infectious diseases, analyzes the impact on different population groups, and provides actionable insights for public health interventions. Tableau and Microsoft Excel are utilized for data visualization, emphasizing significant trends and disparities.

## Keywords

- Data Analytics
- Disease Incidence
- Population Impact
- Data Visualization
- Impact Analysis

## Table of Contents

1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Objective](#objective)
4. [Methodology](#methodology)
    - [Data Source](#data-source)
    - [Data Preparation](#data-preparation)
    - [Data Attributes](#data-attributes)
5. [Data Analysis](#data-analysis)
6. [Discussion](#discussion)
7. [Conclusion](#conclusion)
8. [Project Resources](#project-resources)
9. [Setup Instructions](#setup-instructions)
10. [Data Analysis Workflow](#data-analysis-workflow)

---

## Introduction

Public health and epidemiology play key roles in understanding disease spread and its impact on populations. This project analyzes disease incidence in California, focusing on trends, disparities, and geographical hotspots from 2001 to 2022.

## Problem Statement

This analysis investigates trends in disease incidence, gender disparities, and geographical hotspots across California counties. The focus is on understanding how infectious disease patterns have varied over time and identifying areas of concern.

## Objective

The objective of this project is to analyze disease incidence trends, identify gender disparities, and highlight geographical hotspots. The analysis provides insights into counties with high incidence rates, such as Inyo and Kern, and areas with lower rates like San Francisco and Sacramento.

---

## Methodology

### Data Source

The dataset is sourced from [data.gov](https://data.gov), covering disease incidence by county, year, gender, and population for California from 2001 to 2022. It contains 189,921 records and is supported by the California Department of Public Health.

### Data Preparation

The dataset was cleaned using Python in VSCode, handling missing values and ensuring consistency. Confidence intervals were calculated following public health standards to accurately represent trends.

### Data Attributes

The dataset includes the following key attributes:
- **Year:** Temporal reference for trend analysis.
- **California:** Total disease cases statewide.
- **Counties (Kern, Los Angeles, Orange, San Diego):** County-level disease cases for comparative analysis.

---

## Data Analysis

### Overview of Disease Incidence

The analysis revealed trends in disease incidence from 2001 to 2022, with significant increases in certain diseases like Anaplasmosis in Alameda County and seasonal variations in Lyme disease.

### Trend Analysis

Notable changes in disease rates were observed during 2019-2020, likely influenced by the COVID-19 pandemic.

### Population Impact

High-population counties like Los Angeles showed large case numbers, while smaller counties like Inyo had higher per capita incidence rates, indicating additional contributing factors.

---

## Discussion

### Key Findings

1. **Disease Trends:** Seasonal peaks were observed for Lyme disease. Gender disparities showed higher rates for vector-borne diseases in males and higher rates for certain infections like Chlamydia in females.
2. **Geographical Hotspots:** Inyo and Kern counties were identified as significant hotspots, while San Francisco and Sacramento had lower incidence rates.

### Implications for Public Health

The findings suggest targeted health interventions could be more effective if focused on identified hotspots and tailored to address gender disparities.

### Limitations

The analysis is limited to the diseases included in the dataset and California counties only. External factors like policy changes or healthcare access were not considered, and no predictive modeling was performed.

---

## Conclusion

### Summary of Findings

The analysis identified major trends in disease incidence, highlighted geographical hotspots, and uncovered gender-based disparities. Population density played a role in disease spread, but some smaller counties showed high per capita rates.

### Recommendations

Public health officials should focus on identified hotspots and consider gender-based interventions. Future research could integrate machine learning models for predictive analysis of disease outbreaks.

---

## Project Resources

- [Data.gov Dataset](https://catalog.data.gov/dataset/infectious-diseases-by-disease-county-year-and-sex-6e856)
- [GitHub Repository](https://github.com/Adeyemitoba/Disease-Incidence-Analysis-2001-2022)
- [Overleaf Project](https://www.overleaf.com/project/6716bc6ade42a8c3ebd0e744)
- Tableau Dashboard

---

## Setup Instructions

1. **Install JupyterLab:**
   ```bash
   pip install jupyterlab
