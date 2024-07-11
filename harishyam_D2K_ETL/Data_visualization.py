import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sqlite3

def data_visualization_method():
    
    conn=sqlite3.connect('Web_database.sqlite')
    cur=conn.cursor()

    # What are the peak hours for taxi usage?
    ''' 
        In this Query we are 1st fetching the an hour from "tpep_pickup_datetime" and then count the
        how many passenger was booked on that particular hours by this way we find the peak hours for
        taxi usage
    '''
    cur.execute(''' SELECT round(strftime("%H.%M",tpep_pickup_datetime)) as trip_time,count(passenger_count) from Taxi_Detail 
                    WHERE strftime("%Y",tpep_pickup_datetime) != "2088"
                    group by round(strftime("%H.%M",tpep_pickup_datetime)) ''')
    peek_hour=cur.fetchall()

    df2=pd.DataFrame(peek_hour)

    df2.columns=["trip_time","No_Of_Passenger"]
    df2["trip_time"]=df2["trip_time"].astype("int")

    plt.figure(figsize=(20,6))
    plt.title("** What are the peak hours for taxi usage **")
    sns.barplot(x = 'trip_time', y = 'No_Of_Passenger', data = df2,color="orange")

    x=df2["trip_time"].to_list()
    y=df2["No_Of_Passenger"].to_list()
    for i, (xi,yi) in enumerate(zip(x,y)):
        plt.annotate(f"{yi}",(xi,yi),textcoords="offset points",xytext=(0,10),ha="center")

    plt.tight_layout()
    plt.show()

    # How does passenger count affect the trip fare?
    ''' 
        In this Query we are 1st fetching the passenger count and then calculate the average fare for 
        that passenger count and also removig the outlier from dataset for getting better result
        by this way we are getting the result of How does passenger count affect the trip fare
    '''

    cur.execute(""" SELECT passenger_count,round(sum(fare_amount)/count(passenger_count)) as avg_fare from Taxi_Detail
                    where fare_amount not in (623259.86,8000.3,6666.65,3004.0,0.01) and fare_amount>5
                    group by passenger_count """)
    trip_fare = cur.fetchall()

    df3=pd.DataFrame(trip_fare)

    df3.columns = ['passenger_count','fare_amount']
    df3['passenger_count'] = df3['passenger_count'].astype("int")
    df3['fare_amount'] = df3['fare_amount'].astype("float")

    plt.figure(figsize=(10,6))
    plt.title("** How does passenger count affect the trip fare **")
    sns.barplot(x = 'passenger_count', y = 'fare_amount', data = df3,color="green")

    x=df3["passenger_count"].to_list()
    y=df3["fare_amount"].to_list()
    for i, (xi,yi) in enumerate(zip(x,y)):
        plt.annotate(f"{yi}",(xi,yi),textcoords="offset points",xytext=(0,10),ha="center")

    plt.tight_layout()
    plt.show()

    # What are the trends in usage over the year?
    '''
        In this Query we are calculating the how many booking was happend over the year by picking
        up the year from "tpep_pickup_datetime" and sum the number of "passenger_count"
    '''

    cur.execute(""" SELECT strftime("%Y",tpep_pickup_datetime) year,sum(passenger_count) as booking from Taxi_Detail
                    WHERE strftime("%Y",tpep_pickup_datetime) != "2088"
                    GROUP by strftime("%Y",tpep_pickup_datetime) """)
    trends = cur.fetchall()

    df4=pd.DataFrame(trends)
    df4.columns = ["Year","Booking"]

    plt.figure(figsize=(10,6))
    plt.title("** the trends in usage over the year **")
    sns.lineplot(x = 'Year', y = 'Booking', data = df4,color="brown",marker="^",markersize=8)
    x=df4["Year"].to_list()
    y=df4["Booking"].to_list()

    for i, (xi,yi) in enumerate(zip(x,y)):
        plt.annotate(f"{yi}",(xi,yi),textcoords="offset points",xytext=(0,10),ha="center")
    plt.tight_layout()
    plt.show()