# Restaurant Rating Prediction

## Description
The Restaurants Rating Prediction project is a regression-based analysis aiming to predict restaurant ratings using a dataset sourced from Zomato.  It explores data visualization, model building, and deployment as a web application using Flask. With 56,250 records, this dataset encompasses various factors influencing restaurant ratings, including location, cuisine, cost, and service features. The project utilizes regression techniques to predict restaurant ratings, facilitating insights into factors contributing to higher or lower ratings on the Zomato platform.

## Table of Contents
- [Key Features](#Key-Features)
- [Dependencies](#Dependencies)
- [Dataset](#Dataset)
- [Tools and Libraries](#Tools-and-Libraries)
- [Folder Structure](#Folder-Structure)
- [Usage Instructions](#Usage-Instructions)
- [Models used and Accuracy results](#Models-used-and-Accuracy-results)
- [Deployment](#Deployment)

## Key Features
- Data Analysis and Visualization: Conducts insightful analysis on restaurant ratings, prices, cuisines, and more.
- Model Development: Trains and compares multiple regression models to find the best predictor of ratings.
- Web Application Deployment: Creates an interactive web interface for users to get predictions based on various restaurant attributes.
   
## Dependencies
-	Python 3.x
-	Libraries: pandas, NumPy, matplotlib, seaborn, plotly, sklearn, Flask
-	IDE: PyCharm Community Edition (recommended)

## Dataset
-	Source: The dataset used for this project is taken from kaggle [https://www.kaggle.com/datasets/bansodesandeep/zomatocsv]
-	Format: CSV
-	Size: 56250 records
### Features: 
1. url </B> - contains the url of the restaurant in the zomato website
2. address - contains the address of the restaurant in Bengaluru
3. name - contains the name of the restaurant
4. online_order - whether online ordering is available in the restaurant or not
5. book_table - table book option available or not
6. rate - contains the overall rating of the restaurant out of 5
7. votes - contains total number of ratings for the restaurant as of the above-mentioned date
8. phone - contains the phone number of the restaurant
9. location - contains the neighborhood in which the restaurant is located
10. rest_type - restaurant type
11. dish_liked - dishes people liked in the restaurant
12. cuisines - food styles, separated by comma
13. approx_cost(for two people) - contains the approximate cost of meal for two people
14. reviews_list - list of tuples containing reviews for the restaurant, each tuple
15. menu_item - contains list of menus available in the restaurant
16. listed_in(type) - type of meal
17. listed_in(city) - contains the neighborhood in which the restaurant is listed

## Tools and Libraries
1.	Pandas: Data manipulation and analysis.
2.	NumPy: Numerical computing.
3.	Matplotlib & Seaborn: Data visualization.
4.	Plotly: Interactive visualizations.
5.	Scikit-learn: Machine learning models.
6.	Flask: Web framework for deployment.
   
## Folder Structure
#### o	zomato_df.csv: Clean dataset for the program.
#### o	`my_project/` 
-	`model.py`: Contains model training and saving code
-	`templates/`: Holds HTML files for the web interface 
-	`index.html`: Main web page for user input and prediction display
-	`app.py`: Integrates model and HTML code to create the web application
-	`zomato_df.csv`: Cleaned dataset used by the model

## Usage Instructions
1.	Install Dependencies: 
-	Jupyter Notebook 
-	pip install `pandas` `numpy` `matplotlib` `seaborn` `plotly` `sklearn flask`
-	`PyCharm` Community version

2.	Data Preprocessing: 
-	Import 'zomato.csv' and perform data cleaning.
-	Handle null values, duplicate records, and unnecessary columns.
3.	Exploratory Data Analysis:  
- Visualizing and understanding the data. Explore and visualize restaurant-related data including famous restaurants, booking options, online delivery, and rating distributions.
4.	Model Creation: 
-	Convert categorical variables to numeric format for model training.
-	Split the dataset into training and testing sets.
-	Train models such as Linear Regression, Random Forest Regressor, and Extra Trees Regressor.

5.	Deployment and Integration: 
-	 Generate a pickle file for the trained model (`model.pkl`).
-	Use Flask to deploy the model as a web application.
-	The web application enables users to input restaurant-related parameters and predicts ratings using the trained model.

## Models used and Accuracy results
#### o	Best Performing Model: Extra Trees Regressor with 93.41% accuracy
#### o   Other Models Explored: 
- Linear Regression (Accuracy: 22.81%)
- Random Forest Regressor (Accuracy: 88.09%)

## Deployment
1.	 Run the Web Application: 
-	Navigate to the `my_project` directory in PyCharm. 
-	python `app.py`: Contains Script for creating the regression model. Integrates the model and HTML code.
-	Execute python `app.py`.
2.	 Access the Web Interface: 
-	Open `index.html` in your web browser.
3.	Provide Input and Get Prediction: 
-	Enter values for restaurant attributes in the text boxes.
-	Click the "Predict" button.
-	The predicted rating will be displayed on the web page.
