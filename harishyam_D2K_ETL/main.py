from Data_Extraction import extraction_and_Dataframe_method
from Data_transformation import data_processing_method
from Data_loading import data_loading_method
from Data_visualization import data_visualization_method
import pandas as pd

def main(year,taxi_type):
    print("*************** STARTING THE PIPLINE ********************")
    print()
    print(f"fetching details of year --> {year} and taxi_type --> {taxi_type} ")

    print()
    print("**************** STARTING THE DATA EXTRACTION PROCESS ******************")
    print()
    final_df = extraction_and_Dataframe_method(year,taxi_type)

    print()
    print("**************** STRATING THE DATA TRANSFORMATION PROCESS *****************")
    print()
    df = data_processing_method(final_df)

    print()
    print("**************** SHOWING SOME INSIGHT OF THE TRIP ********************")
    print()
    # showing the value of average trip per day
    average_trip_per_day = round(df["passenger_count"].astype(int).sum()/len(df))
    print(f" average trip per day --> {average_trip_per_day}")

    print()

    # showing the value of average fare per day
    average_fare_per_day = round(df["fare_amount"].sum()/len(df))
    print(f" average fare per day --> {average_fare_per_day}")

    print()
    print("************** STARTING DATA LOADING PROCESS ******************")
    print()
    data_loading_method(df)

    print()
    print("************** STARTING DATA VISUALIZATION PROCESS ******************")
    print()
    print("Data visualization process started !!!!!!")
    data_visualization_method()

if __name__ == "__main__":
    try:
        year = "2019"
        taxi_type = "yellow"

        main(year,taxi_type)
        
    except Exception as e:
        print(f" we got an error in the middle of the process --> {e}")