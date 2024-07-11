import pandas as pd
import sqlite3

def data_loading_method(df):

    # after importing sqlite3 we should connect our database using sqlite3.connect() method  passing database name inside it.
    conn=sqlite3.connect('Web_database.sqlite')

    # after using various query through pyhton we should need of cursor() method object
    cur=conn.cursor()

    # creating schemas and table in the database for storing taxi_details
    c_create='create table Taxi_Detail_jh(tpep_pickup_datetime datetime,tpep_dropoff_datetime datetime,passenger_count int,trip_distance float,fare_amount float,trip_duration Date,trip_speed float)'
    cur.execute(c_create)

    # transfering data from dataframe to created table
    df.to_sql("Taxi_Detail",conn,if_exists="append",index=False)

    # now we are saving the result
    conn.commit()

    # closing the connection
    conn.close()

    print("data_loading_method successfully executed")
