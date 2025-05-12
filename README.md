# Automobile
Automobile Data Analysis with Seaborn & Pandas
This project performs data analysis and visualization on an automobile dataset using Python, Seaborn, Matplotlib, and Pandas. The analysis includes univariate, bivariate, and multivariate visualizations, as well as descriptive statistics and basic filtering operations on the dataset.
📁 Dataset
The dataset used is Automobile (1).csv. Make sure the file is present in the same directory as the script. It contains various features related to automobile specifications and pricing.
________________________________________
📊 Features of the Script
1. Univariate Analysis
•	Distribution plots of the normalized_losses column.
•	Plots include KDE curves, rug plots, and basic histograms.
2. Bivariate Analysis
•	Joint plots for analyzing relationships between engine_size and horsepower.
•	Hexbin plots are used to visualize the concentration of values.
3. Multivariate Analysis
•	Pair plots involving normalized_losses, engine_size, and horsepower to analyze multiple variable relationships.
4. Categorical vs Continuous
•	Strip plots and swarm plots to visualize horsepower against categorical variables like fuel_type.
•	Box plots for comparing distributions grouped by number_of_doors, body_style, and engine_location.
•	Count plots to count occurrences of body_style grouped by engine_location.
5. Regression Analysis
•	Linear regression line plot between horsepower and peak_rpm using lmplot.
________________________________________
📈 Pandas-Based Data Analysis
•	Reading and displaying data (head() and info()).
•	Calculating mean and max of price.
•	Identifying the cars with the highest and lowest prices.
•	Counting cars with horsepower > 100.
•	Displaying info for hatchback cars.
•	Displaying top 3 most common car makers.
•	Filtering cars based on price and body style conditions.
________________________________________
📌 Requirements
Install the required libraries using pip:
bash
pip install pandas, seaborn, matplotlib
