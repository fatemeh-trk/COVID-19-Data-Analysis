# Data Understanding

## Dataset Overview

### Table: CovidDeaths

| Property | Description |
|----------|-------------|
| **Table Name** | CovidDeaths |
| **Purpose** | Stores daily country-level COVID-19 statistics, including confirmed cases, deaths, testing, hospitalization, and other health-related indicators. |
| **Granularity** | One row represents one country (or region) on one specific reporting date. |
| **Time Coverage** | Daily records covering the COVID-19 pandemic period. *(The exact date range will be verified during Data Profiling.)* |
| **Geographic Coverage** | Global (Countries and regions worldwide). |
| **Logical Primary Key** | `(location, date)` |
| **Number of Columns** | 59 |
| **Estimated Number of Rows** | To be determined during Data Profiling. |
| **Data Source** | Our World in Data (OWID) |
| **Update Frequency** | Daily |


### Table: CovidVaccinations

| Property | Description |
|----------|-------------|
| **Table Name** | CovidVaccinations |
| **Purpose** | Stores daily country-level COVID-19 vaccination statistics and health-related indicators, including vaccination progress, testing, healthcare capacity, demographic characteristics, and other factors that may influence the spread and impact of COVID-19. |
| **Granularity** | One row represents one country (or region) on one specific reporting date. |
| **Time Coverage** | Daily records covering the COVID-19 pandemic period. *(The exact date range will be verified during Data Profiling.)* |
| **Geographic Coverage** | Global (Countries and regions worldwide). |
| **Logical Primary Key** | `(location, date)` |
| **Number of Columns** | 37 |
| **Estimated Number of Rows** | To be determined during Data Profiling. |
| **Data Source** | Our World in Data (OWID) |
| **Update Frequency** | Daily |


## Data Dictionary

###core columns

####column:location
| Property           | Value                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------- |
| **Column Name**    | location                                                                               |
| **Description**    | Represents the name of a country or region.                                            |
| **Data Type**      | Text                                                                                   |
| **Unit**           | N/A                                                                                    |
| **Business Usage** | Used for filtering, grouping, country-level comparison, trend analysis, and reporting. |


####column:continent
| Property           | Value                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------- |
| **Column Name**    | continent                                                                                   |
| **Description**    | Indicates the continent to which a country or region belongs.                               |
| **Data Type**      | Text                                                                                        |
| **Unit**           | N/A                                                                                         |
| **Business Usage** | Used for continent-level analysis, regional comparison, reporting, filtering, and grouping. |

####column:date
| Property           | Value                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| **Column Name**    | date                                                                                                  |
| **Description**    | Represents the reporting date for COVID-19 statistics.                                                |
| **Data Type**      | Date                                                                                                  |
| **Unit**           | YYYY-MM-DD                                                                                            |
| **Business Usage** | Used for time-series analysis, trend analysis, filtering, grouping, period comparison, and reporting. |


####column:population 
| Property           | Value                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| **Column Name**    | population                                                                                                                       |
| **Description**    | Represents the total population of a country or region.                                                                          |
| **Data Type**      | Numeric *(to be validated during Data Profiling)*                                                                                |
| **Unit**           | People                                                                                                                           |
| **Business Usage** | Used to calculate per-capita metrics, normalize COVID-19 indicators, compare countries fairly, and support analytical reporting. |


####column:new_cases
| Property           | Value                                                                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Column Name**    | new_cases                                                                                                                                                     |
| **Description**    | Indicates the number of newly confirmed COVID-19 cases reported for a specific country or region on a given date.                                             |
| **Data Type**      | Numeric *(to be validated during Data Profiling)*                                                                                                             |
| **Unit**           | People                                                                                                                                                        |
| **Business Usage** | Used to analyze daily infection trends, monitor pandemic growth, calculate infection rates, compare countries over time, and support public health reporting. |



####column:total_cases
| Property           | Value                                                                                                                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Column Name**    | total_cases                                                                                                                                                                       |
| **Description**    | Represents the cumulative number of confirmed COVID-19 cases reported for a country or region up to the reporting date.                                                           |
| **Data Type**      | Numeric *(to be validated during Data Profiling)*                                                                                                                                 |
| **Unit**           | People                                                                                                                                                                            |
| **Business Usage** | Used to analyze cumulative infection trends, monitor the overall spread of the pandemic, calculate per-capita indicators, compare countries, and support public health reporting. |



####column:new_deaths
| Property           | Value                                                                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Column Name**    | new_deaths                                                                                                                                                         |
| **Description**    | Represents the number of newly reported COVID-19 deaths for a country or region on a specific reporting date.                                                      |
| **Data Type**      | Numeric *(to be validated during Data Profiling)*                                                                                                                  |
| **Unit**           | People                                                                                                                                                             |
| **Business Usage** | Used to analyze daily mortality trends, monitor the severity of the pandemic, compare countries, calculate mortality indicators, and support healthcare reporting. |

#### 

| Column Name | Description | Data Type | Unit | Business Usage |
|--------------|-------------|-----------|------|----------------|
| total_deaths | Represents the cumulative number of confirmed COVID-19 deaths reported for a country or region up to the reporting date. | Numeric *(To be validated during Data Profiling)* | People | Used to analyze cumulative mortality, compare countries, calculate mortality indicators, and support public health reporting. |
| people_vaccinated | Represents the cumulative number of people who have received at least one dose of a COVID-19 vaccine. | Numeric *(To be validated during Data Profiling)* | People | Used to measure vaccination coverage, compare countries, calculate vaccination rates, and evaluate vaccination progress. |
| people_fully_vaccinated | Represents the cumulative number of people who have completed the full COVID-19 vaccination schedule. | Numeric *(To be validated during Data Profiling)* | People | Used to evaluate population immunity, compare vaccination completion rates, and support vaccination strategy analysis. |
| total_vaccinations | Represents the cumulative number of vaccine doses administered. | Numeric *(To be validated during Data Profiling)* | Doses | Used to analyze vaccination progress, compare vaccination campaigns, and support healthcare planning. |
| new_vaccinations | Represents the number of vaccine doses administered on a specific reporting date. | Numeric *(To be validated during Data Profiling)* | Doses | Used to analyze daily vaccination trends, monitor campaign progress, and evaluate vaccination performance. |
| hospital_beds_per_thousand | Represents the number of hospital beds available per 1,000 people. | Numeric *(To be validated during Data Profiling)* | Beds per 1,000 people | Used to evaluate healthcare capacity, compare countries, and support healthcare resource planning. |
| hosp_patients | Represents the number of hospitalized COVID-19 patients on a specific reporting date. | Numeric *(To be validated during Data Profiling)* | People | Used to monitor hospital occupancy, evaluate healthcare demand, and support resource allocation. |
| icu_patients | Represents the number of COVID-19 patients admitted to intensive care units on a specific reporting date. | Numeric *(To be validated during Data Profiling)* | People | Used to monitor critical cases, evaluate ICU capacity, and support emergency healthcare planning. |
| median_age | Represents the median age of the population in a country or region. | Numeric *(To be validated during Data Profiling)* | Years | Used to analyze demographic characteristics, compare countries, and study the relationship between age and COVID-19 outcomes. |
| aged_65_older | Represents the percentage of the population aged 65 years or older. | Numeric *(To be validated during Data Profiling)* | Percentage (%) | Used to identify high-risk populations, compare demographic structures, and analyze mortality risk. |
| aged_70_older | Represents the percentage of the population aged 70 years or older. | Numeric *(To be validated during Data Profiling)* | Percentage (%) | Used to evaluate vulnerable populations, support demographic analysis, and assess mortality risk. |
| new_cases_per_million | Represents the number of newly reported COVID-19 cases per one million people. | Numeric *(To be validated during Data Profiling)* | Cases per million people | Used to compare infection levels fairly across countries regardless of population size. |
| total_cases_per_million | Represents the cumulative number of confirmed COVID-19 cases per one million people. | Numeric *(To be validated during Data Profiling)* | Cases per million people | Used to compare cumulative infection burden across countries. |
| new_deaths_per_million | Represents the number of newly reported COVID-19 deaths per one million people. | Numeric *(To be validated during Data Profiling)* | Deaths per million people | Used to compare daily mortality levels across countries fairly. |
| total_deaths_per_million | Represents the cumulative number of COVID-19 deaths per one million people. | Numeric *(To be validated during Data Profiling)* | Deaths per million people | Used to compare cumulative mortality burden across countries and regions. |
