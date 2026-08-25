import numpy as np
import pandas as pd

def main():

    flights = pd.read_csv("../../data/raw/AirPassengers.csv")       
     

    flights['data'] = pd.to_datetime(flights["time"])
    flights['year'] = flights['data'].dt.year
    flights['month'] = flights['data'].dt.month

    month_number_to_name = {0: "January",
                            1: "February",
                            2: "March",
                            3: "April",
                            4: "May",
                            5: "June",
                            6: "July",
                            7: "August",
                            8: "September",
                            9: "October",
                            10: "November",
                            11: "December"}

    flights["month"] = flights.month.map(month_number_to_name)
    flights["passengers"] = flights["AirPassengers"]
    flights = flights.drop(["AirPassengers", "time"], axis=1)
    path ="../result/"; 
    flights.to_csv(path+"flights.csv", index=False)


if __name__ == "__main__":
    main()
