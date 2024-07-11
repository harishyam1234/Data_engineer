# This Pipeline is created by using Python,BeautifulSoup,Seaborn,Mathplotlibs

# --> For excecuting this we need to run the "main.py" python script and also pass two attribute for filtering the various url the 1st one is for which year we need to extract the data i.e., "year" attribute and 2nd one is for which taxi type i.e., "taxi_type" and it automatically do all the step

""" 
# Extraction : 

With the help of python and web scraping we are able to extract the data from the given url for Extracting the Data we need two attributes 1st one "Year" and 2nd one is the type of taxi i.e., "Taxi_type" by passing this value we are able to extract the data from the url.
The "Data_Extraction.py" python script will perform the extraction part.

# Transformation:

All the extracted data are going to store into pandas dataframe for performing various transformation like droping the null value, handling the empty value for each column and printing the valuable insight from them in run time.
The "Data_transformation.py" will perform the Transformation part.

# Loading:

All the Transformed and filter data then going to be stored in "Web_database.sqlite" database inside "Taxi_Detail" table in Sqllite3 datawarehouse for performing various analysis.
The "Data_loading.py" python script will perform this step.

# Data Visualization:
With the help of Seaborn and mathplotlibs we are performing various visualization to get better understanding of data insight.
The "Data_visualization.py" python script will perform this step.

"""