# Importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


header = st.container()
dataset = st.container()
visuals = st.container()

with header:
	st.title('Kenyan Covid19 Data and Trend.')

	st.header('Introduction')

	st.caption('This project is ment to show the trend of Covid19 cases in kenya, final update was 24th march 2022.')




with dataset:

	st.title('Project overview and data.')
	st.caption('The objective of this analysis is to assess the prevalence of Covid in the county and view the trend though out a timeline.')
	
	# Loading the dataset
	st.header('A preview of the dataset.')
	df = pd.read_csv('/home/francis/Downloads/owid-covid-data.csv',parse_dates=['date'])
	df.drop(['new_cases_smoothed','iso_code','icu_patients_per_million',], axis=1, inplace=True)
	Kenya = df[df['location'] == 'Kenya']
	preview=Kenya.tail()
	st.table(preview)
 
#
#

# objects= [cols for cols in df_poland if df_poland[cols].dtypes=='O']

#st.bar_chart(df[['Date of surgery','Total hospital stay']])
with visuals:

	st.header('Trend on total Covid cases in Kenya from February-2020 to March-2022')
	# time series plot for trend of post operative stays between 2019 and 2020 
	fig, ax = plt.subplots()
	sns.set_style("darkgrid")
	sns.lineplot(x='date',y='total_cases',data=Kenya, hue='location').set(title='Trend on total Covid cases in Kenya from February-2020 to March-2022')
	plt.show()
	st.pyplot(fig)

	# Bar plot to check  the frequency of total hospital days
	st.header('Trend on new Covid19 cases upto 24th March 2022')
	fig, ax = plt.subplots()
	sns.set_style("darkgrid")
	sns.lineplot(x='date',y='new_cases',data= Kenya,hue='location').set(title="Trend on new Covid19 cases upto 24th March 2022")

	st.plotly_chart(fig)

	# plotting to see the trend of people who stayed long in the hospital and whether they were alive or dead at the end

	st.header("Trend on deaths due to Covid19 up to the 24th of March 2022")
	fig, ax = plt.subplots()
	sns.set_style("darkgrid")
	sns.lineplot(x='date',y='new_deaths',hue='location',data=Kenya).set(title="Trend on deaths due to Covid19 up to the 24th of March 2022")
	st.plotly_chart(fig)

	# plotting to see the type of surgery that makes people stay for long in hospital

	st.header('Trend on Testing_rate for Covid19 up to the 24th of March 2022')
	# plotting for the testing rate
	fig, ax = plt.subplots()
	sns.set_style("darkgrid")
	sns.lineplot(x='date',y='new_tests',hue='location',data=Kenya).set(title="Trend on Testing_rate for Covid19 up to the 24th of March 2022")
	st.plotly_chart(fig)

	st.header('Trend on Positive rate for Covid19 up to the 24th of March 2022')
	# plotting for the testing rate
	fig, ax = plt.subplots()
	sns.set_style("darkgrid")
	sns.lineplot(x='date',y='positive_rate',hue='location',data=Kenya).set(title="Trend on Positive rate for Covid19 up to the 24th of March 2022")
	st.plotly_chart(fig)

	st.header('Trend on new vaccinations against Covid19 up to the 24th of March 2022')
	# plotting for the testing rate
	fig, ax = plt.subplots()
	sns.set_style("darkgrid")
	sns.lineplot(x='date',y='new_vaccinations',hue='location',data=Kenya).set(title="Trend on new vaccinations against Covid19 up to the 24th of March 2022")
	st.plotly_chart(fig)

	st.header('Timeline of People vaccinated vs those fully Vaccinated in Kenya upto 24th March 2022')
	# plotting the people vaccinated vs people fully vaccinated
	Kenya[['people_fully_vaccinated','people_vaccinated']].plot(figsize=(15,8),title='Timeline of People vaccinated vs those fully Vaccinated in Kenya upto 24th March 2022')
	st.plotly_chart(fig)
