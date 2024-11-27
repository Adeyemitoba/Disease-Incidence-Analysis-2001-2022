# Disease Incidence and Population Impact Analysis (2001-2022)

## Overview
This project analyzes infectious disease trends in California counties from 2001 to 2022. Using advanced data analytics techniques, the report identifies key trends, gender disparities, and geographical hotspots. Predictive modeling is also utilized to forecast future disease trends, providing actionable insights for public health interventions.

## Key Findings
1. **Disease Trends:**
   - A steady rise in Campylobacteriosis cases.
   - Seasonal variations in Lyme disease.
   - A decline in some diseases coinciding with public health measures during the COVID-19 pandemic (2019–2020).

2. **Geographical Hotspots:**
   - High incidence in counties like **Los Angeles** and **Kern**.
   - Lower rates in counties like **San Francisco** and **Sacramento**.

3. **Gender Disparities:**
   - Higher incidence rates for vector-borne diseases in males.
   - Females exhibited higher rates of sexually transmitted diseases, including Chlamydia.

4. **Population Impact:**
   - High population density correlates with higher disease counts.
   - Per capita analysis revealed that less populous counties like Inyo showed disproportionate case rates.

## Methodology
### Data Preparation
- Data cleaning was performed using Python to handle missing values and standardize formats.
- Tableau was used for geospatial and demographic analysis.
- Confidence intervals and derived measurements were calculated for accuracy.

### Analysis Techniques
- **Time Series Forecasting:** 
  - ARIMA modeling to predict trends.
  - Example: Projected rise in Campylobacteriosis cases over the next five years.
- **Geospatial Mapping:**
  - Visualized disease hotspots across California.
- **Demographic Analysis:**
  - Explored gender disparities in disease incidence.

## Results
## Visualizations of Disease Trends

### 1. Population Size vs. Disease Incidence
![Population vs Disease](./images/population_vs_disease.png)
*This scatter plot shows the relationship between population size and disease incidence.*

### 2. Forecast of Campylobacteriosis Cases
![Forecast Cases](./images/forecast_cases.png)
*Forecast of Campylobacteriosis cases including historical data and predictions.*

### 3. Historical Trend of Campylobacteriosis Cases
![Historical Trend](./images/historical_trend.png)
*Line chart showing annual Campylobacteriosis cases from 2001 to 2022.*

### 4. Geographical Hotspots of Disease Incidence
![Geographical Hotspots](./images/tableau_map.png)
*Map of California counties with the highest disease incidence.*

### 5. Top 10 Counties by Disease Incidence
![Top 10 Counties](./images/top_ten_county.png)
*Bar chart displaying the top 10 counties with the highest disease incidence.*

### Key Deliverables
- **Data Insights**: Detailed report highlighting disease patterns and their implications.
- **Forecasting Model**: ARIMA-based predictive analysis for selected diseases.
- **Interactive Dashboard**: Tableau dashboard for exploring disease trends and demographics ([View Dashboard](https://public.tableau.com/views/CapstoneDashboard_17305693049120/Dashboard)).
- **Code Repository**: Python scripts and notebooks for data cleaning and modeling ([View on GitHub](https://github.com/Adeyemitoba/Disease-Incidence-Analysis-2001-2022)).
- **LaTeX Report**: Comprehensive report prepared in Overleaf ([View on Overleaf](https://www.overleaf.com/read/vnpwhvzfnzht)).

## Recommendations
1. Prioritize public health resources in identified hotspots.
2. Address gender disparities through targeted interventions.
3. Expand predictive modeling to incorporate additional factors such as policy impacts and healthcare access.

## References
1. Dataset sourced from [Data.gov](https://catalog.data.gov/dataset/infectious-diseases-by-disease-county-year-and-sex-6e856).
2. California Department of Public Health reports.


