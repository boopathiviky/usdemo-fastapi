from sklearn.neighbors import BallTree
from sklearn.neighbors import KDTree
import numpy as np
import pandas as pd
"""
The Package for Proximity

"""

class proximity:
    """
    class Proximity

    ...

    Attributes
    ----------
    data : pandas.dataframe
        A data with Latiude and Longitude for proximity checking
    column : str
        The name of column to be used
        eg:StoreID/MasterId/HotelCode
    """
    def __init__(self,data,column):
        self.data=data.reset_index()
        self.tree = BallTree(np.deg2rad(data[['Latitude', 'Longitude']].values), metric='haversine')
        self.column=column
        
    def get_data(self,radius,ID):
        """
        Function get_data
        ...

        Attributes
        ----------
        radius: float
            returns the data within the radius--------(Miles)
        
        ID: int
             The ID in the column......
        -----------------------------------------------     
        """
        self.distance=radius
        self.ID=ID
        earth_radius_in_miles = 3958.8
        radi = self.distance / earth_radius_in_miles
        ND=self.data[self.data[self.column]==self.ID]
        lat=ND['Latitude'].values[0]
        lon=ND['Longitude'].values[0]
        ins,dis=self.tree.query_radius(np.deg2rad(np.c_[lat,lon]), r=radi,return_distance=True) 
        ND=self.data.iloc[ins[0]]
        ND['Distance']=dis[0] 
        ND['Distance']=ND['Distance']*earth_radius_in_miles
        ND=ND[ND[self.column]!=self.ID]
        return ND

    
class Demoproximity:
    """
    class demographic Proximity

    ...

    Attributes
    ----------
    data : pandas.dataframe
        A data with Latiude and Longitude for proximity checking
    column : str
        The name of column to be used
        eg:StoreID/MasterId/HotelCode
    """
    def __init__(self,data):
        self.data=data.reset_index()
        self.tree = BallTree(np.deg2rad(data[['Latitude', 'Longitude']].values), metric='haversine')
        #self.column=column
        
    def get_data(self,radius,lat,lon):
        """
        Function get_data
        ...

        Attributes
        ----------
        radius: float
            returns the data within the radius--------(Miles)
        
        lat,lon: float
             The lat and lon as float......
        -----------------------------------------------     
        """
        self.distance=radius
        self.lat=lat
        self.lon=lon
        earth_radius_in_miles = 3958.8
        radi = self.distance / earth_radius_in_miles
        #ND=self.data[self.data[self.column]==self.ID]
        #lat=ND['Latitude'].values[0]
        #lon=ND['Longitude'].values[0]
        ins,dis=self.tree.query_radius(np.deg2rad(np.c_[self.lat,self.lon]), r=radi,return_distance=True) 
        ND=self.data.iloc[ins[0]]
        ND['Distance']=dis[0] 
        ND['Distance']=ND['Distance']*earth_radius_in_miles
        #ND=ND[ND[self.column]!=self.ID]
        return ND
