import pandas as pd
import numpy as np
import matplotlib as plt
from typing import List, Dict
import seaborn as sns

class DataAnalyzer:
    def __init__(self, songs : List):

        self.songs = songs
        self.df = self._convert_to_dataframe()
    
    def _convert_to_dataframe(self) -> pd.DataFrame: #praivte method

        if not self.songs:
            return pd.DataFrame() # empty table
        
        data = [song.__dict__ for song in self.songs] # saving information about each song by using dictionaries!
        return pd.DataFrame(data)
    
    def partition_songs(self) -> pd.DataFrame:

        # partition songs by mean of numeric featurs

        if self.df.empty:
            return pd.DataFrame()
        
        numeric_featurs = ['popularity', 'duration_ms', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

        partition = self.df.groupby('genre')[numeric_featurs].mean()
        return partition

    def get_matrix(self) -> pd.DataFrame:

        if self.df.empty:
            return pd.DataFrame()
        
        features = ['_danceability', '_energy', '_loudness', '_speechiness', '_acousticness', '_instrumentalness', '_liveness', '_valence', '_tempo']
        matrix = self.df[features].corr(method = 'pearson')
        return matrix        
