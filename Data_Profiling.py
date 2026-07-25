import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/CovidDeaths.csv")

##Which countries have demonstrated a sustained decrease in COVID-19 infection and mortality rates relative
##to their population over time?

df["date"] = pd.to_datetime(df["date"])

##print(df[["location","date","population","new_cases","total_cases","new_deaths","total_deaths"]].sample(30))

df_Q1 = df.sort_values(["location","date"])
#print(df_Q1.loc[df_Q1["location"] == "Iran" ,["location","date"]])


case_rate = (df_Q1["total_cases"] / df_Q1["population"]).round(6)
df_Q1["case_rate"] = case_rate
death_rate = (df_Q1["total_deaths"] / df_Q1["population"]).round(6)
df_Q1["death_rate"] = death_rate


new_case_rate = (df_Q1["new_cases"] / df_Q1["population"]).round(6)
df_Q1["new_case_rate"] = new_case_rate
new_death_rate = (df_Q1["new_deaths"] / df_Q1["population"]).round(6)
df_Q1["new_death_rate"] = new_death_rate

#smoothing new_cases and new_deaths

df_q1_1 = df_Q1.loc[df_Q1["location"]== "Iran",["date","case_rate","death_rate","new_death_rate","new_case_rate","new_deaths","new_cases"]]
new_cases_ma7 = df_q1_1.new_cases.rolling(7).mean()
new_deaths_ma7 = df_q1_1.new_deaths.rolling(7).mean()
df_q1_1["new_cases_ma7"] = new_cases_ma7
df_q1_1["new_deaths_ma7"] = new_deaths_ma7


##print((df_q1_1[["date","new_cases","new_cases_ma7"]]).tail(30))
df_q1_1=df_q1_1.set_index("date")
plt.figure(figsize=(8,6))
plt.plot(df_q1_1["new_cases_ma7"],label='7-Day Moving Average')
plt.title("7-Day Moving Average of Daily COVID-19 Cases in Iran")
plt.xlabel('Date')
plt.ylabel('7-Day Moving Average of New Cases')
plt.grid()
plt.legend()
plt.show()
print(df_q1_1[["new_cases_ma7"]])







df_q1_2 = df_Q1.loc[df_Q1["location"]== "Germany",["date","case_rate","death_rate","new_death_rate","new_case_rate","new_deaths","new_cases"]]
new_cases_ma7 = df_q1_2.new_cases.rolling(7).mean()
new_deaths_ma7 = df_q1_2.new_deaths.rolling(7).mean()
df_q1_2["new_cases_ma7"] = new_cases_ma7
df_q1_2["new_deaths_ma7"] = new_deaths_ma7

##print((df_q1_2[["date","new_cases","new_cases_ma7"]]).tail(30))













