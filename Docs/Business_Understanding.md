# COVID-19 Data Analysis

## Project Overview

This project analyzes global COVID-19 data using the Our World in Data (OWID) dataset to explore the spread of the pandemic, mortality trends, and vaccination progress across different countries. The objective is to transform raw data into meaningful insights that support data-driven decision-making in public health. The project combines PostgreSQL, Python, and Power BI to perform data analysis, create interactive dashboards, and communicate findings through effective storytelling.

## Project Scenario

Assume that the Ministry of Health is responsible for monitoring the global COVID-19 situation and improving preparedness for future public health emergencies. As a Data Analyst, the responsibility of this project is to analyze pandemic data, identify meaningful patterns, evaluate vaccination progress, and provide analytical insights that support strategic decision-making and resource planning.

## Data Sources

The analysis is based on the COVID-19 dataset published by Our World in Data (OWID), which aggregates publicly available data from trusted international organizations, including the World Health Organization (WHO) and other official public health agencies.

Main datasets used:

- CovidDeaths
- CovidVaccinations

The datasets contain daily country-level information about confirmed cases, deaths, testing, vaccination, population, and other related indicators.



## Project Goals

## Stakeholders

The primary stakeholders of this project include:

- Ministry of Health
- Public Health Decision Makers
- Hospital Administrators
- Vaccination Program Managers
- Health Policy Makers
- Researchers and Data Analysts

These stakeholders can use the analytical results to monitor pandemic trends, allocate healthcare resources, evaluate vaccination strategies, and support evidence-based decision-making.

## KPIs

## Business Questions

### 1. Pandemic Trend Analysis
Which countries have demonstrated a sustained decrease in COVID-19 infection and mortality rates relative to their population over time?

### 2. Vaccination Effectiveness
To what extent did COVID-19 vaccination programs contribute to reducing infection and mortality trends across different countries?

### 3. Geographic Impact Assessment
Which continents and countries were most severely affected by COVID-19 based on infection, mortality, and vaccination indicators?

### 4. Resource Allocation
Which countries or regions should be prioritized for healthcare resource allocation based on infection trends, mortality rates, and vaccination coverage?

### 5. Healthcare Performance Evaluation
Which countries achieved the best overall pandemic management performance considering infection control, mortality reduction, and vaccination progress?

### 6. Population Risk Assessment
How do demographic factors such as population size and age distribution relate to COVID-19 infection and mortality rates?

### 7. Future Pandemic Preparedness
What patterns and lessons can be identified from historical COVID-19 data to support preparedness for future public health emergencies?


## Q1 Analysis Methodology

To answer the first business question, a trend analysis was performed using Linear Regression on 7-day moving averages of COVID-19 cases and deaths.

### Analysis Process

1. Calculate a 7-day moving average for:
   - New Cases
   - New Deaths

2. Remove missing values.

3. Evaluate only countries with at least 30 valid observations.

4. Analyze the most recent 180 days of data.

5. Apply Linear Regression where:
   - X = Time (days)
   - Y = 7-day moving average

6. Evaluate:
   - Slope
   - R² (Coefficient of Determination)

7. Selection Criteria

Countries were considered to have a sustained decreasing trend if:

- Slope < 0
- Infection Trend: R² > 0.70
- Mortality Trend: R² > 0.80

8. Final Classification

The final results were categorized into:

- Infection Only
- Mortality Only
- Infection & Mortality



## Business Problem

Large volumes of COVID-19 data are collected daily from countries around the world. However, the complexity and scale of these datasets make it difficult to identify meaningful trends, compare country performance, and evaluate the effectiveness of public health interventions.

As a result, healthcare decision-makers may face challenges in allocating medical resources, evaluating vaccination strategies, and responding effectively to new waves of the pandemic.

This project addresses these challenges by transforming raw COVID-19 data into meaningful insights through data analysis and interactive visualizations, enabling evidence-based decision-making and supporting future pandemic preparedness.


## Project Objectives

- Analyze global COVID-19 trends using historical data.
- Evaluate the impact of vaccination programs on infection and mortality trends.
- Identify meaningful patterns and insights to support public health decision-making.
- Support evidence-based healthcare resource allocation.
- Compare pandemic management performance across countries and regions.
- Communicate analytical findings through interactive dashboards and data storytelling.


## Q1 Key Findings

The regression analysis identified countries with sustained decreasing pandemic trends based on infection and mortality indicators.

Countries were classified into three categories according to the regression results:

- Infection Only
- Mortality Only
- Infection & Mortality

These findings provide an objective overview of countries that demonstrated stable improvements during the analyzed period and support further evaluation in the following business questions.