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
            "infection_slope":slope,
            "infection_r_squared":r_two})

reg_df = pd.DataFrame(results)
q1_result_1 = reg_df[(reg_df["infection_slope"] < 0)& (reg_df["infection_r_squared"] > 0.7)]



results_2 = []
for location , loc_Data in df_Q1.groupby("location"):
    clean_non_values = loc_Data.dropna(subset=["new_deaths_ma7"]).tail(180)

    if(len(clean_non_values)> 30):
        y = clean_non_values["new_deaths_ma7"]
        x=np.arange(len(clean_non_values))

        reg_result_2 = linregress(x,y)
        
        slope2 = (reg_result_2.slope).round(4)
        rvalue2 = reg_result_2.rvalue
        r_two2 = (rvalue2 ** 2).round(4)

        results_2.append({
            "location":location,
            "mortality_slope":slope2,
            "mortality_r_squared":r_two2})
reg_df_2 = pd.DataFrame(results_2)
q1_result_2 = reg_df_2[(reg_df_2["mortality_slope"] < 0)& (reg_df_2["mortality_r_squared"] > 0.8)]




q1_final_technical_result = q1_result_1.merge(q1_result_2 ,on = "location",how = "outer")

q1_final_status = np.select(condlist = [(q1_final_technical_result["infection_slope"].notna()) &(q1_final_technical_result["mortality_slope"].notna())  ,
                        (q1_final_technical_result["infection_slope"].isna())& (q1_final_technical_result["mortality_slope"].notna())],
          choicelist = ["infection & mortality" , "mortality only"],
          default = "infection only")

q1_final_technical_result["status"] = q1_final_status




#To what extent did COVID-19 vaccination programs contribute to reducing infection and mortality trends across different countries?

vaccination_df = df.groupby("location")["people_fully_vaccinated_per_hundred"].apply(lambda x:x.dropna().iloc[-1] if not x.dropna().empty else np.nan).reset_index(name = "vaccination_percent")

vaccination_df = vaccination_df.dropna(subset=["vaccination_percent"])
vaccination_quartiles = vaccination_df["vaccination_percent"].quantile([0.25,0.5,0.75])

q1 = vaccination_quartiles.loc[0.25]
q2 = vaccination_quartiles.loc[0.5]
q3 = vaccination_quartiles.loc[0.75]

choices = ["low","medium"]
conditions = [(vaccination_df["vaccination_percent"] <= q1) ,
              (vaccination_df["vaccination_percent"] <= q3)]


vaccination_df["vaccination_group"] = np.select(conditions,choices,default="high") 



