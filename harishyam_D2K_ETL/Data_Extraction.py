import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyarrow.parquet as pq
from io import BytesIO

def extraction_and_Dataframe_method(year,taxi_type):
    try:
        print(f"year : {year} , taxi_type : {taxi_type}")

        url = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
    
        response = requests.get(url)
        response.raise_for_status()

        # this will read the html document and save the html doc into var 'html_data'
        html_data = BeautifulSoup(response.text,'html.parser')
    
        final_df = pd.DataFrame()

        # since entire details avaliable on "class_='faq-answers'" so we taking that part from "html_data"
        for data in html_data.find_all(class_="faq-answers"):
            if data["id"] == "faq" + year :  # this will take the desired year
                for li_tag in data.find_all("ul"): # Since all file link is reside in <ul> tag so we are takin this one
                    for a_tag in li_tag.find_all("a"):
                        if taxi_type.lower() in  a_tag["href"]: # Now we are fetching the file url
                            taxi_link = a_tag["href"]
                            
                            par_data_resp = requests.get(taxi_link) # hitting the file data
                            par_data_resp.raise_for_status()
                            
                            buffer = BytesIO(par_data_resp.content) # saving the file data 
                            df = pd.read_parquet(buffer)

                            final_df = final_df._append(df)
        print("extraction_and_Dataframe_method successfully executed")
        
        return final_df
    except Exception as e:
        print(f" we got an error in creating connection --> {e}")
        return