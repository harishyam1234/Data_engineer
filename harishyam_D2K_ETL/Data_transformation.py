import pandas as pd

def data_processing_method(df):
    
    # The dataset includes fields such as pickup time, drop-off time, trip distances, fares, and passenger counts.
    df = df[["tpep_pickup_datetime","tpep_dropoff_datetime","passenger_count","trip_distance","fare_amount"]]

    df.dropna(how="all",inplace=True)
    df["passenger_count"].fillna(0.0,inplace=True)
    df["trip_distance"].fillna(0.00,inplace=True)
    df["fare_amount"].fillna(0.00,inplace=True)
    df=df[df["trip_distance"]!=0.00].reset_index(drop=True)

    # Creating the column "trip_duration" 
    df["trip_duration"] = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]

    # Creating the column "trip_speed"
    df["trip_speed"] = df["trip_distance"] / (df["trip_duration"].dt.total_seconds()/3600)

    print("data_processing_method successfully executed")

    return df
    