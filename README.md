![Dengue-Fever](https://www.niaid.nih.gov/sites/default/files/styles/image_style_landscape_md/public/FemaleAAegyptiMosquito_0.jpg?itok=ejsHcfmR)


# dengue-fever-analytics
A simple data analytics project to see the relationship between rainfall ,temperature and the increasing amount of dengue cases in Singapore.


# Datasets

- [RainFall Data](https://data.gov.sg/dataset/rainfall-monthly-number-of-rain-days)
- [Temperature Data](https://www.climatestotravel.com/climate/singapore)
- [Dengue Cases](https://data.gov.sg/dataset/weekly-infectious-disease-bulletin-cases)

# Approach to the Project
```
First,we used the csv files from the gov data site . As there was no weekly temperature given, we used webscraping and the Beautiful Soup module
to scrape data for the average temperature in 2020. Furthermore, for data cleaning, as there were differences in the names  of the  columns , we used 
regex subsituiton to make the columns for the months consistent.For the data visualization, we used matplotlib to plot graphs of temperature and rainfall
against the number of dengue cases in Singpore. Lastly,we used machine learning linear regression model to determine the relationship between these mutiple variables
and the number of dengue fever cases in Singapore.
```
