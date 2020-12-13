# dengue-fever-analytics
A simple data analytics project to see the relationship between rainfall ,temperature and the increasing amount of dengue cases in Singapore.


# Datasets

- [RainFall Data](https://data.gov.sg/dataset/rainfall-monthly-number-of-rain-days)
- [Temperature Data](https://www.climatestotravel.com/climate/singapore)
- [Dengue Cases](https://data.gov.sg/dataset/weekly-infectious-disease-bulletin-cases)

# Approach to the Project
```
First,we used the csv files from the gov data site . As there was no weekly temperature given, we used webscraping and the beautiful soup module
to scrape data for the average temperature in 2020. Furthermore, for data cleaning, as there were differnces in the type of columns , we used 
regex subsituiton to make the columns for the months consitent.For the data visualization, we used matplotlib to plot graphs of temperature and rainfall
against the number of dengue cases in Singpore. Lastly,we used machine learning to determine the relationship between these mutiple variables.
```
