import numpy as np
import logging as log
from geopy.distance import geodesic as GD

log.basicConfig(filename='../logs/log.txt', format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')


class Util:
    """
    A class that contains helper functions
    """
    def get_missing(self, df):
        """
        A method for getting missing values
        Args:
            df: dataframe
        Return:
            %missing: Percent of missing values
            missingCount: The number of missing values
        """
        totalCells = np.product(df.shape)
        missingCount = df.isnull().sum()
        totalMissing = missingCount.sum()
        log.info("Get the missing values")
        return round((totalMissing/totalCells), 2) * 100, missingCount
    
    def drop_column(self, df, col):
        """
        Drops the colum from the dataframe
        Args:
            df: dataframe
            col: column name
        Return:
            df: The data frame with the removed column
        """
        df = df.drop(col, axis=1)
        return df

    def get_distance(self, start, end):
        """
        Measures distance between 2 places
        Args:
            start: starting latitude and longitude
            end: ending latitiude and longtude
        Returns:
            distance: Measured distance in km
        """   
        place1 =(float(start[0]),float(start[1]))
        place2 =(float(end[0]),float(end[1]))
        return GD(place1,place2).km

    def split_date(self, date):
        """
        Split the date in to year, month, and day
        Args:
            date: date input
        Return:
            year: The year
            month: The month
            day: The day
            hour: The hour
        """
        date = date.split(" ")
        hour = date[1]
        date = date[0].split("-")
        year = date[0]
        month = date[1]
        day = date[2]
        return year, month, day, hour
    def split_time(self, time):
        """
        Split the time to hour, minute and seconds
        Args:
            time: The time input
        """
        hour, minute, second = time.split(":")
        return hour, minute, second