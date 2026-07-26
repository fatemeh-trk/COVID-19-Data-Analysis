import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import os

df = pd.read_csv("Data/CovidDeaths.csv")

##Which countries have demonstrated a sustained decrease in COVID-19 infection and mortality rates relative
##to their population over time?


df["date"] = pd.to_datetime(df["date"])
df_Q1 = df.sort_values(["location","date"])



df_Q1["case_rate"] = (df_Q1["total_cases"] / df_Q1["population"]).round(6)
df_Q1["death_rate"] = (df_Q1["total_deaths"] / df_Q1["population"]).round(6)

df_Q1["new_case_rate"] = (df_Q1["new_cases"] / df_Q1["population"]).round(6)
df_Q1["new_death_rate"] = (df_Q1["new_deaths"] / df_Q1["population"]).round(6)



new_cases_ma7 = df_Q1.groupby("location")["new_cases"].rolling(7).mean()
new_deaths_ma7 = df_Q1.groupby("location")["new_deaths"].rolling(7).mean()

new_cases_ma7 = new_cases_ma7.reset_index(level = "location" , drop = True)
new_deaths_ma7 = new_deaths_ma7.reset_index(level = "location" , drop = True)


df_Q1["new_deaths_ma7"]= new_deaths_ma7
df_Q1["new_cases_ma7"]= new_cases_ma7



results=[]
for location , loc_Data in df_Q1.groupby("location"):
    
    clean_loc_Data = loc_Data.dropna(subset=["new_cases_ma7"]).tail(180)

    if len(clean_loc_Data) >= 30:
        y = clean_loc_Data["new_cases_ma7"]
        x = np.arange(len(clean_loc_Data))
    
        reg_result = linregress(x,y)
        slope = (reg_result.slope).round(4)
        rvalue = reg_result.rvalue
        r_two = (rvalue ** 2).round(4)

        results.append({
            "location":location,
            "slope":slope,
            "r_squared":r_two})

reg_df = pd.DataFrame(results)
q1_result = reg_df[(reg_df["slope"] < 0)& (reg_df["r_squared"] > 0.7)]


os.makedirs("Output", exist_ok=True)

q1_result.to_csv(
    "Output/q1_regression_results.csv",
    index=False
)





















