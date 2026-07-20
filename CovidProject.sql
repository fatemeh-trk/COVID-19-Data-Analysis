SELECT * FROM CovidDeaths
WHERE continent is null

SELECT * FROM CovidVaccinations

--SELECTING DATA we are going to use
SELECT location,date,total_cases,new_cases,total_deaths,population
FROM CovidDeaths
ORDER BY 1,2 DESC

--the total cases vs total deaths in each day depend on total death and case from first.
-- probablity of dying if you get covid in ur country
SELECT location,date,total_cases,total_deaths,(total_deaths/total_cases)*100 AS death_case_percent,population
FROM CovidDeaths
WHERE location like '%ran' AND continent is not null
ORDER BY location DESC

--total cases vs population
--percentage of population got covid
SELECT location,date,total_cases,((total_cases)/population)*100 AS case_pop_percent,population
FROM CovidDeaths
WHERE location = 'Iran' AND continent is not null
ORDER BY date

--country with most infection rate compared to population
SELECT location,MAX(total_cases/population)*100 AS Highest_case_pop_percentage ,population
FROM CovidDeaths
WHERE continent is not null
GROUP BY location , population
ORDER BY 2 DESC

--country with most die rate compared to population of countries not continents
SELECT location , MAX(cast(total_deaths as int)) AS total_death ,MAX(cast(total_deaths as int)/population)* 100 AS death_pop_percent,population 
FROM CovidDeaths
WHERE continent is not null
GROUP BY location,population
ORDER BY 3 DESC

--lets work with continents
SELECT location , MAX(cast(total_deaths as int)) AS total_death 
FROM CovidDeaths
WHERE continent is null
GROUP BY location

--showing the continet with highest death count per population
SELECT location , MAX(cast(total_deaths as int)) AS total_death ,MAX(cast(total_deaths as int)/population)*100 AS death_pop_continent_percent,population
FROM CovidDeaths
WHERE continent is null 
GROUP BY location,population
ORDER BY death_pop_continent_percent DESC

--GLOBAL NUMBERS
SELECT date , SUM(cast(total_cases as int))
FROM CovidDeaths
WHERE continent is not null
GROUP BY date
ORDER BY 1 

SELECT SUM(new_cases),SUM(cast(new_deaths as int)),(SUM(cast(new_deaths as int))/SUM(new_cases))*100 as death_case_globe
FROM CovidDeaths
WHERE continent is not null
--GROUP BY date
--ORDER BY date


--joining two tables
select * from
CovidDeaths dea join 
CovidVaccinations vac
on dea.location = vac.location
and dea.date = vac.date

--looking to total population and vaccination(new vaccinations per day)
SELECT vacc.continent,dea.location,population,vacc.new_vaccinations,vacc.date
FROM CovidDeaths dea
JOIN CovidVaccinations vacc
ON dea.location=vacc.location AND vacc.date=vacc.date
WHERE vacc.continent is not null 


SELECT vacc.continent,dea.location,dea.date,population,vacc.new_vaccinations,SUM(CONVERT(int,vacc.new_vaccinations)) OVER (Partition By dea.location Order By dea.location , dea.date) as people_vaccinated_count
--, (MAX(people_vaccinated_count)/population)*100
FROM CovidDeaths dea
JOIN CovidVaccinations vacc
ON dea.date=vacc.date AND dea.location=vacc.location
WHERE vacc.continent is not null

--درصد تعداد افراد واکسن شده از ابتدا تا ان تاریخ به کل جمعیت 
--USING CTE to solve the erorr

WITH people_vaccinated_CTE(continent,location,date,population,new_vaccinations,people_vaccinated_count)
AS
(
SELECT dea.continent,dea.location,dea.date,population,vacc.new_vaccinations,SUM(CONVERT(int,vacc.new_vaccinations))
OVER (Partition By dea.location Order By dea.location , dea.date) as people_vaccinated_count
--,(MAX(people_vaccinated_count)/population)*100 
FROM CovidDeaths dea
JOIN CovidVaccinations vacc
ON dea.date=vacc.date AND dea.location=vacc.location
WHERE vacc.continent is not null
)
SELECT * ,((people_vaccinated_count)/population)*100
FROM people_vaccinated_CTE

